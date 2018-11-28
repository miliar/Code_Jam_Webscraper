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

int T, n, m, k;
int arr[105][105];
int res[105][105];
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};


bool can(int x, int y){
	return x>=0 && y>=0 && x<n && y<m;
}


int go(int x, int y){
	if (res[x][y]!=-1)
		return res[x][y];
	int p = -1;
	
	Rep(i,4){
		int xx = x + dx[i], yy = y + dy[i];
		if (can(xx,yy)){
			if (p != -1 && arr[xx][yy]<arr[x+dx[p]][y+dy[p]] ){
				p = i;
			}
			if (p == -1 && arr[xx][yy]<arr[x][y] ){
				p = i;
			}
		}
	}

	if (p == -1)
		return res[x][y] = k++;
	else
		return res[x][y] = go(x+dx[p],y+dy[p]);

}

int main() { 
	freopen("BB.in","rt",stdin);
	freopen("BB.out","wt",stdout);
	scanf("%d\n",&T);
	For(TT,1,T){
		Fill(res,-1);
		k = 0;
		scanf("%d%d\n",&n,&m);
		Rep(i,n)Rep(j,m){
			scanf("%d",&arr[i][j]);
		}

		printf("Case #%d:\n",TT);
		Rep(i,n){
			Rep(j,m){
				if (res[i][j] == -1)
					go(i,j);
				printf("%c ",char(res[i][j]+'a'));
			}
			printf("\n");
		}		

	}

	return 0;
}


