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

const string problem_name = "1";
const int INF = 1000000;

int m, v, g[11000], c[11000], l[11000];

int go(int u, int need){
	if (2*u+1 > m) {
		if (need == l[u]) return 0;
		return INF;
	}
	if (g[u] == 1){ // AND
		if (need == 0){
			int v1 = go(2*u,0);
			int v2 = go(2*u+1,0);
			if (c[u])
				return Min(Min(v1,v2), v1+v2+1 );
			else
				return Min(v1,v2);
		} else {
			if (c[u])
				return Min(go(2*u,1) + go(2*u+1,1), Min(go(2*u,1),go(2*u+1,1))+1  );
			else
				return go(2*u,1) + go(2*u+1,1);
		}
	} else {
		if (need == 0){
			if (c[u])
				return Min(go(2*u,0) + go(2*u+1,0),  Min(go(2*u,0),go(2*u+1,0))+1 );
			else
				return go(2*u,0) + go(2*u+1,0);
		} else {
			int v1 = go(2*u,1);
			int v2 = go(2*u+1,1);
			if (c[u])
				return Min(Min(v1,v2),  go(2*u,1)+go(2*u+1,1)+1 );
			else
				return Min(v1,v2);
		}
	}
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int t;
	scanf("%d\n",&t);
	
	For(z,1,t){
		printf("Case #%d: ",z);
		
		scanf("%d%d",&m,&v);
		
		For(i,1,(m-1)/2) {
			scanf("%d%d",&g[i],&c[i]);
		}
		
		For(i,(m-1)/2+1,m) scanf("%d",&l[i]);

		int res = go(1,v);

		if (res >= INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",res);

		fflush(stdout);
	}
	
	return 0;
}
