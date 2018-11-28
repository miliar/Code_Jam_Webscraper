#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
typedef long long ll;
int N;
#define M 11000
int tipo[M], CH[M];
int dp[2][M];
bool visited[2][M];
#define MX 12200
int back(int V, int ind){
	if( ind >= (N+1)/2 ){
		if( V ==CH[ind] ) return 0;
		return MX;
	}
	if( visited[V][ind] ) return dp[V][ind];
	visited[V][ind] = true;
	int & res  = dp[V][ind]; res = MX;
	if( !tipo[ind] ){// es un OR...
		if( V ){
			res = min( res, back(1,2*ind) + back(0,2*ind+1));
			res = min( res, back(0,2*ind) + back(1,2*ind+1));
			res = min( res, back(1,2*ind) + back(1,2*ind+1));
		}else{
			res = min( res, back(0,2*ind) + back(0,2*ind+1));
		}
	}else{
		if( !V ){
			res = min( res, back(1,2*ind) + back(0,2*ind+1));
			res = min( res, back(0,2*ind) + back(1,2*ind+1));
			res = min( res, back(0,2*ind) + back(0,2*ind+1));
		}else{
			res = min( res, back(1,2*ind) + back(1,2*ind+1));
		}
	}
// 	}else{
	if( CH[ind] ){
		if( !tipo[ind] ){// es un OR...
			// lo transformo en AND
			if( !V ){
				res = min( res, 1+back(1,2*ind) + back(0,2*ind+1));
				res = min( res, 1+back(0,2*ind) + back(1,2*ind+1));
				res = min( res, 1+back(0,2*ind) + back(0,2*ind+1));
			}else{
				res = min( res, 1+back(1,2*ind) + back(1,2*ind+1));
			}
		}else{
			
			if( V ){
				res = min( res, 1+back(1,2*ind) + back(0,2*ind+1));
				res = min( res, 1+back(0,2*ind) + back(1,2*ind+1));
				res = min( res, 1+back(1,2*ind) + back(1,2*ind+1));
			}else{
				res = min( res, 1+back(0,2*ind) + back(0,2*ind+1));
			}
		}
	}
	return res;
}


int main(){
		int V;
	int i,j ,k;
	int casos;
	scanf("%i", &casos);
	for(int h = 0 ;h < casos ; h ++ ){
		scanf("%i %i", &N, &V);
		for(i=1;i<=(N-1)/2;i++){
			scanf("%i %i", &tipo[i], &CH[i]);
		}
		for(i=(N+1)/2;i<=N;i++)scanf("%i", &CH[i]);
		memset(dp, -1, sizeof(dp));
		memset(visited, false, sizeof(visited));
		int r = back(V, 1);
		printf("Case #%i: ", h+1);
		if( r >=  MX ) printf("IMPOSSIBLE\n");
		else printf("%i\n", r);
	}
	return 0;
}
