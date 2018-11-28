#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=1000100;
long long s[maxn];
int f[maxn]={};
long long half(int i,int j) //i>=j
{
	int z=upper_bound(f,f+maxn,j)-f;
	//printf("%d,%d %d\n",i,j,z);
	if(z>i) return s[i];
	else return s[z-1]+(long long)j*(i-z+1);
}
long long rect(int i,int j) //i>=j
{
	if(i<j) return rect(j,i);
	//printf("%d,%d %I64d,%I64d\n",i,j,half(i,j),half(j,j));
	return half(i,j)+half(j,j);
}
int main()
{
	for(int i=1;i<maxn;i++)
	{
		if(i>1) f[i]=max(f[i],f[i-1]);
		int t=i+f[i]+1;
		if(t<maxn) f[t]=max(f[t],i);
	}
	//for(int i=1;i<100;i++) printf("%d\n",f[i]);
	s[0]=0;
	for(int i=1;i<maxn;i++) s[i]=s[i-1]+f[i];
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		long long ans=rect(a2,b2)-rect(a2,b1-1)-rect(a1-1,b2)+rect(a1-1,b1-1);
		//printf("%I64d %I64d %I64d %I64d\n",rect(a2,b2),rect(a2,b1-1),rect(a1-1,b2),rect(a1-1,b1-1));
		printf("Case #%d: %I64d\n",i,ans);
	}
	return 0;
}
