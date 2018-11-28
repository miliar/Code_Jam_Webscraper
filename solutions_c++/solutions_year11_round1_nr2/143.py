#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
using namespace std;

bool stillin[10000];
int disagreeindex[10000];
int totalcount[26];
int curcount[26];

string solve(vector<string>& words, string& alph) {
	int N = words.size();
	map<char,int> charmap;
	for(int i = 0; i<26; i++) {
		charmap[alph[i]] = i;
	}
	int lost = -1;
	string best;
	for(int i = 0; i<N; i++) {
		string& word = words[i];
		int L = word.length();
//cout << word << endl;

		memset(totalcount, 0, sizeof(totalcount));
		memset(curcount, 0, sizeof(curcount));
		
		for(int j = 0; j<L; j++) {
			curcount[charmap[word[j]]]++;
		}

		int numin = 0;
		for(int j = 0; j<N; j++) {
			string& oword = words[j];
			int earliest = 25;
			if(i==j || oword.length() != L) {
				stillin[j] = false;
				continue;
			}
			stillin[j] = true;
			numin++;
			for(int k = 0; k<L; k++) {
				if(word[k] != oword[k]) {
					earliest = min(charmap[word[k]], earliest);
					earliest = min(charmap[oword[k]], earliest);
				}
				totalcount[charmap[oword[k]]]++;
			}
			disagreeindex[j] = earliest;
//		cout << oword << " " << earliest << endl;
		}
		int points = 0;
		for(int j = 0; j<26 && numin != 0; j++) {
	//cout << j << endl;
			if(totalcount[j] != 0 && curcount[j] == 0) {
				points++;
			}
			for(int k = 0; k<N; k++) {
				if(stillin[k] && j>= disagreeindex[k]) {
					stillin[k] = false;
					numin--;
					for(int l = 0; l<L; l++) {
						totalcount[charmap[words[k][l]]]--;
					}
				}
			}
		}
//	cout << points << " " << word << endl;
		if(points>lost) {
			lost = points;
			best = word;
		}
	}
	return best;
}

int main() {
	int TESTS;
	cin >> TESTS;
	for(int TEST = 1; TEST<=TESTS; TEST++) {
		int N, M;
		cin >> N >> M;
		vector<string> words;
		for(int i = 0; i<N; i++) {
			string word;
			cin >> word;
			words.push_back(word);
		}
		cout << "Case #" << TEST << ":";
		for(int i = 0; i<M; i++) {
			string alph;
			cin >> alph;
			cout << " " << solve(words, alph);
		}
		cout << endl;
	}
}
