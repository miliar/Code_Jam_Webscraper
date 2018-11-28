#include "cstdlib"
#include "cctype"
#include "cstring"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "vector"
#include "string"
#include "set"
#include "map"
#include "iostream"
#include "sstream"
#include "queue"
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define MP				make_pair
#define CCQ(que)			while(!que.empty()) que.pop();
#define CC(m,what)			memset(m,what,sizeof(m))
#define FS(i,a)				for( int i = 0 ; a[i] ; i ++ )
#define FF(i,a)				for( int i = 0 ; i < a ; i ++ )
#define FOR(i,a,b)			for( int i = a ; i < b ; i ++ )
#define PP(n,m,a)			puts("---");FF(i,n){FF(j,m)cout << a[i][j] << ' ';puts("");}
const double Pi = acos(-1.0);
void read(char *a)		{	freopen(a,"r",stdin);	}
void write(char *a)		{	freopen(a,"w",stdout);	}
template<class T> inline void checkmin(T &a,T b)	{if(a < 0 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)	{if(a < b)	a = b;}
template<class T> inline int fix(T x,const int p)	{if((x%=p) >= 0) return x;return x + p;}
int dx[] = {-1,0,1,0,1,1,-1,-1};//up Right down Left
int dy[] = {0,1,0,-1,1,-1,1,-1};
//-----------------------------------------------------------------

int hh[9999];
int cost[10][1024];
int len[10];
int main() {
	read("B-small-attempt0.in");
	write("B-small-attempt0.out");
	int T;
	scanf("%d",&T);
	int cas = 1;
	while(T --) {
		int n;
		scanf("%d",&n);
		int m = (1<<n);
		for (int i = 0 ; i < m ; i ++) {
			scanf("%d",&hh[i]);
		}
		for (int i = 0 ; i < n ; i ++) {
			if(i == 0) len[i] = m/2;
			else len[i] = len[i-1]/2;
			for (int j = 0 ; j < len[i] ; j ++) {
				scanf("%d",&cost[i][j]);
			}
		}
		int ret = 0;
		for (int k = n - 1; k >= 0 ; k --) {
			int temp = m / len[k];
			for (int i = 0 ; i < len[k] ; i ++) {
				bool flag = false;
				for (int j = i*temp ; j < (i+1)*temp ; j ++) {
					if(hh[j] < n) {
						flag = true;
					}
				}
				if(flag) {
					ret ++;
					for (int j = i*temp ; j < (i+1)*temp ; j ++) {
						hh[j] ++;
					}
				}
			}
		}
		printf("Case #%d: %d\n",cas++,ret);
	}
	return 0;
}