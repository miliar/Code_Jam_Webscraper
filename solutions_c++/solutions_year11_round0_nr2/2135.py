/*
 * B.cpp
 *
 *  Created on: May 7, 2011
 *      Author: loai
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <map>
#include <string>
#include <stdio.h>
#include <string.h>
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define NCHAR 26
using namespace std;

map<char, int> hash;
int combine[NCHAR][NCHAR];
bool opposite[NCHAR][NCHAR];
int v[NCHAR];

void preProcess() {
	REP(i,NCHAR)
		REP(j,NCHAR) {
			combine[i][j] = -1;
			opposite[i][j] = false;
		}
	REP(i,NCHAR)
		v[i] = 0;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int K;
	scanf("%d\n", &K);
	for (int test = 1; test <= K; test++) {
		preProcess();
		int C;
		scanf("%d ", &C);
		REP(i,C) {
			char s[8];
			scanf("%s ", s);
			combine[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			combine[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		int D;
		scanf("%d ", &D);
		REP(i,D) {
			char s[8];
			scanf("%s ", s);
			opposite[s[0] - 'A'][s[1] - 'A'] = true;
			opposite[s[1] - 'A'][s[0] - 'A'] = true;
		}
		int N;
		scanf("%d ", &N);
		char c;
		scanf("%c", &c);
		int x = c - 'A';
		vector<int> ret;
		ret.push_back(x);
		v[x]++;
		REP(i,N-1) {
			scanf("%c", &c);
			x = c - 'A';
			//	printf("in loop %d \n",i);
			if (ret.empty()) {
				ret.push_back(x);
				v[x]++;
				continue;
			}
			int prev = ret[(int) ret.size() - 1];
			if (combine[x][prev] != -1) {
				ret.pop_back();
				v[prev]--;
				ret.push_back(combine[x][prev]);
			} else {
				bool cleared=false;
				REP(j,NCHAR)
					if (opposite[x][j] && v[j]) {
						ret.clear();
						//	printf("test %d size is %d\n", test, (int) ret.size());
						memset(v, 0, sizeof(v));
						cleared=true;
						break;
					}
				if(cleared)
					continue;
				ret.push_back(x);
				v[x]++;
			}

		}
		//	printf("vector size is %d\n",ret.size());
		string res = "[";
		int size = (int) ret.size();
		REP(i,size-1) {
			c = (char) (ret[i] + 'A');
			res += c;
			res += ", ";
		}
		if (!ret.empty()) {
			c = (char) (ret[size - 1] + 'A');
			res += c;
		}
		res += "]";
		printf("Case #%d: %s\n", test, res.c_str());
	}
}

