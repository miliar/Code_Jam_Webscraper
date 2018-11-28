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

const string problem_name = "3";

int rows, cols, dp[20][1<<11];
char s[20][20];

bool good(int mask){
	int last=0;
	while (mask){
		if (last && (mask%2)) return false;
		last=(mask%2);
		mask/=2;
	}
	return true;
}

int bits(int mask){
	if (!mask)return 0;
	return bits(mask/2) + (mask%2);
}

int forb(int mask){
	int res=0, z=0;
	while (mask){
		if (mask%2) {
			if (z>0) res|=(1<<(z-1));
			if (z<cols-1) res|=(1<<(z+1));
		}
		++z;
		mask/=2;
	}
	return res;
}

int go(int r, int mask){
	int &res = dp[r][mask];
	if (res!=-1) return res;

	if (r == rows) return res=0;
	res = 0;
	For(i,0,cols-1) if (s[r][i]=='x') mask|=(1<<i);
	For(i,0,(1<<cols)-1) if (good(i) && ((mask&i) == 0)) {
		res = Max(res, go(r+1,forb(i)) + bits(i) );
	}

	return res;
}

void solve_case(){
	
	scanf("%d%d\n",&rows,&cols);
	For(i,0,rows-1) gets(s[i]);
	
	Fill(dp,-1);
	printf("%d\n",go(0,0));
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
