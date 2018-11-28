#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std ;

typedef struct NODE
{
	int gate;
	int change;
	int value;
};

NODE node[35];
int m, v, flag, ans;

void go(int depth, int nowch)
{
	if(depth < 1)
	{
		if(node[1].value == v && nowch < ans)
		{
			ans = nowch;
//			printf("----%d\n",ans);
			flag = 1;	
		}
		return;
	}	
	if (node[depth].change)
	{
		node[depth].gate = 1 - node[depth].gate;
		if (node[depth].gate == 1) 
			node[depth].value = node[depth*2].value & node[depth*2+1].value;
		else node[depth].value = node[depth*2].value | node[depth*2+1].value;
		
		go(depth - 1, nowch + 1);
		node[depth].gate = 1 - node[depth].gate;
	}
	
	if (node[depth].gate == 1) 
		node[depth].value = node[depth*2].value & node[depth*2+1].value;
	else 
		node[depth].value = node[depth*2].value | node[depth*2+1].value;
	
	go(depth - 1, nowch);
}


int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out.txt", "w", stdout);
	int n, kase ,k, i, j, l;

	scanf("%d", &n);
	for(kase = 1; kase <= n; kase ++)
	{
		scanf("%d %d", &m, &v);
		for (i = 1; i <= (m-1)/2; i ++)
		{
			scanf("%d %d",&node[i].gate, &node[i].change);
		}
		for (i; i <= m; i++)
		{
			scanf("%d",&node[i].value);
		}
		flag = 0;
		ans = 99999999;
		go((m - 1) / 2 , 0);			
		
		printf("Case #%d: ", kase);
		if (flag) 
			printf("%d\n", ans);
		else 
			printf("IMPOSSIBLE\n");	
	}
//	system("pause");
	return 0;
}



