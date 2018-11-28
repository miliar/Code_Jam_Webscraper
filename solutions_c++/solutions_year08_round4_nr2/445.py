// Tim  

#include <queue> 
#include <map> 

#include <set>
#include <stack> 
#include <list>
#include <numeric>

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 

using namespace std;
#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b)  for (int i=int(a); i<=int(b); ++i)
#define Ford(i,a,b) for (int i=int(a); i>=int(b); --i) 
#define Rep(i,n)    for (int i=0; i<int(n); ++i)
#define RepV(i,v)   for (int i=0; i<sz(v); ++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
typedef pair <int,int> PI;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;
typedef long long LL;

const string pr_name="Bs";
const int oo=10000;
int T,n,m,a;
int x[3]={0},y[3];

int sq(int x1, int y1, int x2, int y2){
	return x1*y2-x2*y1;

}

int main() {
	freopen((pr_name+".in").c_str(),"rt",stdin);
	freopen((pr_name+".out").c_str(),"wt",stdout);
	
	scanf("%d\n",&T);
	For(TT,1,T){
		scanf("%d%d%d\n",&n,&m,&a);
		Fill(x,0);
		Fill(y,0);
		bool ok=0;
		if (n*m>=a)
		Rep(i1,n+1) Rep(i2,n+1) Rep(j1,m+1) Rep(j2,m+1){
			if (sq(i1,j1,i2,j2)==a) {
				x[1]=i1;
				x[2]=i2;
				y[1]=j1;
				y[2]=j2;
				ok=1;
				goto yy;
			}
		}


		yy:
		printf("Case #%d:",TT);
		if (ok)
			Rep(i,3) printf(" %d %d",x[i],y[i]);
		else 
			printf(" IMPOSSIBLE");
		printf("\n");

	}


	return 0;
}


