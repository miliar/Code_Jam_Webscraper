#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GI64 ({int64 t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GS ({string s;cin>>s;s;})
#define f(i,a,b) for(int i=a;i<b;i++)
#define rf(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9

typedef long long int64;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

#define is istringstream
#define os ostringstream

//char ch;
const int dx[]={-1,0,0,1},dy[]={0,-1,1,0};
int m,n;
int global;
int grid[105][105],ans[105][105];

bool ok(int i,int j){return(i>=0 && j>=0 && i<m && j<n);}

void go(int i,int j){
	if(ans[i][j]>=0)return;
	int nxti=i,nxtj=j,minval=grid[i][j];
	f(k,0,4)if(ok(i+dx[k],j+dy[k]))if(grid[i+dx[k]][j+dy[k]]<minval)minval=grid[i+dx[k]][j+dy[k]],nxti=i+dx[k],nxtj=j+dy[k];
	if(nxti==i && nxtj==j){ans[i][j]=(global++);return;}
	else{
		go(nxti,nxtj);
		ans[i][j]=ans[nxti][nxtj];
		return;
	}
}

int main(){
	int t=GI;
	int cnt=0;
	while(t--){
		cnt++;
		global=0;
		SET(ans,-1);
		m=GI,n=GI;	
		f(i,0,m)f(j,0,n)grid[i][j]=GI;
		f(i,0,m)f(j,0,n)if(ans[i][j]==-1)go(i,j);
		cout<<"Case #"<<cnt<<":\n";
		f(i,0,m){f(j,0,n)cout<<char(ans[i][j]+'a')<<" ";cout<<endl;}		
	}
	return 0;	
}
