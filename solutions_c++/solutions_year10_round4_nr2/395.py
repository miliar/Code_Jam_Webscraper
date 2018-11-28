#include <algorithm>  
#include <iostream>  
#include <cstdio>  
#include <sstream>  
#include <ctype.h>  
#include <cstring>  
#include <string>  
#include <cmath>  
#include <queue>  
#include <vector>  
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

const i64 inf = 1LL<<60;

vi M;
vvi V;
int P;

int tree[2000];
int pt;

bool isNeed(int level, int h, int num, int root) {
	if (level == P) {
		if (P - M[root - (1<<P)] - num > 0)
			return true;
		return false;
	}
	bool res = isNeed(level + 1, h, num, root + root);
	res |= isNeed(level + 1, h, num, root + root + 1);
	return res;
}

i64 dfs (int level, int num, int root) {
	if (level == P) {
		if (M[root - (1<<P)] + num < P) {
			return inf;
		}
		return 0;
	}
	bool need = isNeed(level, level, num, root);

	if (!need) return 0;
	i64 res = min(
		dfs (level + 1, num + 1, 2 * root) + 
		dfs (level + 1, num + 1, 2 * root + 1) + tree[root],

		dfs (level + 1, num, 2 * root) + 
		dfs (level + 1, num, 2 * root + 1)
		);
	if (res > inf) res = inf;
	return res;
}

 int main() {

	 freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);

	 int Tests;
	 scanf("%d", &Tests);

	 for (int Test = 1; Test <= Tests; ++Test) {
		 scanf("%d", &P);
		 int size = 1 << P;

		 M.clear();
		 M.resize(size);
		 for (int i = 0; i < size; ++i)
			 scanf("%d", &M[i]);
		 size /= 2;

		 V.clear();
		 
		 while (size >= 1) {
			 vi t(size);
			 for (int i = 0; i < size; ++i)
				 scanf("%d", &t[i]);

			 V.pb(t);
			 size /= 2;
		 }
		 memset (tree, 0, sizeof(tree));

		 pt = 1;
		 for (int i = V.size() - 1; i >= 0; --i) {
			 for (int j = 0; j < V[i].size(); ++j) {
				tree[pt++] = V[i][j];
			 }
		 }

		 i64 res = dfs (0,0, 1);

		 printf ("Case #%d: %I64d\n", Test, res);
	 }

	 return 0;
} 

