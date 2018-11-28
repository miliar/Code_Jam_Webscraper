#include<stdio.h>
#include<algorithm>
using namespace std;
#pragma comment(linker, "/STACK:10000000"); 
int a[2000],b[2000];
int solved[2000][2000];
int solve(int l,int r ,int c)

{
	if(l*c>=r)return 0;
	//printf("%d\n",solved[l][r]);
    if(solved[l][r]!=-1)return solved[l][r];
	int minn=100000000;
	for(int j=l+1;j<r;j++)
	{
		if (max(solve(l,j,c),solve(j,r,c   ))+1<minn)minn=max(solve(l,j,c),solve(j,r,c   ))+1;
	}
	return solved[l][r]=minn;

}

int main()
{
	freopen("B.in","rt",stdin);
	freopen("B.out","wt",stdout);

	int t;
	int sum=0;
	scanf("%d",&t);
	int l,r,k;
	for (int c=0;c<t;c++) 
	{
		for(int i=1;i<1003;i++)
			for(int j=1;j<1003;j++)
			{
				solved[i][j]=-1;
			}
		scanf("%d %d %d",&l,&r,&k);
        printf("Case #%d: %d\n",c+1,solve(l,r,k));
	}


}