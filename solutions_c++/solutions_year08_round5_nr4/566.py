#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstdarg>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

#define LL __int64
#define ALL(v) v.begin(), v.end()
#define sz(v) sizeof(v)
#define VI vector<int>
#define pb push_back
#define debug(x) cerr<<#x<<"="<<x<<endl
#define fne(i,a,b) for(i=a;i<b;i++)
#define feq(i,a,b) for(i=a;i<=b;i++)

template<class T> inline void max(T& x, T y) { if(y>x) x=y; }
template<class T> inline void min(T& x, T y) { if(y<x) x=y; }

inline void OUT(const char* fmt, ...)
{
	va_list va;
	va_start(va,fmt);
	vprintf(fmt,va);
	vfprintf(stderr,fmt,va);
	va_end(va);
}
//#define OUT printf

const int maxn=200;
int a[maxn][maxn];

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	int cas;
	scanf("%d",&cas);
	for(int lv=1;lv<=cas;lv++) {
		OUT("Case #%d: ",lv);
		int w,h, R;
		int i,j,k, r, c;
		scanf("%d%d%d",&h,&w,&R);
		memset(a,0,sz(a));
		fne(i,0,R) {
			scanf("%d%d",&r,&c);
			a[r][c]=-1;
		}
		a[1][1]=1;
		feq(i,2,h) feq(j,1,w) {
			if(a[i][j]!=-1) {
				if(i-1>=1&&j-2>=1&&a[i-1][j-2]!=-1) {
					a[i][j]+=a[i-1][j-2];
					a[i][j]%=10007;
				}
				if(i-2>=1&&j-1>=1&&a[i-2][j-1]!=-1) {
					a[i][j]+=a[i-2][j-1];
					a[i][j]%=10007;
				}
			}
		}
		OUT("%d\n",a[h][w]);
	}

	return 0;
}
