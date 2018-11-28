#include <stdio.h>
#include <string.h>

char path[10001][301];
int n,m,total;

void read()
{
	int i;
	scanf("%d %d\n",&n,&m);
	for(i=0;i<n;i++)
		scanf("%s",&path[i]);
	total = 0;
}

bool find(char *str)
{
	int i;
	for(i=0;i<n;i++)
		if(!strcmp(str,path[i]))
			return true;
	strcpy(path[n++],str);
	return false;
}

void solve()
{
	int i;
	char np[101],*p,sp[]="/",aux[301];
	for(i=0;i<m;i++)
	{
		scanf("%s\n",np);
		p = strtok(np,sp);
		strcpy(aux,"/");
		while(p)
		{
			strcat(aux,p);
			if(!find(aux))
				total++;
			p = strtok(NULL,sp);
			strcat(aux,"/");
		}
	}
}

int main()
{
	int t,i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&t);
	for(i=1;i<=t;i++)
	{
		read();
		solve();
		printf("Case #%d: %d\n",i,total);
	}
	return 0;
}
