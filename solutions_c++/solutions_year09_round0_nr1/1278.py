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

const string problem_name = "1";

int l, d;
string w[10000];

void solve_case(){
	string s;
	getline(cin,s);
	int mask[30];
	Fill(mask,0);
	int cur=0;
	For(i,0,l-1) {
		if (s[cur]=='(') {
			++cur;
			while (s[cur] != ')') {
				mask[i]|=(1<<(s[cur]-'a'));
				++cur;
			}
			++cur;
		} else {
			mask[i] = (1<<(s[cur]-'a'));
			++cur;
		}
	}
	int res=0;
	For(i,1,d) {
		bool ok=true;
		For(j,0,l-1) if (!(mask[j]&(1<<(w[i][j]-'a')))) {ok=false; break;}
		if (ok) ++res;
	}
	printf("%d\n",res);
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int _t;
	scanf("%d%d%d\n",&l,&d,&_t);
	For(i,1,d) {
		getline(cin,w[i]);
	}
	
	For(_z,1,_t){
		printf("Case #%d: ",_z);
		
		solve_case();
		
		fflush(stdout);
	}
	
	return 0;
}
