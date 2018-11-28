#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char name[102][103];
int s,q;

int find(char *ss)
{
	int i;
	for(i=0;i<s;i++)
	{
		if(strcmp(name[i],ss)==0)
			return i;
	}	
	abort();
}

int main()
{
	int max,j,maxp;
	int count;
	int seq[1024];
	int next[102];
	char tmp[1024];
	int fuck[1024];
	int cas;
	int asd,i;
	scanf("%d ",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d ",&s);
		for(i=0;i<s;i++)
		{
			gets(name[i]);
		}
		scanf("%d ",&q);
                for(i=0;i<s;i++)
                        next[i] = q;

		for(i=0;i<q;i++)
		{
			gets(tmp);
			seq[i] = find(tmp);
		}
		if(q==0)
		{
			printf("Case #%d: %d\n",asd+1,0);
			continue;
		}
		for(i=q-1;i>=0;i--)
		{
			next[seq[i]] = i; 
			max=-1;
			for(j=0;j<s;j++)
			{
				if(next[j] > max)
				{
					max=next[j];
					maxp=j;
				}
			}
			fuck[i] = max;
		}
		count=0;
		for(i=0;i<q;)
		{
			count++;
			i=fuck[i];
		}
		printf("Case #%d: %d\n",asd+1,count-1);
	}
	return 0;
}
