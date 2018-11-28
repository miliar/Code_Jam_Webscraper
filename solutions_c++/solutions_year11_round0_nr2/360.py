#include <iostream>
#include <stdio.h>
#include <string>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int tran(char a)
{
	return a-'A'+1;
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int op[37][37];
	int comb[37][37];
	int T;
	scanf("%d",&T);
	int cas = 0;
	while(T--)
	{
		memset(op,0,sizeof(op));
		memset(comb,0,sizeof(comb));
		char str[200];
		int C,N;
		scanf("%d",&C);
		for(int i = 0; i < C; i++)
		{
			scanf("%s",str);
			int a = tran(str[0]),b = tran(str[1]),c = tran(str[2]);
			comb[a][b] = c;
			comb[b][a] = c;
		}
		scanf("%d",&N);
		for(int i = 0; i < N; i++)
		{
			scanf("%s",str);
			int a = tran(str[0]), b = tran(str[1]);
			op[a][++op[a][0]] = b;
			op[b][++op[b][0]] = a;
		}
		int M;
		scanf("%d",&M);
		scanf("%s",str);
		int used[37] = {0};
		int Q[10000] = {0};
		int top = -1;
		for(int i = 0; i < M; i++)
		{
			int now = tran(str[i]);
			while(top >= 0 && comb[now][Q[top]])
			{
				used[Q[top]]--;
				now = comb[now][Q[top]];
				top--;
			}
			bool flag = false;
			for(int j = 1; j <= op[now][0]; j++)
			{
				if(used[op[now][j]])
				{
					memset(used,0,sizeof(used));
					flag = true;
					break;
				}
			}
			if(flag) top = -1;
			else
			{
				used[now]++;
				Q[++top] = now;
			}
		}
		printf("Case #%d: [",++cas);
		for(int i = 0; i < top; i++)
		{
			printf("%c, ",Q[i]+'A'-1);
		}
		if(top >= 0) printf("%c]\n",Q[top]+'A'-1);
		else printf("]\n");
	}
	return 0;
}
