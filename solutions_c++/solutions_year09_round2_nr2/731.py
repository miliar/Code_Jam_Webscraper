#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<algorithm>
using namespace std;
int num[30], t;
char out[30], need[30];
void work()
{
	char  p;
	int i;
	t = strlen(need);
	for(i = t - 1; i >= 1; i--)
	{
		if (need[i] > need[i - 1])
		{
			p = i;
			for(int j = i + 1; j <= t - 1; j++)
			{
				if (need[j] > need[i - 1] && need[j] < need[p])
				{
					p = j;
				}
			}
			int q = need[i - 1];
			need[i - 1] = need[p];
			need[p] = q;
			sort(need + i, need + t);
			break;
		}
	}
	if (i == 0)
	{
		int tt = 0;
		for(i = t - 1; i >= 0; i--)
			if (need[i] != '0')
				break;
			else
				tt++;
		out[0] = need[i];
		out[1] = '0';
		p = 2;
		for(int j = 1; j <= tt; j++)
			out[p++] = '0';
		i--;
		for(; i >= 0;  i--)
			out[p++] = need[i];
		out[p] = '\0';
		memcpy(need, out, sizeof(out));
	}
}
int main()
{
	int all;
	freopen("11.in","r",stdin);
	freopen("a.txt","w",stdout);
	int cas, nca;
	scanf("%d",&cas);
	nca = 0;
	while(cas--)
	{
		nca++;
		scanf("%s",need);
		work();
		printf("Case #%d: %s\n",nca, need);
	}

}