#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
	int T,t,L,cnt[10],i,j;
	char s[21],ss[21];
	//freopen("B-large.in","r",stdin);
	//freopen("B.txt","w",stdout);
	scanf("%d",&T);
	for(t = 1;t <= T;t++)
	{
		scanf("%s",s);
		printf("Case #%d: ",t);
		L = strlen(s);
		for(i = 0;i < L - 1;i++)
		{
			if(s[i] < s[i + 1])
				break;
		}
		if(i == L - 1)
		{
			int min = 10;
			memset(cnt,0,sizeof(cnt));
			for(i = 0;i < L;i++)
			{
				if(s[i] != '0' && s[i] - '0' < min)
					min = s[i] - '0';
				cnt[s[i] - '0']++;
			}
			cnt[min]--;
			printf("%d0",min);
			for(i = 0;i < 10;i++)
				for(j = 0;j < cnt[i];j++)
					printf("%d",i);
			printf("\n");
		}
		else
		{
			do
			{
				next_permutation(s,s + L);
			}while(s[0] == '0');
			puts(s);
		}
	}
	//system("PAUSE");
	return 0;
}
			
			
				
