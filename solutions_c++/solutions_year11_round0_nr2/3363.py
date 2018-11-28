/*
 * B.cpp
 *
 *  Created on: May 7, 2011
 *      Author: yassery
 */

#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

vector<char> out;
map<pair<char, char> , char> C;
set<pair<char, char> > Op;

void combine(char c1, char c2, char c3) {
	C[make_pair(c1, c2)] = c3;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("test.txt", "wt", stdout);
#endif

	int TC;
	char c1, c2, c3;
	string q;
	int n;

	cin >> TC;

	for (int tt = 0; tt < TC; tt++) {
		out.clear();
		C.clear();
		Op.clear();

		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> c1 >> c2 >> c3;
			combine(min(c1, c2), max(c1, c2), c3);
		}
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> c1 >> c2;
			Op.insert(make_pair(min(c1, c2), max(c1, c2)));
		}
		cin >> n;
		cin >> q;

		for (int i = 0; i < n; i++) {
			if (out.size()) {
				c1 = out.back();
				c2 = q[i];
				if (c2 < c1)
					swap(c1, c2);
				if (C.find(make_pair(c1, c2)) != C.end()) {
					out[out.size() - 1] = C[make_pair(c1, c2)];
				}else{
					out.push_back(q[i]);
				}
			}else{
				out.push_back(q[i]);
			}

			for (int i = 0; i <(int) out.size(); i++) {
				c1 = min(out[i], out.back());
				c2 = max(out[i], out.back());
				if (Op.count(make_pair(c1, c2))) {
					out.clear();
					break;
				}
			}

		}
		printf("Case #%d: [",tt+1);
		for(int i=0;i<out.size();i++){
			if(i)
				printf(", ");
			printf("%c",out[i]);
		}
		printf("]\n");
	}

	return 0;
}
