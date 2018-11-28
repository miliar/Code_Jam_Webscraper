#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/
const int maxn=110;
const int MOD=10007;
int a[maxn][maxn],n,m,r,t;
bool used[maxn][maxn];
int main(){
	ifstream cin("input4.txt");
	cin >> t;
	for(int cas=1;t--;cas++){
		cin >> n >> m >> r;
		CLR(used,0);
		For(i,0,r){
			int x,y;
			cin >> x>> y; 
			x--,y--;
			used[x][y]=1;
		}
		CLR(a,0);
		a[0][0]=1;
		For(i,0,n)
			For(j,0,m){
				if (!(i|j)) continue;
				if (used[i][j]) continue;
				if (i>=2 && j>=1) a[i][j]+=a[i-2][j-1];
				if (i>=1 && j>=2) a[i][j]+=a[i-1][j-2];
				a[i][j]%=MOD;			
			}
		printf("Case #%d: %d\n",cas,a[n-1][m-1]);
	}
	return 0;
}