#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int count[501];
char list[5001][16];
char temp[501][1024];
char temp2[501][1024];
char hash[501][16][26];


int main()
{
	int L,D,K,i,j,k,h;

	scanf("%d%d%d",&L,&D,&K);

		memset(count,0,sizeof(int)*K);
		for(i=0;i<K;i++) memset(hash,0,sizeof(char)16*26);
		for(i=0;i<D;i++) 
			scanf("%s",list[i]);
		for(i=0;i<K;i++) scanf("%s",temp[i]);

		for(i=0;i<K;i++)
		{
			for(j=0,h = 0;temp[i][j]!='\0';j++)
			{
				if(temp[i][j] == '(')
				{
					for(j++;temp[i][j] != ')';j++)
					{
						if(hash[i][h][temp[i][j] - 'a'] == 0)
							hash[i][h][temp[i][j] - 'a']++;
					}
					temp2[i][h] = -(h+1);
					h++;
				}
				else
				{
					temp2[i][h++] = temp[i][j];
				}
			}
		}

		for(i=0;i<D;i++)
		{
			for(j = 0;j<K;j++)
			{
				for(k=0;k<L;k++)
				{
					h = temp2[j][k];
					if(h>0)
					{
						if(list[i][k] != h)
							break;
					}
					else
					{ 
						if(hash[j][-(h+1)][list[i][k]-'a']==0)
							break;
					}
				}
				if(k>=L) count[j]++;
			}
		}

		for(i=0;i<K;i++)
		{
			printf("Case #%d: %d\n",i+1,count[i]);
		}
	return 0;
}

