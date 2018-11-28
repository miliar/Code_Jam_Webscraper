/*
 * gcj.cpp
 *
 *  Created on: 2011-5-7
 *      Author: kokopelli
 */

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

class node{
public:
	char a, b;
	node(char _a = 0, char _b = 0){
		a = _a; b = _b;
		if (a > b){
			char t = a;
			a = b;
			b = t;
		}
	}
	node(const node& m){
		a = m.a;
		b = m.b;
	}
	bool operator==(const node& m){
		return a == m.a && b== m.b;
	}
};

	bool operator<(const node& lm, const node& rm){
		if (lm.a != rm.a) return lm.a < rm.a;
		return lm.b < rm.b;
	}

map<node, char> comb;
set<node> oppose;
char res[105];

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++){
		int C; scanf("%d", &C);
		int i, j;
		comb.clear();
		for (i = 1; i <= C; i++){
			string s; cin >> s;
			comb.insert(pair<node, char>(node(s[0], s[1]), s[2]));
		}
		int D; scanf("%d", &D);
		oppose.clear();
		for (i = 1; i <= D; i++){
			string s; cin >> s;
			oppose.insert(node(s[0], s[1]));
		}
		int N; scanf("%d", &N);
		string s; cin >> s;
		printf("Case #%d: [", cas);
		for(i = 0, j = 0; i < N; i++){
			res[j] = s[i];
			char flag = false;
			while(1){
				if (j > 0 && comb.find(node( res[j], res[j-1] )) != comb.end()){
					res[j - 1] = comb[node(res[j], res[j-1])];
					j--;
					flag = true;
				}else
					break;
			}
			for (int k = 0; !flag && k < j; k++)
				if (oppose.find(node(res[k], res[j])) != oppose.end())
					j = -1;
			j++;
		}
		for (i = 0; i < j; i++)
			printf("%s%c", (i > 0 ? ", " : ""), res[i]);
		printf("]\n");
	}
	return 0;
}
