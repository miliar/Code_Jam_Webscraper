#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

struct node {
	string letters;
	node* arr[26];
};

void insert(string word);
int find(string word, node* aNode);

node* first;

int main()
{
	ifstream fin;
	fin.open ("example.txt");

	ofstream fout;
	fout.open ("alien.txt");

	int L; // length of word
	fin >> L;

	int D; // dictionary size
	fin >> D;

	int N;
	fin >> N;

	first = new node();

	// read/process dictionary
	for( int i = 0; i < D; i++ ) {
		string word;
		fin >> word;
		//cout << word << endl;
		insert(word);
	}

	for( int i = 0; i < N; i++ ) {
		string word;
		fin >> word;
		cout << "Case #" << i+1 << ": " << find(word,first) << endl;
		fout << "Case #" << i+1 << ": " << find(word,first) << endl;
	}

	return 0;
}

int find(string word, node* aNode) {
	// empty
	if( word.length() == 0 ) {
		return 0;
	}
	// found word
	if( word.length() == 1 ) {
		size_t index = aNode->letters.find(word[0]);
		if( index == string::npos ) {
			return 0;
		}
		else {
			return 1;
		}
	}

	// group of possible letters
	if( word[0] == '(' ) {
		size_t index = word.find(')');
		string rest = word.substr(index+1);

		int results = 0;
		for( int i = 1; i < index; i++ ) {
			string newStr = word[i] + rest;
			results += find(newStr,aNode);
		}
		return results;
	}
	// only single letter
	else {
		size_t index = aNode->letters.find(word[0]);
		if( index == string::npos ) {
			return 0;
		}
		else {
			return find(word.substr(1),aNode->arr[index]);
		}
	}
}

void insert(string word) {
	node* aNode = first;

	for( int i = 0; i < word.length(); i++ ) {
		string letters = aNode->letters;
		size_t index = letters.find(word[i]);
		if( index == string::npos ) {
			aNode->letters = letters + word[i];
			index = aNode->letters.find(word[i]);	

			if( i != word.length()-1 ) {
				aNode->arr[index] = new node();
			}
		}
		aNode = aNode->arr[index];
	}
}