
#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include <ext/hash_map>
#include<cassert>
#include<set>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 100000000
//__gnu_cxx::hash_map< int ,int> best;
typedef long long ll;
using namespace std;
#define maxn 105
int dp[maxn][maxn];
bool bad[maxn][maxn];
int H,W,R;
#define mod 10007
int tx[]= { -2, -1 };
int ty[]= { -1, -2 };

int solve( int y ,int x){
	if( y<= 0 || x <= 0 ) return 0;
	if( bad[y][x]) return 0;
	if( y==1 && x== 1 ) return 1;
	if( dp[y][x]!=-1 ) return dp[y][x];
	int w= 0;
	fup(i,0,1){
		w+= solve(y+ty[i],x+tx[i]);
		w%= mod;
	}
	dp[y][x]=w;
	return w;
}

int main(){
int cas;cin>>cas;
fup(vv,1,cas){
	memset(dp,-1,sizeof(dp));
	cin>>H>>W>>R;
	fup(i,0,100) fup(j,0,100) bad[i][j]=false;

	fup(i,1,R){
		int y,x;;
		cin>>y>>x;
		bad[y][x]=true;
	}
	cout<<"Case #"<<vv<<": ";
	cout << solve(H,W) <<endl;
}


return 0;
}
