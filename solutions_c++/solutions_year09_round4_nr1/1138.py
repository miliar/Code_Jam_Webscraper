#include <cstdio>
#include <algorithm>
int f(char *row,int n)
{
	int i=n-1;
	for(;i>=0;--i)
	{
		if(row[i]=='1')break;
	}
	return i;
}
int n;
int v[100];
bool ok()
{
	for(int i=0;i<n;++i)
	{
		if(v[i]>i)return false;
	}
	return true;
}
int main()
{
	int t;
	scanf("%d",&t);
	char tab[100][100];
	for(int i=1;i<=t;++i)
	{
		scanf("%d",&n);
		for(int x=0;x<n;++x)
		{
			scanf("%s",tab[x]);
			v[x]=f(tab[x],n);
		}
		int a=0;
		for(int j=0;j<n-1;++j)
		{
			if(v[j]<=j)continue;
			int x=j+1;
			for(x=j;x<n-1;++x)
			{
				if(v[x]<=j)break;
			}
			for(;x>j;--x)
			{
				std::swap(v[x],v[x-1]);
				++a;
			}
		}
		printf("Case #%d: %d\n",i,a);
	}
	return 0;
}

