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

const string problem_name = "2";

int n, m, a;

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int t;
	scanf("%d\n",&t);
	
	For(z,1,t){
		printf("Case #%d: ",z);
		
		scanf("%d%d%d",&n,&m,&a);
		
		if ( n*m < a/2 ) {
			printf("IMPOSSIBLE\n");
			continue;
		}

		int x1=0, x2, x3, y1=0, y2, y3;
		bool ok=false;

		For(i,0,n) For(j,0,m) if (i+j>0) {
			x3 = i;
			y2 = j;
			int t = a + x3*y2;
			For(i,1,n) if (t%i == 0){
				x2 = i; y3 = t/i;
				if ( (y3<=m) && (x2!=x1||y2!=y1) && (x2!=x3||y2!=y3) && (x3!=x1||y3!=y1) ){
					ok=true;
					goto f;
				}
			}
		}
f:

		if (ok) {
			printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
		} else {
			printf("IMPOSSIBLE\n");
		}

		fflush(stdout);
	}
	
	return 0;
}
