#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int patterns[10000*15][255];
int last = 1;
int L,D,N;

void addword(string& s, int id, int cur)
{
	if (cur == L)
		return;
	if (patterns[id][s[cur]])
		addword(s, patterns[id][s[cur]], cur+1);
	else 
		addword(s, patterns[id][s[cur]] = last++, cur+1);
}

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("file.out");
	cin >> L >> D >> N;
	for (int i = 0; i < D; ++i) {
		string tmp;
		cin >> tmp;
		addword(tmp, 0, 0);
	}

	for (int i = 1; i <= N; ++i) {
		vector <int> curids(1);
		for (int j = 0; j < L; ++j){
			vector <int> newids;
			char c;
			cin >> c;
			if (c == '(') {
				while (cin >> c, c != ')') {
					for (int k = 0; k < curids.size(); ++k) {
						if (patterns[curids[k]][c]) {
							newids.push_back(patterns[curids[k]][c]);
						}
					}
				}
			}
			else {
				for (int k = 0; k < curids.size(); ++k) {
					if (patterns[curids[k]][c]) {
						newids.push_back(patterns[curids[k]][c]);
					}
				}
			}
			curids = newids;
		}
		cout << "Case #" << i << ": " << curids.size() << endl;
	}

	return 0;
}
