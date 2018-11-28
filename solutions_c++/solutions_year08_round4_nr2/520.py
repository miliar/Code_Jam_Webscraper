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
#define SZ(v) v.size()
#define VI vector<int>
#define pb push_back
#define debug(x) cerr<<#x<<"="<<i<<endl
#define f0(i,n) for(i=0;i<n;i++)
#define f1(i,n) for(i=1;i<=n;i++)

inline void OUT(const char* fmt, ...)
{
	va_list va;
	va_start(va,fmt);
	vprintf(fmt,va);
	vfprintf(stderr,fmt,va);
	va_end(va);
}
//#define OUT printf

const int maxn=1000;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int cas;
	scanf("%d",&cas);
	for(int lv=1;lv<=cas;lv++) {
		OUT("Case #%d: ",lv);
		int n,m,a;
		scanf("%d%d%d",&n,&m,&a);
		int i,j,k,p;
		for(i=0;i<=n;i++) for(j=0;j<=m;j++) {
			for(k=0;k<=n;k++) {
				p=a+j*k;
				if(p==0) goto end;
				if(i!=0&&p>0&&p%i==0&&p/i<=m) { p/=i; goto end; } 
				p=j*k-a;
				if(p==0) goto end;
				if(i!=0&&p>0&&p%i==0&&p/i<=m) { p/=i; goto end; } 
			}
		}
		OUT("IMPOSSIBLE\n"); continue;
end:;
		OUT("%d %d %d %d %d %d\n",0,0,i,j,k,p);
	}
	return 0;
}
