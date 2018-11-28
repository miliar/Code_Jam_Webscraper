#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define MAXN 510
#define MAXL 20
#define MAXD 5010

int L,D,N,ans[MAXN];
char word[MAXD][MAXL];
bool pat[MAXN][MAXL][30];

void run()
{
	int i,j,k;
	bool flag;
	for (i=1;i<=D;i++)
		for (j=1;j<=N;j++)
		{
			flag=true;
			for (k=0;k<L;k++)
				if (!pat[j][k][word[i][k]-'a'])
				{
					flag=false;
					break;
				}
			if (flag)
				ans[j]++;
		}
}

void ini()
{
	int i,k;
	char c;
	scanf("%d%d%d",&L,&D,&N);
	for (i=1;i<=D;i++)
	{
		scanf("\n%s",word[i]);
	}
	for (i=1;i<=N;i++)
	{
		scanf("\n");
		for (k=0;k<L;k++)
		{
			scanf("%c",&c);
			if (c=='(')
				while (true)
				{
					scanf("%c",&c);
					if (c==')')
						break;
					else
						pat[i][k][c-'a']=true;
				}
			else
				pat[i][k][c-'a']=true;
		}
	}
}

int main()
{
 	freopen("A-large.in","r",stdin);
 	freopen("A-large.out","w",stdout);
 	ini();
 	run();
 	for (int i=1;i<=N;i++)
 	{
	 	//Case #X: K
	 	printf("Case #%d: %d\n",i,ans[i]); 
	}
	return 0;
}
