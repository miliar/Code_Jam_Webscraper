#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<string>
#include<set>
#include<map>
using namespace std;
#define LIM 52
#define check(a,b) (mat[a][b]=='#'&&(((a)>=0)&&((a)<m))&&(((b)>=0)&&((b)<n)))
char mat[LIM][LIM];
int main()
{
	int t, m, n, i, j, k, flag;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		flag=0;
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
		scanf("%s",mat[i]);
		for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		{
			if(mat[i][j]=='#')
			{
				if(check(i+1,j)&&check(i,j+1)&&check(i+1,j+1))
				{
					mat[i][j]='/';
					mat[i+1][j]='\\';
					mat[i][j+1]='\\';
					mat[i+1][j+1]='/';
				}
				else
				{
					flag=1;
					goto end;
				}
			}
		}
		end :
		if(flag==1)
		printf("Case #%d:\nImpossible\n",k);
		else
		{
			printf("Case #%d:\n",k);
			for(i=0;i<m;i++)
			printf("%s\n",mat[i]);
		}
	}
	return 0;
}
