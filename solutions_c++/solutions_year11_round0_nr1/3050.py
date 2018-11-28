#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;

struct st 
{
	char bot;
	int pos;
}a[200];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, Case=1;
	scanf("%d", &T);
	while(T--)
	{
		int i, j, n, res=0, p=0;
		int nextb=-1, nexto=-1, nowb=1, nowo=1;
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		for (i=0; i<n; i++)
		{
			scanf(" %c %d", &a[i].bot, &a[i].pos);
			if(nextb==-1 && a[i].bot=='B') nextb=a[i].pos;
			if(nexto==-1 && a[i].bot=='O') nexto=a[i].pos;
		}
		while (1)
		{
			res++;
			if(a[p].bot=='O') //下一次要O踩
			{
				if (nowo==nexto) //在当前位置，踩！
				{
					p++;
					nexto=-1;
					for (j=p; j<n; j++) //找下一个O
					{
						if(a[j].bot=='O') 
						{
							nexto=a[j].pos;
							break;
						}
					}
					if(nowb!=-1 && nowb<nextb) nowb++;
					else if(nowb!=-1 && nowb>nextb) nowb--;
				}
				else
				{
					if(nowo<nexto) nowo++;
					else if(nowo>nexto) nowo--;

					if(nextb!=-1 && nowb<nextb) nowb++;
					else if(nextb!=-1 && nowb>nextb) nowb--;
				}
			}

			else if(a[p].bot=='B') //下一次要B踩
			{
				if (nowb==nextb) //在当前位置，踩！
				{
					p++;
					nextb=-1;
					for (j=p; j<n; j++) //找下一个B
					{
						if(a[j].bot=='B') 
						{
							nextb=a[j].pos;
							break;
						}
					}
					if(nexto!=-1 && nowo<nexto) nowo++;
					else if(nexto!=-1 && nowo>nexto) nowo--;
				}
				else
				{
					if(nowb<nextb) nowb++;
					else if(nowb>nextb) nowb--;
					
					if(nexto!=-1 && nowo<nexto) nowo++;
					else if(nexto!=-1 && nowo>nexto) nowo--;
				}
			}
			if(p>=n) break;
		}
		printf("Case #%d: %d\n", Case++, res);
	}
	return 0;
}
