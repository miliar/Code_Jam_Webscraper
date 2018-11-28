#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <iostream>
#include <sstream>
#include <set>
#define zbwmqlw
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define pow(x) (1<<(x))
#define powLL(x) ((1LL)<<(LL)(x))
#define sqr(x) ((x)*(x))
#define abs(x) ((x)>0?(x):-(x))
#define lch(x) (((x)<<1)+1)
#define rch(x) (((x)<<1)+2)
#define PI 3.141592653589793238463
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define fill(x,y) memset((x),(y),sizeof(x))
#define sro(x,r,l) for ((x)=(r);(x)>=(l);--(x))
using namespace std;
typedef long long LL;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-7;
template<class T> inline void checkmin(T &a,const T &b) {if (b<a) a=b;}
template<class T> inline void checkmax(T &a,const T &b) {if (b>a) a=b;}

const int N=2100;

bool map[N][N];
int f[N][N],count[N];
bool used[N][N];
int ans;
pair<int,int> select;
int m,n,T;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
#endif
	scanf("%d",&T);
	for (int t=1;t<=T;++t) {
		scanf("%d%d\n",&m,&n);
		for (int i=1;i<=m;++i) {
			for (int j=1;j*4<=n;++j) {
				char c;
				int a;
				scanf("%c",&c);
				if (c>='A') a=c-'A'+10;else a=c-'0';
				map[i][j*4-3]=((a&8)>0);
				map[i][j*4-2]=((a&4)>0);
				map[i][j*4-1]=((a&2)>0);
				map[i][j*4]=((a&1)>0);
			}
			scanf("\n");
		}
		memset(count,0,sizeof(count));
		memset(used,0,sizeof(used));
		while (1) {
			ans=0;
			select=make_pair(0,0);
			for (int i=1;i<=m;++i) for (int j=1;j<=n;++j) {
				if (used[i][j])
					f[i][j]=0;
				else if (i==1 || j==1) 
					f[i][j]=1;
				else {
					if (map[i][j]==!map[i-1][j] && map[i][j]==!map[i][j-1] && map[i][j]==map[i-1][j-1])
						f[i][j]=min(f[i-1][j],min(f[i][j-1],f[i-1][j-1]))+1;
					else
						f[i][j]=1;
				}
				if (f[i][j]>ans) {
					ans=f[i][j];
					select=make_pair(i,j);
				}
			}
			if (ans==0) break;
			++count[ans];
			for (int i=select.first;i>=select.first-ans+1;--i) for (int j=select.second;j>=select.second-ans+1;--j)
				used[i][j]=true;
		}
		int orz=0;
		for (int i=n;i>=1;--i) if (count[i]>0) ++orz;
		printf("Case #%d: ",t);
		printf("%d\n",orz);
		for (int i=n;i>=1;--i) if (count[i]>0) printf("%d %d\n",i,count[i]);
	}
}
