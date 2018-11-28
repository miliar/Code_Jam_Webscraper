#include<stdio.h>
#include<string>
#include<cstring>
using namespace std;

const int MAXN = 110;

char com[MAXN][MAXN];
bool opp[MAXN][MAXN];
char str[MAXN];
int n;

int main()
{
	int test,A,B;
	scanf("%d",&test);
	for (int cas=1;cas<=test;cas++)
	{
		memset(com,0,sizeof(com));
		memset(opp,0,sizeof(opp));
	
		scanf("%d",&A);
		for (int i=0;i<A;i++)
		{
			scanf("%s",str);
			com[ str[0] ][ str[1] ] = str[2];
			com[ str[1] ][ str[0] ] = str[2];
		}
		scanf("%d",&B);
		for (int i=0;i<B;i++)
		{
			scanf("%s",str);
			opp[ str[0] ][ str[1] ] = true;
			opp[ str[1] ][ str[0] ] = true;
		}
		scanf("%d",&n);
		scanf("%s",str);
		
		//printf("str is %s\n",str);
		string now = "";
		for (int j=0;str[j]!=0;j++)
		{
			char ch = str[j];	
			now += ch;
			
			while (now.size() > 1)
			{
				char c1 = now[ now.size()-1 ];
				char c2 = now[ now.size()-2 ];
				if (com[c1][c2] > 0)
				{
					now.erase(--now.end());
					now.erase(--now.end());
					now += com[c1][c2];
				}else
					break;				
			}
			if (now.size() > 1)
			{
				char c = now[ now.size()-1 ];
				for (int k=0;k<now.size();k++)
				if (opp[ now[k] ][c])
				{
					now.clear();
					break;
				}
			}
		}	
		printf("Case #%d: ",cas);
		printf("[");
		for (int i=0;i<now.size();i++)
		{
			if (i < now.size()-1)
				printf("%c, ",now[i]);
			else
				printf("%c",now[i]);
		}
		printf("]\n");
	}
}

