#include<stdio.h>
#include<map>
#include<cmath>
#include<algorithm>

using namespace std;


int cell[100];
int permu[5];

int main(void)
{
	freopen("E:\\C-small.in","r",stdin);
	freopen("E:\\C-small.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tcase;
	for(tcase = 1 ; tcase <= t; tcase ++)
	{
		int p,q;
		int i;
		scanf("%d%d",&p,&q);
		for(i=0;i<q;i++)
			permu[i] = i;
		int prison[5];
		for(i=0;i<q;i++)
		{
			scanf("%d",&prison[i]);
			prison[i]--;
		}
		int result = 0x7fffffff;
		do
		{
			int bribe = 0;
			for(i=0;i<p;i++)
				cell[i] = 1;
			for(i=0;i<q;i++)
			{
				cell[prison[permu[i]]] = 0;
				int j;
				for(j=prison[permu[i]] - 1;j>=0;j--)
				{
					if(cell[j] == 0)
						break;
					else
						bribe++;
				}
				for(j=prison[permu[i]]+1;j<p;j++)
				{
					if(cell[j] == 0)
						break;
					else
						bribe++;
				}
			}
			if(bribe < result)
				result = bribe;
		}while(next_permutation(permu,permu+q));
		printf("Case #%d: %d\n",tcase,result);
	}
	return 0;
}