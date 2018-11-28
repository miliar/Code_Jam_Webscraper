#include <iostream>
#include <algorithm>
using namespace std;
int ca, list[10], sign[10], k, len, Min;
char a[2000], b[2000];
void fun()
{
	int i, j;
	int re;
	int length = strlen(a);
	int t = 0;
	for(i = 0; i < length;)
	{
		for(j = 0; j < len; j++)
		{
			b[i] = a[list[j]-1+t];
			i++;
		}
		t = t + k;
	}
	re = 0;
	for(i = 0; i < length;)
	{
		j = i;
		while((j+1) < length && b[j] == b[j+1])
		{
			j ++;
		}
		j ++;
		i = j;
		re ++;
	}
	if(Min == -1 || re < Min)
		Min = re;
}
void dfs()
{
	int i;
	if(len == k)
	{
		fun();
		return;
	}
	for(i = 1; i <= k; i++)
	{
		if(!sign[i])
		{
			sign[i] = 1;
			list[len] = i;
			len ++;
			dfs();
			len --;
			sign[i] = 0;
		}
	}
}
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i;
	scanf("%d",&ca);
	for(i = 1; i <= ca; i++)
	{
		scanf("%d", &k);
		scanf("%s", a);
		memset(sign, 0, sizeof(sign));
		len = 0;
		Min = -1;
		dfs();
		printf("Case #%d: %d\n", i, Min);
	}
	return 0;
}