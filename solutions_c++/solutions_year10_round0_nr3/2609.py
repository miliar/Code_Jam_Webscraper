#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int size[1001];
	int R;
	int k;
	int N;
	int test;
	int start,end;
	int count;
	int total;
	int f=0;
	scanf("%d",&test);
	while(test--)
	{
		scanf("%d%d%d",&R,&k,&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d",&size[i]);
		}
		start=0;
		count=0;
		total=0;
		int j=0;
		for(int i=0;i<R;i++)
		{
			int l=j;
			while(count + size[j] <= k)
			{
				count+=size[j];
				j++;
				j=j%N;
				if(l==j)
				{
					break;
				}
			}
			total+=count;
			count=0;
		}
		printf("Case #%d: %d\n",f+1,total);
		f++;
	}
	return 0;
}
