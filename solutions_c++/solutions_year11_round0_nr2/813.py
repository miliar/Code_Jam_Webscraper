#include<iostream>
#include<cstdio>
using namespace std;
int T,c,d,n;
char s[109],a[109],opp[109][3],g[300][300];
bool f[300];

void init()
{
	scanf("%d",&c);		memset(g,0,sizeof(g));
	for (int i=1;i<=c;i++)
	{
		char tmp[5];	scanf("%s",tmp);
		g[tmp[0]][tmp[1]]=g[tmp[1]][tmp[0]]=tmp[2];
	}
	scanf("%d",&d);
	for (int i=1;i<=d;i++)	scanf("%s",opp[i]);
	scanf("%d",&n);	scanf("%s",s+1);
}

void work()
{
	int op=0;	memset(a,0,sizeof(a));
	for (int i=1;i<=n;i++)
	{
		a[++op]=s[i];
		while (op>1 && g[a[op]][a[op-1]]) 
		{
			char tmp=g[a[op]][a[op-1]];	
			a[op-1]=g[a[op]][a[op-1]];	op--;
		}

		memset(f,0,sizeof(f));	for (int i=1;i<=op;i++) f[a[i]]=true;
		for (int i=1;i<=d;i++)	
			if (f[opp[i][0]] && f[opp[i][1]]) 
			{
				op=0;	break;
			}
	}
	for (int i=1;i<op;i++) printf("%c, ",a[i]);	
	if(op) printf("%c",a[op]);	printf("]\n");
}		

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b_l.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		init();
		printf("Case #%d: [",t);
		work();
	}
	return 0;
}


