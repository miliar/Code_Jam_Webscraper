#include<iostream>
#include<stdio.h>
#include<string.h>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
#define fod(i,u,d) for (long i=(u); i>=(d); --i)
using namespace std;

const long maxn=50;

long n,t;
long pos[maxn];
char g[maxn][maxn];

void init()
{
	scanf("%d",&n);
	fo(i,0,n-1) scanf("%s",g[i]);
}
void solve()
{
	fo(i,1,n) {
		pos[i]=1;
		fod(j,n,1) 
		    if (g[i-1][j-1]=='1') {pos[i]=j; break;}
	}
	long tmp, ans=0;
	fo(i,1,n-1)
		fo(j,i,n)
		    if (pos[j]<=i)  {
		       fod(l,j,i+1) {
		           tmp=pos[l], pos[l]=pos[l-1], pos[l-1]=tmp;
				   ++ans;
	           }
			   break;
	       }
	printf("%d\n",ans);
}
int main()
{
	freopen("AL.in","r",stdin);
	freopen("AL.out","w",stdout);
	scanf("%d",&t);
	fo(l,1,t) {
		init();
		printf("Case #%d: ",l);
		solve();
	}
	return 0;
}
