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

const string problem_name = "A-large";

map<string, int> h;

int dp[1100][110];

const int INF = 1000000;

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int t;
	scanf("%d",&t);
	
	Fill(dp,0);
	
	For(z,1,t){
		int n;
		h.clear();
		scanf("%d\n",&n);
		For(i,1,n) {
			string s;
			getline(cin,s);
			h[s] = i;
		}
		int m, a[1100];
		scanf("%d\n",&m);
		
		For(i,1,m) {
			string s;
			getline(cin,s);
			a[i] = h[s];
		}
		
		For(i,1,m) For(j,1,n) {
			if (a[i]==j) dp[i][j]=INF;
			else {
				dp[i][j]=INF;
				For(k,1,n) dp[i][j] = min (dp[i][j], dp[i-1][k] + (k==j?0:1));
			}
		}
		
		int res = INF;
		For(i,1,n) res=min(res,dp[m][i]);
		
		printf("Case #%d: %d\n",z,res);
	} 
	
	return 0;
}
