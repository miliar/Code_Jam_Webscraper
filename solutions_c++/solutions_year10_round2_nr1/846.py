#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i ++) {
		int N, M;
		int ans = 0;
		map < string, int > db;
		map <string, int >::iterator p;
		scanf("%d %d", &N, &M);

		db.insert(make_pair("", 1));
		db.insert(make_pair("/", 1));
		for (int j = 0; j < N; j ++) {
			string str;
			cin >> str;
			db.insert(make_pair(str, 1));
		}
		
		for (int j = 0; j < M; j ++) {
			string str;
			cin >> str;

			int len = str.length();
			string tmp = "";
			for (int i = 0; i < len; i ++) {
				if (str[i] != '/')
					tmp += str[i];
				else {
					p=db.find(tmp);
					if (p == db.end()) {
						ans ++;
						db.insert(make_pair(tmp, 1));
					}
				
					tmp += str[i];
				}
			}
			
			p=db.find(tmp);
			if (p == db.end()) {
				ans ++;
				db.insert(make_pair(tmp, 1));
			}
		
		}

		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}