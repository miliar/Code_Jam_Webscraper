#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int Com[30][30];
int Opp[30][30];
char str[110];
char combine[4];
char res[110];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Bsmall.out","w",stdout);
	int T,C,D,N,t=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&C);
		memset(Com,-1,sizeof(Com));
		for(int i=0;i<C;i++)
		{
			scanf("%s",combine);
			int a=combine[0]-'A';
			int b=combine[1]-'A';
			int c=combine[2]-'A';
			Com[a][b]=Com[b][a]=c;
		}
		scanf("%d",&D);
		memset(Opp,0,sizeof(Opp));
		for(int i=0;i<D;i++)
		{
			scanf("%s",combine);
			int a=combine[0]-'A';
			int b=combine[1]-'A';
			Opp[a][b]=Opp[b][a]=1;
		}
		scanf("%d",&N);
		scanf("%s",str);
		int j=0;
		for(int i=0;i<N;i++)
		{
			res[j++]=str[i];

			if(j>1&&Com[res[j-2]-'A'][str[i]-'A']!=-1)
			{
				res[j-2]=Com[res[j-2]-'A'][str[i]-'A']+'A';
				j--;
			}
			else 
			{
				for(int k=0;k<j-1;k++)
					if(Opp[res[k]-'A'][str[i]-'A'])
					{
						j=0;		
						break;
					}
			}
		}
		printf("Case #%d: [",t++);
		for(int i=0;i<j-1;i++)
			printf("%c, ",res[i]);
		if(j>0)
			printf("%c",res[j-1]);
		printf("]\n");
	}
	return 0;
}
