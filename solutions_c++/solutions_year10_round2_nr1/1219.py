#include <algorithm>  
#include <iostream>  
#include <cstring>  
#include <ctype.h>  
#include <sstream>  
#include <cstdio>  
#include <string>
#include <vector>  
#include <cmath>  
#include <queue>  
#include <map>  
#include <set>  

using namespace std;  

typedef long long i64;
typedef unsigned long long u64;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;

#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(),(a).end()
#define mset(a,byteval) memset(a, byteval, sizeof(a))
#define ff(i,b) for(i=0;i<(b);++i)
#define fr(i,a,b) for(i=(a);i<(b);++i)

 int main() {

	 int T;

	 freopen("A-large.in", "r", stdin); 
	 freopen("A-large.out", "w", stdout);

	 scanf("%d", &T);

	 for (int t = 1; t <= T; ++t) {
		int n, m;
		scanf("%d%d", &n, &m);

		set <string> si;

		char s[120];

		for (int i = 0; i < n; ++i) {
			scanf("%s", s);
			int len = strlen(s);
			string ss = s;
			for (int j = 0; j < len; ++j) {
				if (s[j] == '/' && j) {
					string str = ss.substr(0, j);
					si.insert(str);
				}
				si.insert(ss);
			}
		}
		int res = si.size();
		for (int i = 0; i < m; ++i) {
			scanf("%s", s);
			int len = strlen(s);
			string ss = s;

			for (int j = 0; j < len; ++j) {
				if (s[j] == '/' && j) {
					string str = ss.substr(0, j);
					si.insert(str);
				}
				si.insert(ss);
			}
		}
		printf ("Case #%d: %d\n", t, si.size() - res);
	 }


	 return 0;
} 

