#include <iostream>
#include <cstdio>
using namespace std;

int N;
int p;
int T;
int S;
int scores[250];
int res;
int main(void)
{
	int i,j;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		res = 0;
		scanf(" %d %d %d",&N,&S,&p);
		for(j=0;j<N;j++)
		{
			scanf("%d",&scores[j]);
			if(p==0)
			{
				res++;
				continue;
			}
			if(3*p-2<=scores[j])
			{
				res++;
				continue;
			}
			else
			{
				if(p==1) continue;
				if(3*p-4<=scores[j] && S)
				{
					res++;
					S--;
					continue;
				}
			}
			
		}
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}
