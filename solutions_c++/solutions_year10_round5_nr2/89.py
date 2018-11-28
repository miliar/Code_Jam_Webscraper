#include <iostream>
using namespace std;

const int maxn=100+10,maxv=100000+10;
int tot,tc,n;
long long L,d[maxv],s[maxv],a[maxn];
bool v[maxv];

void init()
{
	scanf("%I64d%d",&L,&n);
	for (int i=1;i<=n;++i) 
		scanf("%I64d",&a[i]);
	sort(a+1,a+1+n);
	memset(d,0,sizeof(d));
}

void work()
{
	for (int i=0;i<a[n];++i) d[i]=-1;
	d[0]=L/a[n];
	memset(v,0,sizeof(v));
	s[1]=0;v[0]=true;
	int h=0,t=1;
	while (h!=t)
	{
		++h;
		if (h>a[n]) h=1;
		for (int i=1;i<n;++i)
		{
			long long j=(s[h]+a[i])%a[n];
			long long del,V;
			if (s[h]<=L%a[n]) V=L%a[n]-s[h];
						else  V=L%a[n]-s[h]+a[n];
			if (a[i]<=V) del=1;
				else     del=0;
			if (d[j]==-1 || d[s[h]]+del<d[j])
			{
				d[j]=d[s[h]]+del;
				if (!v[j]) 
				{	
					++t;
					if (t>a[n]) t=1;
					v[j]=true;
					s[t]=j;
				}
			}
		}
		v[s[h]]=false;
	}
}
	
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tot);
    for (int tc=1;tc<=tot;++tc)
    {
    	init();
    	work();
    	printf("Case #%d: ",tc);
    	if (d[L%a[n]]==-1) printf("IMPOSSIBLE\n");
					  else printf("%I64d\n",d[L%a[n]]);
    }
    return 0;
}
