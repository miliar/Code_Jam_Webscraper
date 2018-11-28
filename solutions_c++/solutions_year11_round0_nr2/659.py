#include <cstdio>
using namespace std;
int test,n,top;
char com['Z'+1]['Z'+1],s[105],list[105];
bool opp['Z'+1]['Z'+1];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		for (char i='A';i<='Z';i++)
		for (char j='A';j<='Z';j++)
		{
			com[i][j]=' ';
			opp[i][j]=0;
		}
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",s);
			com[s[0]][s[1]]=com[s[1]][s[0]]=s[2];
		}
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",s);
			opp[s[0]][s[1]]=opp[s[1]][s[0]]=1;
		}
		scanf("%d",&n);
		scanf("%s",s);
		top=0;
		for (int i=0;i<n;i++)
		{
			list[++top]=s[i];
			if (top>1&&com[list[top-1]][list[top]]!=' ') list[top-1]=com[list[top-1]][list[top]],top--; else
			for (int j=1;j<top;j++)
			if (opp[s[i]][list[j]])
			{
				top=0;
				break;
			}
		}
		printf("Case #%d: [",kase);
		if (top)
		{
			for (int i=1;i<top;i++)
				printf("%c, ",list[i]);
			printf("%c",list[top]);
		}
		printf("]\n");
	}
	
	return 0;
}
