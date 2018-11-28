#include<iostream>

using namespace std;

int t,n,q,f[101][101],a[101];

void getans(int left,int right)
{
	if(left>right)
		return ;
	if(left==right)
	{
		f[left][right]=a[right+1]-a[left-1]-2;
		return ;
	}
	if(f[left][right])
		return ;
	f[left][right]=1<<29;
	for(int i=left;i<=right;++i)
	{
		getans(left,i-1);
		getans(i+1,right);
		f[left][right]<?=f[left][i-1]+f[i+1][right];
	}
	f[left][right]+=a[right+1]-a[left-1]-2;
	return ;
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	for(int z=1;z<=t;++z)
	{
		memset(f,0,sizeof(f));
		scanf("%d %d",&n,&q);
		for(int i=1;i<=q;++i)
			scanf("%d",a+i);
		a[0]=0;
		a[q+1]=n+1;
		getans(1,q);
		printf("Case #%d: %d\n",z,f[1][q]);
	}
	return 0;
}
