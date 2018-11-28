#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>

int T,N,M,cnt[33];
bool map[32][32],ok[32][33];
char str[32][33];

void check(int x,int y,int size)
{
	int i,j;
	for(i = x;i < x + size;i++)
		for(j = y;j < y + size;j++)
		{
			if(!ok[i][j])
				return;
		}
	for(i = x;i < x + size;i++)
		for(j = y;j + 1 < y + size;j++)
		{
			if(map[i][j] == map[i][j+1])
				return;
		}
	for(j = y;j < y + size;j++)
		for(i = x;i + 1 < x + size;i++)
		{
			if(map[i][j] == map[i+1][j])
				return;
		}
	for(i = x;i < x + size;i++)
		for(j = y;j < y + size;j++)
			ok[i][j] = false;
	cnt[size]++;
	return;
}

int main()
{
	int i,j,k;
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%d%d",&N,&M);
		for(i = 0;i < N;i++)
			scanf("%s",str[i]);
		for(i = 0;i < N;i++)
			for(j = 0;j < M/4;j++)
			{
				int t;
				if(str[i][j] >= '0' && str[i][j] <= '9')
					t = str[i][j] - '0';
				else
					t = str[i][j] - 'A' + 10;
				for(k = 0;k < 4;k++)
				{
					if(t & (1 << (3 - k)))
						map[i][4*j+k] = true;
					else
						map[i][4*j+k] = false;
				}
			}
		memset(cnt,0,sizeof(cnt));
		memset(ok,true,sizeof(ok));
		for(int size = (M < N ? M : N);size >= 1;size--)
			for(i = 0;i + size <= N;i++)
				for(j = 0;j + size <= M;j++)
					check(i,j,size);
		int ans = 0;
		for(i = 32;i >= 1;i--)
		{
			if(cnt[i])
				ans++;
		}
		printf("Case #%d: %d\n",Case,ans);
		for(i = 32;i >= 1;i--)
		{
			if(cnt[i])
				printf("%d %d\n",i,cnt[i]);
		}
	}
	return 0;
}

