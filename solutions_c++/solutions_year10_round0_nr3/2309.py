#include <iostream>
#include <cmath>

using namespace std;

typedef struct node
{
	int cost;
	node* next;

} node_type;

int main()
{
	int i,j;
	int t;
	int r, k, n;
	long long int sum, euro;
	node g[1000], *ptr, *str;
	 

	//freopen("D:\\VC2005\\google\\2010\\ProbC\\in.txt","r",stdin);
	//freopen("D:\\VC2005\\google\\2010\\ProbC\\out.txt","w",stdout);
	freopen("D:\\VC2005\\google\\2010\\ProbC\\C-small.in","r",stdin);
	freopen("D:\\VC2005\\google\\2010\\ProbC\\C-small.out","w",stdout);
	//freopen("D:\\VC2005\\google\\2010\\ProbC\\C-large.in","r",stdin);
	//freopen("D:\\VC2005\\google\\2010\\ProbC\\C-large.out","w",stdout);

	scanf("%d\n", &t);
	for(i=1;i<=t;i++)
	{
		euro=0;
		scanf("%d %d %d\n", &r, &k, &n);
		scanf("%d", &g[0].cost);
		for(j=1;j<n;j++)
		{
			scanf("%d", &g[j].cost);
			g[j-1].next = &g[j];
		}
		g[n-1].next = &g[0];
		
		ptr=&g[0];
		str=ptr;
		while(r--)
		{
			sum=0;
			while( sum+(ptr->cost) <= k)
			{
				sum+=(ptr->cost);
				ptr=ptr->next;
				if(str==ptr) break;
			}
			str=ptr;
			euro += sum;
		}

		printf("Case #%d: %lld\n", i, euro);
	}

	fclose(stdout);
	return 0;
}
