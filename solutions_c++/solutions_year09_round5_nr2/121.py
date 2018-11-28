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

const string problem_name = "B-small-attempt1";
const int M = 10009;

int n, k, taken, t[1000], cnt[26], res[1000];
char s[1000], w[1000][1000];

void go(int p, int need){
	if (need == 0){
		Fill(cnt,0);
		For(i,1,taken){
			int l=strlen(w[t[i]]);
			For(j,0,l-1) ++cnt[w[t[i]][j]-'a'];
		}

		int l=strlen(s), cur=1;

		For(i,0,l-1) if (s[i]=='+') {
			res[taken] = (res[taken]+cur)%M;
			cur=1;
		} else {
			cur = cur * cnt[s[i]-'a'];
		}

		return;
	}
	if (p > n) return;
	go(p+1,need);

	t[++taken] = p;
	go(1,need-1);
	--taken;
}

void solve_case(){
	Fill(s,0);
	scanf("%s %d\n",s,&k);
	s[strlen(s)]='+';
	scanf("%d\n",&n);
	For(i,1,n) gets(w[i]);
	Fill(res,0);
	For(i,1,k){
		taken=0;
		go(1, i);
		printf(" %d",res[i]);
	}
	printf("\n");
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int _t;
	scanf("%d\n",&_t);
	
	For(_z,1,_t){
		printf("Case #%d:",_z);
		
		solve_case();
		
		fflush(stdout);
	}
	
	return 0;
}
