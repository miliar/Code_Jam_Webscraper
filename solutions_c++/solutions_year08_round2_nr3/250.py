#include <cstdio>

struct Node
{
	int num,next;
}pool[5001];

int k,n,d[5001],count,now,first,last,c,a;

int main()
{
 	freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
	scanf("%d",&c);
	for(int C = 1;C <= c;++C)
	{
		scanf("%d",&k);
		for(int i = 0;i < k;++i)
		{
			pool[i].num = i+1;
			pool[i].next = i+1;
		}
		pool[k-1].next = 0;
		first = 0;
		last = k-1;
		count = now = 1;
		while(now != k+1)
		{
			while(count != now)
			{
				first = pool[first].next;
				last = pool[last].next;
				count++;
			}
			d[pool[first].num] = now;
			now++;
			pool[last].next = pool[first].next;
			first = pool[last].next;
			count = 1;
		}
		scanf("%d",&n);
		printf("Case #%d:",C);
		for(int i = 0;i < n;++i)
		{
			scanf("%d",&a);
			printf(" %d",d[a]);
	}
		printf("\n");
	}
}
