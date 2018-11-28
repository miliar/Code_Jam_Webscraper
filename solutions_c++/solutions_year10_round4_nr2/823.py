#include<cstdio>
#include<algorithm>
#include<cmath>
#define MAX 1024
using namespace std;

int M[MAX];
int cost;
int z=0;
int c;
void check(int left,int right)
{
	
	int i;
	if(left>=right)
		return ;
	for(i=left;i<right;i++)
	{
		if(M[i]>0)
			break;
	}
	if(i!=right)
	{
		for(i=left;i<right;i++)
			M[i]--;
		c++;
		int mid=(left+right)/2;
		check(left,mid);
		check(mid,right);
	}
	else
	{
		return ;
	}
}

int main()
{
	int t;
	int p;
	scanf("%d",&t);
	int i,j,n;
	while(t--)
	{
		c=0;
		scanf("%d",&p);
		int l=pow(2.0,p);
		for(i=0;i<l;i++)
		{
			scanf("%d",&M[i]);
			M[i]=p-M[i];
		}
		for(i=0;i<p;i++)
		{
			int n=pow(2.0,p-i-1);
			for(j=0;j<n;j++)
			{
				scanf("%d",&cost);
			}
		}
		check(0,pow(2.0,p));
		printf("Case #%d: %d\n",++z,c);
	}
	return 0;
}
