#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int a[10];
bool used[105];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outc1.txt","w",stdout);
	int i,j,p,t,q,test=0,count;
	scanf("%d",&t);
	while(t>0)
	{
		t--;
		test++;
		scanf("%d%d",&p,&q);
		for(i=0;i<q;i++)
			scanf("%d",&a[i]);
		sort(a,a+q);
		int *beg=a;
		int *end=a+q;
		int max=0x7fffffff;
		do{
			memset(used,0,sizeof(used));
			count=0;
			for(i=0;i<q;i++)
			{
				used[a[i]]=1;
				for(j=a[i]+1;j<=p;j++)
				{
					if(!used[j])
						count++;
					else
						break;
				}
				for(j=a[i]-1;j>0;j--)
				{
					if(!used[j])
						count++;
					else
						break;
				}
			}
			if(count<max)
				max=count;
		}while(next_permutation(beg,end));
		printf("Case #%d: %d\n",test,max);
	}
	return 0;
}
