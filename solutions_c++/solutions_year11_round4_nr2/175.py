#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define FOR(it,A) for( typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define impr(A) for( typeof A.begin() chen = A.begin(); chen !=A.end(); chen++ ) cout<<*chen<<" "; cout<<endl
#define ll long long
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define poner push_back
#define eps (1e-9)
#define sqr(x) (x)*(x)
using namespace std;

ll a[505][505], b[505][505], c[505][505];
ll ST[505][505], SI[505][505], SJ[505][505];
string A[505];
int T, caso = 1;
int R,C,D;

ll sumaT(int x,int y,int k){
	return ST[x][y] + ST[x-k][y-k] - ST[x-k][y] - ST[x][y-k]
	- a[x][y] - a[x-k+1][y-k+1] - a[x-k+1][y] - a[x][y-k+1];
}
ll sumaI(int x,int y,int k){
	return SI[x][y] + SI[x-k][y-k] - SI[x-k][y] - SI[x][y-k]
	- b[x][y] - b[x-k+1][y-k+1] - b[x-k+1][y] - b[x][y-k+1];
}
ll sumaJ(int x,int y,int k){
	return SJ[x][y] + SJ[x-k][y-k] - SJ[x-k][y] - SJ[x][y-k]
	- c[x][y] - c[x-k+1][y-k+1] - c[x-k+1][y] - c[x][y-k+1];
}

int solve(){
	fd(k,505,3){
		f(i,k,R+1)f(j,k,C+1){
			if( sumaT(i,j,k)*(i-k+1+i)== 2*sumaI(i,j,k) &&
				 sumaT(i,j,k)*(j-k+1+j)== 2*sumaJ(i,j,k) ){
						return k;
			}
		}
	}
	return 0;
}

int main()
{
	cin >> T;
	while( T-- ){
		cin >> R >> C >> D;
		f(i,0,R) cin >> A[i];
		clr(a,0); clr(b,0); clr(c,0);
		f(i,0,R)f(j,0,C) a[i+1][j+1] = A[i][j]-'0';
		f(i,1,R+1)f(j,1,C+1) b[i][j] = a[i][j] * i, c[i][j] = a[i][j]*j;
		
		f(i,0,R+1)f(j,0,C+1){
			ll &res = ST[i][j] = a[i][j];
			if( i ) res += ST[i-1][j];
			if( j ) res += ST[i][j-1];
			if( i&&j ) res-= ST[i-1][j-1];
		}
		f(i,0,R+1)f(j,0,C+1){
			ll &res = SI[i][j] = b[i][j];
			if( i ) res += SI[i-1][j];
			if( j ) res += SI[i][j-1];
			if( i&&j ) res-= SI[i-1][j-1];
		}
		f(i,0,R+1)f(j,0,C+1){
			ll &res = SJ[i][j] = c[i][j];
			if( i ) res += SJ[i-1][j];
			if( j ) res += SJ[i][j-1];
			if( i&&j ) res-= SJ[i-1][j-1];
		}
//		cout << a[3][3] <<endl;
//		cout << sumaT(3,3,3) << endl;
		printf( "Case #%d: ",caso++ );
		int res = solve();
		if( res ) cout << res << endl;
		else puts( "IMPOSSIBLE" );
	}
}
