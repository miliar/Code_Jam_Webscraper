#include <iostream>
#include <algorithm>

#define MAXN 2000

using namespace std;

char str[MAXN], temp[MAXN];
int L[10], load[10];
int k, ans;

void judge( int len )
{
	int i, j, Tep;
	int l = strlen(str);
	int t = 0;
	i = 0;
	while ( i < l )
	{
		for(j = 0; j < len; j ++)
		{
			temp[i++] = str[L[j]-1+t];
		}
		t += k;
	}
	Tep = 0;
	i = 0;
	while ( i < l )
	{
		j = i;
		while( j+1 < l && temp[j] == temp[j+1] )
		{
			j ++;
		}
		j ++;
		i = j;
		Tep ++;
	}
	if(ans == -1 || Tep < ans)
		ans = Tep;
}

void DFS( int len )
{
	int i;
	if(len == k)
	{
		judge(len);
		return;
	}
	for(i = 1; i <= k; i ++)
	{
		if(load[i])
			continue;
		load[i] = 1;
		L[len] = i;
		DFS(len+1);
		load[i] = 0;
	}
}
int main(void)
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int Case = 0, T;
	scanf("%d",&T);
	while ( T -- )
	{
		Case ++;
		scanf("%d",&k);
		scanf("%s",str);
		memset(load,0,sizeof(load));
		ans = -1;
		DFS(0);
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}