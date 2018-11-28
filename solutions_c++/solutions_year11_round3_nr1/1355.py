#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int n,m;
char a[1000][1000];
bool solve()
{
	int i,j;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
			if(a[i][j] == '#')
			{
				if(a[i][j+1]!='#' || a[i+1][j]!='#' || a[i+1][j+1]!='#')
					return false;
				a[i][j] =  a[i+1][j+1] ='/';
				a[i][j+1]= a[i+1][j] = '\\';
			}
	return true;
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("A.out","wt",stdout);
	int TC,i;
	scanf("%d",&TC);
	for(int tc = 1;tc<=TC;tc++)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%s",a[i]);
		printf("Case #%d:\n",tc);
		if(solve())
			for(i=0;i<n;i++)
				printf("%s\n",a[i]);
		else printf("Impossible\n");
	}
	return 0;
}