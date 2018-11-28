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

void insert(string word);
int find(string word);

map<string,string> dictionary;
map<string,string>::iterator it;

int main()
{
	ifstream fin;
	fin.open ("example.txt");

	ofstream fout;
	fout.open ("welcome.txt");

	string wtcj = "welcome to code jam";

	//int N; // num test cases
	string str;
	getline(fin,str);
	int N = atoi(str.c_str());

	for( int n = 0; n < N; n++ ) {
		string word;
		getline(fin,word);
		size_t index;

		// trim word
		index = word.find('w');
		if( index != string::npos ) {
			word = word.substr(index);
		}

		index = word.rfind('m');
		if( index != string::npos ) {
			word = word.substr(0,index+1);
		}

		// word.length() x wtcj.length()
		int arr[500][19] = {0};

		// do first row of array
		for( size_t i = word.find('w'); i != string::npos && i < word.length(); i++ ) {
			if( word[i] == 'w' ) {
				if( i == 0 ) {
					arr[i][0] = 1;
				}
				else {
					arr[i][0] = arr[i-1][0]+1;
				}
			}
			else {
				arr[i][0] = arr[i-1][0];
			}
		}

		for( int i = 1; i < wtcj.length(); i++ ) {
			char ch = wtcj[i];
			size_t index = word.find(ch);
			if( index == string::npos ) {
				break;
			}
			for( int j = index; j < word.length(); j++ ) {
				if( word[j] == ch ) {
					arr[j][i] = (arr[j-1][i] + arr[j][i-1]) % 10000;
				}
				else {
					arr[j][i] = arr[j-1][i];
				}
			}
		}

		int result = arr[word.length()-1][wtcj.length()-1];

		stringstream strStream;
		strStream << result;
		string answer = strStream.str();
		if( result < 10 ) {
			answer = "000" + answer;
		}
		else if( result < 100 ) {
			answer = "00" + answer;
		}
		else if( result < 1000 ) {
			answer = "0" + answer;
		}

		cout << "Case #" << n+1 << ": " << answer << endl;
		fout << "Case #" << n+1 << ": " << answer << endl;
	}

	return 0;
}