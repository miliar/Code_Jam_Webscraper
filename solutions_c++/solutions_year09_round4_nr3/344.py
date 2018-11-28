#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <queue> 
#include <bitset> 
#include <valarray> 
#include <complex> 
#include <iostream> 
#include <sstream> 
#include <cmath> 
#include <algorithm> 
#include <string> 
#include <cassert>
#include <ctime>
#include <float.h>
#include <string>
#include <cstring>

#ifdef _MSC_VER
#pragma comment(linker,"/STACK:20000000")
#endif

using namespace std;

// prewritten code

#define Size(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define RepV(i,v) for (int i=0;i<Size(v);++i)
#define All(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Abs(a) ((a)<0?-(a):(a))
#define VVI vector<vector<int> >
#define VI vector<int>
#define VVS vector<vector<string> >
#define VS vector<string>
#define ForEach(it,a) for (typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)
#define DBG(x) cout << #x <<" = "<< x << endl;
#define DBGA(x) {cout << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cout<<x[i]<<' '; cout<<endl;}
#define DBGV(x) {cout << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cout<<x[i]<<' '; cout<<endl;}

const string problem_name = "3";

int n, k, a[200][200], c[200][200];
int dp[1<<17], g[1<<17];

int go(int mask){
	int &res=dp[mask];
	if (res!=-1) return res;
	if (mask==0) return res=0;
	res = 1<<30;
	for (int j=mask; j>0; j=(j-1)&mask){
		if (g[j]) res=min(res,1+go(mask^j)); 
	}
	return res;
}

void solve_case(){
	Fill(c,0);
	scanf("%d%d",&n,&k);
	For(i,1,n) For(j,1,k) scanf("%d",&a[i][j]);
	For(i,1,n) For(j,i+1,n){
		bool cross=false;

		if (a[i][1] == a[j][1]) cross=true;
		For(t,2,k) if (a[i][t-1] > a[j][t-1] && a[i][t] <= a[j][t]) {
			cross=true;
			break;
		} else if (a[i][t-1] < a[j][t-1] && a[i][t] >= a[j][t]){
			cross=true;
			break;
		}

		if (cross) c[i][j]=c[j][i]=1;
	}

	Fill(g,0);
	g[0]=1;
	For(i,1,(1<<n)-1){
		For(j,0,n-1) if (i&(1<<j)) {
			bool ok=g[i^(1<<j)];
			For(t,j+1,n-1) if ((i&(1<<t)) && c[j+1][t+1]==1){ok=false; break;}
			g[i] = ok?1:0;
			break;
		}
	}

	Fill(dp,-1);
	printf("%d\n",go((1<<n)-1));
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int _t;
	scanf("%d\n",&_t);
	
	For(_z,1,_t){
		printf("Case #%d: ",_z);
		
		solve_case();
		
		fflush(stdout);
	}
	
	return 0;
}
