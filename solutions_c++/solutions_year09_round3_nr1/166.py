#include<iostream>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
#define fod(i,u,d) for (long i=(u); i>=(d); --i)
using namespace std;

const long maxn=101;

char s[maxn];
long a[maxn],num[maxn],b[maxn],n,t;

void init()
{
	scanf("%s",s);
	n=strlen(s);
	for (long i=0; i<n; ++i)
		if (s[i]>='0' && s[i]<='9') num[i+1]=s[i]-'0';
	    else num[i+1]=s[i]-'a'+10; 
}
void solve()
{
	memset(b,255,sizeof(b));
	a[1]=1, b[num[1]]=1;
	long m=0;
	fo(i,2,n) {
		if (b[num[i]]==-1) {
			b[num[i]]=m;
		    if (m==0) m=2; else ++m;
		}
		a[i]=b[num[i]];
	}
	long long ans=0,jie=1,big=0;
	fo(i,1,n) if (a[i]>big) big=a[i]; ++big;
	fod(i,n,1) ans+=a[i]*jie, jie*=big;
	printf("%I64d\n",ans);
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
