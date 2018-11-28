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
#define PB push_back
#define MP make_pair

const string problem_name = "1";

int name[10000], a[10000], b[10000], cnt, clr[10005][10];

map<string,int> h;

int id(string s){
	if (h.find(s) != h.end()) return h[s];
	return h[s]=++cnt;
}

int bits(int m){
	if (m==0) return 0; else return bits(m/2)+(m%2);
}

void solve_case(){
	int n;
	h.clear();
	cnt=0;
	
	scanf("%d\n",&n);
	For(i,1,n){
		string ss;
		cin >> ss >> a[i] >> b[i];
		name[i] = id(ss);
	}
	int res=1000000000;
	For(mask,0,(1<<n)-1){
		int use[100];
		Fill(use,0);
		int y=0;
		For(i,0,n-1) if (mask&(1<<i)) {
			if (!use[name[i+1]]) ++y;
			use[name[i+1]]=1;
		}
		if (y>3) continue;
		bool good=true;
		Fill(clr,0);
		For(i,0,n-1) if (mask&(1<<i)){
			For(j,a[i+1],b[i+1]) {
				bool ok=false;
				For(k,0,clr[j][0]) if (clr[j][k] == name[i+1]) {ok=true; break;}
				if (!ok) {
					++clr[j][0];
				}
			}
		}
fin:
		For(i,1,10000) if (clr[i][0]<=0 || clr[i][0]>3) good=false;
		if (good) {
			res=Min(res,bits(mask));
		}
	}

	if (res==1000000000) cout << "IMPOSSIBLE" << endl;
	else cout << res << endl;
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
