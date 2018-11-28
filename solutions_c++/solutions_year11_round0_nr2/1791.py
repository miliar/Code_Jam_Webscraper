//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

bool op[128][128];
char com[128][128];

char STACK[2000];
int  top;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int T, C, D, t, i, j, n;
	char str[4], elem[2000];
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		memset(op, 0, sizeof(op));
		memset(com, 0, sizeof(com));
		scanf("%d", &C);
		for (i=0;i<C;++i)
		{
			scanf("%s", str);
			char a = str[0], b = str[1];
			com[a][b]=com[b][a]=str[2];
		}
		scanf("%d", &D);
		for (i=0;i<D;++i)
		{
			scanf("%s", str);
			char a=str[0], b=str[1];
			op[a][b]=op[b][a]=true;
		}
		top = 0;
		scanf("%d %s", &n, elem);
		for (i=0;i<n;++i)
		{
			STACK[top++] = elem[i];
			if (top > 1)
			{
				char a;
				if (a=com[STACK[top-1]][STACK[top-2]])
				{
					--top;
					STACK[top-1]=a;
				}
				else
				{
					for(j=0; j<top-1;++j)
					{
						if (op[STACK[j]][elem[i]])
						{
							top = 0;break;
						}
					}
				}
			}
		}
		printf("Case #%d: [", t);
		if (top>0) printf("%c", STACK[0]);
		for (i=1;i<top;++i)
			printf(", %c",STACK[i]);
		printf("]\n");
	}
	return 0;
}