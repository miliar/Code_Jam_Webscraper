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

	 for (int test = 1; test <= T; ++test) {
		 int n;
		 scanf("%d", &n);
		 
		 vector <ii> V;
		 for (int i = 0; i < n; ++i) {
			ii a;
			scanf("%d%d", &a.first, &a.second);
			V.push_back(a);
		 }
		 sort(all(V));

		 int res = 0;
		 for (int i = 0; i < n; ++i) {
			 for (int j = i + 1; j < n; ++j) {
				 if (V[i].second > V[j].second) {
					++res;
				 }
			 }
		 }
		 printf ("Case #%d: %d\n", test, res);
	 }
	 return 0;
} 

