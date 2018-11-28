#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int a[1000];
int res,n;
void fun(int l,int gff,int sss,int fuck,int flag)
{
	if(l==n)
	{
		if(gff==sss&&flag)if(fuck>res)res=fuck;
		return ;
	}
	fun(l+1,gff^a[l],sss,fuck+a[l],flag);
	fun(l+1,gff,sss^a[l],fuck,flag+1);
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t,txttttt=1;
	scanf("%d",&t);
	while(t--)
	{
		res=-9999;
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%d",&a[i]);
		fun(0,0,0,0,0);
		printf("Case #%d: ",txttttt++);
		if(res!=-9999)
			printf("%d\n",res);
		else
			printf("NO\n");
	}
	return 0;
}
