//#include <iostream>
#include <stdio.h>
#include <string.h>


const int nmax = 1000+5;

int mgi[nmax], mnext[nmax], mcost[nmax];
int r, k, n;

void init()
{
	memset(mgi,0,sizeof(mgi));
	memset(mnext,0,sizeof(mnext));
	memset(mcost,0,sizeof(mcost));
	scanf("%d%d%d",&r,&k,&n);
	for(int i=0; i<n; ++i)
	{
		scanf("%d",&mgi[i]);
	}
}

int solve()
{
	int csum = 0;
	int iter = 0;
	int ret = 0;
	for(int i=0; i<n; ++i)
	{
		while(1)
		{
			if(csum+mgi[iter]>k)
			{
				mnext[i]=iter;
				mcost[i]=csum;
				csum-=mgi[i];
				break;
			}
			else
			{

				csum+=mgi[iter];
				++iter;
				if(iter>=n) iter = 0;
				if(iter==i)
				{
					mnext[i]=iter;
					mcost[i]=csum;
					csum-=mgi[i];
					break;
				}
			}
		}

	}
	iter = 0;
	for(int i=0;i<r;++i)
	{
		ret += mcost[iter];
		iter = mnext[iter];
	}
	return ret ;

}


int main()
{
	freopen("d:\\in.txt","r",stdin);
	freopen("d:\\out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int caseId=1; caseId<=t; ++caseId)
	{
		printf("Case #%d: ",caseId);
		init();
		int ret = solve();
		printf("%d\n",ret);

	}
	
	return 0;
}