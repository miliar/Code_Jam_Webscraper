/*
 TASK: C. Candy Splitting
 LANG: C++
 by pasin30055
*/
#include <iostream>
#include <cstdio>

#define MAX_VAL (1<<20)
#define MAX_N 1005
#define INF 1000000000

using namespace std;

int t,iii;
int n,i,j;
int val[MAX_N];
int tmp;
int sum;
int minn;

int main()
{
	freopen("C-large.in.txt","r",stdin);
	freopen("C-large-out.txt","w",stdout);
	scanf("%d",&t);
	for(iii=0;iii<t;iii++)
	{
		scanf("%d",&n);
		tmp=0;
		minn=INF;
		sum=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&val[i]);
			sum+=val[i];
			minn=min(minn,val[i]);
			tmp=(tmp^val[i]);
		}
		if(tmp==0)
		{
			printf("Case #%d: %d\n",iii+1,sum-minn);
		}
		else
		{
			printf("Case #%d: NO\n",iii+1);
		}
	}
	return 0;
}