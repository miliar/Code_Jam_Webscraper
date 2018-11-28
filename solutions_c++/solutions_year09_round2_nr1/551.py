#include<cstdio>
#include<cstring>

int m,n;
char a[1000000];
char b[1000][1000];

void process()
{
	char trash[1000];
	for(int i=0;i<m;i++)
	{
		double score=1;
		scanf("%s",trash);
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			scanf("%s",b[j]);
		}
		char *c=a;
		while(*c!='(') c++;
		c++;
		while(1)
		{
			double p;
			int j;
			sscanf(c,"%lf",&p);
			score*=p;
			while(((*c<'a')||(*c>'z'))&&(*c!=')')) c++;
			if(*c==')') break;
			for(j=0;j<n;j++)
			{
				int k;
				for(k=0;k<strlen(b[j]);k++)
				{
					if(c[k]!=b[j][k]) break;
				}
				if(k>=strlen(b[j])&&(c[k]<'a'||c[k]>'z')) break;
			}
			if(j<n)
			{
				int sp=1;
				while(sp)
				{
					if(*c=='(') sp--;
					else if(*c==')') sp++;
					c++;
				}
			}
			else
			{
				int sp=1;
				while(sp)
				{
					if(*c=='(') sp--;
					else if(*c==')') sp++;
					c++;
				}
				sp=-1;
				while(sp)
				{
					if(*c=='(') sp--;
					else if(*c==')') sp++;
					c++;
				}
				sp=1;
				while(sp)
				{
					if(*c=='(') sp--;
					else if(*c==')') sp++;
					c++;
				}
			}
		}
		printf("%.7lf\n",score);
	}
}

void input()
{
	int n,i;
	scanf("%d\n",&n);
	a[0]=0;
	for(i=0;i<n;i++)
	{
		gets(a+strlen(a));
		a[strlen(a)+1]=0;
		a[strlen(a)]=' ';
	}
	scanf("%d\n",&m);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		input();
		printf("Case #%d:\n",i+1);
		process();
	}
}