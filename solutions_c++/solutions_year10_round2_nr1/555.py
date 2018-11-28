#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define PROBLEM_NAME "a"

set<string> names;

int main () {
	freopen (PROBLEM_NAME ".in", "rt" ,stdin);
	freopen (PROBLEM_NAME ".out", "wt" ,stdout);
	int T; scanf ("%d", &T);
	char s[10000];
	for (int t = 1; t <= T; t++) {
		int n, m;
		scanf ("%d%d\n", &n, &m);
		names.clear();
		names.insert ("/");
		names.insert("");
		for (int i = 0; i < n; i++) {
			scanf ("%s\n", s);
			int len = strlen(s);
			string res = "";
			for (int j = 0; j < len; j++) {
				if (s[j] == '/') {
					names.insert(res);
					names.insert(res+"/");					
				}
				res += s[j];
			}
			names.insert(res);
			names.insert(res+"/");
		}
		
		int kol = 0;
		
		for (int i = 0; i < m; i++) {
			scanf ("%s", s);
			int len = strlen(s);
			string res = "";
			for (int j = 0; j < len; j++) {
//				cerr << s[j];
				if (s[j] == '/') {
					if (names.find(res) == names.end()) {
//						printf (" %d", j);
						kol++;
						names.insert(res);
						names.insert(res+"/");
					}
				}
				res += s[j];
			}
			if (names.find(res) == names.end()) {
//				printf (" aaa");
				kol++;
				names.insert(res);
				names.insert(res+"/");
			}
//			cerr << "\n";
		}
		
		printf ("Case #%d: %d\n", t, kol);
	}
	return 0;
}
