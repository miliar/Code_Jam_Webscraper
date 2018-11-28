#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

int L,D,N;
bool use[15][26];

struct WORD
{
	char s[20];
}w[1 << 13];

int main()
{
	int i,j,k,cnt;
	char str[1 << 10];
	//freopen("1.txt","w",stdout);
	//freopen("A-large.in","r",stdin);
	scanf("%d%d%d",&L,&D,&N);
	for(i = 0;i < D;i++)
		scanf("%s",w[i].s);
	for(i = 1;i <= N;i++)
	{
		scanf("%s",str);
		memset(use,false,sizeof(use));
		for(j = k = 0;str[j];)
		{
			if(str[j] == '(')
			{
				for(j++;str[j] != ')';j++)
					use[k][str[j] - 'a'] = true;
				j++;
			}
			else
				use[k][str[j] - 'a'] = true,j++;
			k++;
		}
		cnt = 0;
		for(j = 0;j < D;j++)
		{
			for(k = 0;k < L;k++)
			{
				if(!use[k][w[j].s[k] - 'a'])
					break;
			}
			if(k == L)
				cnt++;
		}
		printf("Case #%d: %d\n",i,cnt);
	}
	//system("PAUSE");
	return 0;
}
			
		
