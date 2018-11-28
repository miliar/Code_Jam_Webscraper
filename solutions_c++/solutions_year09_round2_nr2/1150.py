#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;

int main()
{
	int i,kase=1,test,l,flag = 0;
	char n[35];
	freopen("b.txt","r",stdin);
	freopen("c.txt","w",stdout);
	scanf("%d",&test);
	while(test--)
	{
		scanf(" %s",&n);
		l = strlen(n);
		flag = 0;
		if(n[l-1]=='0')flag = 1;
		if(next_permutation(n,n+l) == true)
		{
			printf("Case #%d: %s\n",kase++,n);		
		}
		else
		{
			printf("Case #%d: ",kase++);
			if(flag)
			{
				sort(n,n+l);
				for(i=0;i<l;i++)
				{
					if(n[i]> '0')
					{
						printf("%c",n[i]);
						n[i] = '*';break;
					}
				}
				printf("0");
				for(i=0;i<l;i++)
				{
					if(n[i] != '*')
					{
						printf("%c",n[i]);
					}
				}
			}
			else
			{
				printf("%c0",n[0]);
				for(i=1;i<l;i++)
					printf("%c",n[i]);
			}
			printf("\n");
		}
		
	}
	return 0;
}