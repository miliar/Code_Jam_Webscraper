#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const long long oo=2e18;
long long Test,t,n,l;
long long b[109],f[200009];
long long q[2000009];
bool inque[200009];

bool cmp(long long x,long long y)
{
	return x>y;
}

void init()
{
	cin>>l>>n;
	for (long long i=0;i<n;i++) cin>>b[i];
	sort(b,b+n,cmp);	n--;
}

void work()
{
	long long ans=oo,op=1,cl=1,m=l%b[0];
	memset(inque,0,sizeof(inque));
	for (long long i=1;i<=b[0];i++) f[i]=oo;
	f[0]=0;	q[1]=0;	inque[0]=true;
	while (op>=cl)
	{
		long long k=q[cl];
		for (long long i=1;i<=n;i++)
		{
			long long p=(k+b[i])%b[0];
			long long del;
			if (k+b[i]<b[0]) del=1; else del=0;
			if (f[p]>f[k]+del)
			{
				f[p]=f[k]+del;
				if(!inque[p])	inque[q[++op]=p]=true;
			}
		}
		inque[k]=false;
		cl++;
	}
	if (f[m]<oo) ans=l/b[0]+f[m];
	cout<<"Case #"<<t<<": ";
	if (ans<oo) cout<<ans<<endl; else cout<<"IMPOSSIBLE"<<endl;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>Test;
	for (t=1;t<=Test;t++)
	{
		init();
		work();
	}
	fclose(stdin);	fclose(stdout);
	return 0;
}

