#include<iostream>
using namespace std;
#include<string.h>
int flag;	
int hash[10];
int n;
int m;
char ans[100];
int tt=0;
char s[1000];
void dfs(char *p,int a)
{
	int i;
	if(a==n)
	{
		p[a]='\0';
		if(strcmp(s,p)==-1)
		{
			if(flag==-1)
			{
				strcpy(ans,p);
				flag=1;
			}
			else
			{
				if(strcmp(ans,p)==1)
				{
					strcpy(ans,p);
				}
			}
		}
		return ;
	}
	for(i=0;i<10;i++)
	{
		if(hash[i]>0)
		{
			hash[i]--;
			p[a]=i+'0';
			dfs(p,a+1);
			hash[i]++;
		}
	}
	return ;
}
char aa[501][30];
int main()
{
	int t;
	int i,j;


	//	freopen("B-small-attempt0.in","r",stdin);
	//	freopen("out.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		tt++;

		scanf("%s",&s);
		printf("Case #%d: ",tt);
		
		memset(hash,0,sizeof(hash));

		for(i=0;s[i]!='\0';i++)
			hash[s[i]-'0']++;
		n=strlen(s);
		flag=-1;


		char st[100];
		dfs(st,0);

		if(flag!=-1)
		{
	
			puts(ans);
		//	strcpy(aa[tt],ans);
		}
		else
		{
			char hh[1000];
			for(i=1;i<=9;i++)
			{
				if(hash[i]!=0)
				{
					hash[i]--;
					hh[0]=i+'0';
					break;
				}
			}
			hh[1]='0';
			m=2;
			for(i=0;i<=9;i++)
			{
				while(hash[i]>0)
				{
					hash[i]--;
					hh[m]=i+'0';
					m++;
				}
			}
			hh[m]='\0';
			puts(hh);
			//strcpy(aa[tt],hh);
		}
	}
}


