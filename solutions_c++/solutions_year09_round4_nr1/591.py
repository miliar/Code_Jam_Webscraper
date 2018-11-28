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

int n,m, T;
string mx[50];
char c[50];

bool isP(int x, int p){
	For(i,p,n-1)
		if (mx[x][i]!='0') 
			return 0;
	return 1;
}


int find(int x){
	int res = 0;
	For(i,x,n-1){
		if (isP(i,x+1)){
			res = i;
			break;
		}
	}
	string buf = mx[res];
	Ford(i,res,x+1)
		mx[i] = mx[i-1];
	mx[x] = buf;
	return res-x;
}

int main() { 
	freopen("AA.in","rt",stdin);
	freopen("AA.out","wt",stdout);
	scanf("%d",&T);
	For(TT,1,T){
		scanf("%d\n",&n);
		Rep(i,n){
			scanf("%s\n",c);
			mx[i] = c;
		}

		int res = 0; 
		Rep(i,n-1){
			res += find(i);
		}

		printf("Case #%d: %d\n",TT,res);
	}
	

	return 0;
}


