#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const M=1050000;
int f[2200000],g[2200000],fr[2200000];

long long sqtt1(int a,int b)
{
	int a0=fr[b];
	if(a<a0)a0=a;
	return g[a0]+(long long)(a-a0)*b;
}

long long sqtt2(int a,int b)
{
	int a0=b;
	if(a<a0)a0=a;
	return (long long)a0*(a0+1)/2+(long long)(a-a0)*a0;
}

long long sqtt(int a,int b)
{
	return sqtt1(a,b)-sqtt2(a,b);
}

long long sqttt(int a1,int a2,int b1,int b2)
{
	return sqtt(a2,b2)-sqtt(a2,b1)-sqtt(a1,b2)+sqtt(a1,b1);
}

int main()
{
	freopen("c:\\C-small-attempt0.in","r",stdin);
	freopen("c:\\a.out","w",stdout);
	
	f[0]=0;
	f[1]=1;
	int p=2;
	for(int i=1;i<=M;++i)
		for(;p<=i+f[i];++p)f[p]=i;
	memset(fr,0,sizeof(fr));
	for(int i=M;i>=1;--i)
	{
		f[i]=f[i-1]+i;
		fr[f[i]]=i;
	}
	for(int i=1;i<=M;++i)
		if(fr[i-1]>fr[i])fr[i]=fr[i-1];
	g[0]=0;
	for(int i=1;i<=M;++i)
		g[i]=g[i-1]+f[i];
	int t;
	scanf("%d",&t);
	for(int t1=1;t1<=t;++t1)
	{
		int a1,a2,b1,b2;
		scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
		long long ans=sqttt(a1-1,a2,b1-1,b2)+sqttt(b1-1,b2,a1-1,a2);
		int c1=max(a1,b1),c2=min(a2,b2);
		if(c1<=c2)ans+=c2-c1+1;
		ans=(long long)(a2-a1+1)*(b2-b1+1)-ans;
		printf("Case #%d: %Ld\n",t1,ans);
	}
	scanf("\n");
	return 0;
}


