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

const int maxn=2000;
char str[maxn];
int a[20];

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	int cas;
	scanf("%d",&cas);
	for(int lv=1;lv<=cas;lv++) {
		OUT("Case #%d: ",lv);
		int i,j,k;
		scanf("%d%s",&k,str);
		for(i=0;i<k;i++) {
			a[i]=i;
		}
		int len=strlen(str);
		int ans=len;
		do {
			char cur,pre=0; int cnt=0;
			for(i=0;i<len;i++) {
				cur=str[i-i%k+a[i%k]];
				if(cur!=pre) pre=cur,cnt++;
			}
			if(cnt<ans) ans=cnt;
		}while(next_permutation(a,a+k));
		OUT("%d\n",ans);
	}

	return 0;
}
