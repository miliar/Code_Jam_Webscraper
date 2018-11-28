#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int T;
bool opp[200][200];
char com[200][200];
int C,D,N;
char str[105];
int S[200];
int &size = S[0];
bool check(int cur)
{
	for(int j = 1;j <= size;++j)
	{
		if(opp[cur][S[j]])
		{
			return true;
		}
	}
	return false;
}
void solve()
{
	size = 0;
	int len = strlen(str);
	for(int i = 0;i < len;++i)
	{
		if(size == 0)	S[++size] = str[i];
		else
		{
			int cur = str[i];
			int top = S[size];
			if(com[cur][top] != 0)
			{
				S[size] = com[cur][top];
			}
			else if(check(cur))
			{
				size = 0;
			}
			else	S[++size] = str[i];
		}
	}
}
int Case;
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		memset(opp,0,sizeof(opp));
		memset(com,0,sizeof(com));
		scanf("%d",&C);
		while(C--)
		{
			scanf("%s",str);
			int x = str[0];
			int y = str[1];
			com[x][y] = str[2];
			com[y][x] = str[2];
		}
		scanf("%d",&D);
		while(D--)
		{
			scanf("%s",str);
			int x = str[0];
			int y = str[1];
			opp[x][y] = opp[y][x] = 1;
		}
		scanf("%d",&N);
		scanf("%s",str);
		solve();
		printf("Case #%d: [",++Case);
		if(size != 0)	printf("%c",S[1]);
		for(int i = 2;i <= size;++i)
			printf(", %c",S[i]);
		printf("]\n");
	}
}