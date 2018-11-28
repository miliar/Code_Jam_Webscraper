/*
 * B.cpp
 *
 *  Created on: 7 May 2011
 *      Author: Admin
 */
#include<cstdio>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<string>
#define min(A,B) ((A)<(B)?(A):(B))
#define max(A,B) ((A)<(B)?(B):(A))
#define abs(a) ((a)<0?(a)*-1:(a))

using namespace std;

int main() {
		freopen("B-large.in", "rt", stdin);
		freopen("a.txt", "wt", stdout);

	int t, n;
	scanf("%d", &t);
	char str[4];
	for (int K = 1; K <= t; ++K) {
		scanf("%d", &n);
		map<string, string> base;
		map<string, string>::iterator it;
		map<char, set<char> > opp;
		map<char, set<char> >::iterator it2;
		while (n--) {
			scanf(" %s", str);
			base[string(str, str + 2)] = str[2];
			swap(str[0], str[1]);
			base[string(str, str + 2)] = str[2];
		}
		scanf("%d", &n);
		while (n--) {
			scanf(" %s", str);
			opp[str[0]].insert(str[1]);
			opp[str[1]].insert(str[0]);
		}
		scanf("%d", &n);
		string s;
		while (n--) {
			scanf(" %c", &str[0]);
			s += str[0];
			if (s.size() >= 2) {
				it = base.find(s.substr(-2 + s.size()));
				if (it != base.end()) {
					s = s.substr(0, -2 + s.size()) + it->second;
				}
			}
			for (size_t i = 0; i < s.size(); ++i) {
				for (size_t j = 0; j < s.size(); ++j) {
					if (i != j) {
						it2 = opp.find(s[i]);
						if (it2->second.find(s[j]) != it2->second.end())
							s.clear();
					}
				}
			}
		}
		printf("Case #%d: [", K);
		for (size_t i = 0; i < s.size(); ++i)
			printf(i ? ", " : ""), printf("%c", s[i]);
		printf("]\n");
	}

	return 0;
}

