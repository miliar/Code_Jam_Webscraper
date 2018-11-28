// Tim  defines
#include <vector> 
#include <queue> 
#include <set>
#include <map> 

#include <numeric>
#include <algorithm> 
#include <string.h> 

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 

using namespace std;
//#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define Rep(i,n) for (int i=0;i<(n);++i)
#define RepV(i,v) for (int i=0;i<sz(v);++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
typedef long long LL;
typedef pair <int,int> PI;
typedef pair<double, double> PD;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;
const int oo = (1<<30);
const double eps = 1e-10;
const double INF = 1e10;

int n;
string pattern = " welcome to code jam";
char s[600];
int dp[600];


int main() { 
	freopen("CC.in","rt",stdin);
	freopen("CC.out","wt",stdout);
	scanf("%d\n",&n);
	For(q,1,n){
		gets(s);
		Fill(dp,0);
		dp[0] = 1;
		int l = strlen(s);
		Rep(i,l){
			For(j,1,19){
				if (s[i] == pattern[j])
					dp[j] = (dp[j]+dp[j-1])%10000;
			}
		}
		printf("Case #%d: %04d\n",q,dp[19]);
	}

	return 0;
}


