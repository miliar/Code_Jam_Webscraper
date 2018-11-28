#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>

#define rep(i,n) for(int i=0;i<n;i++)
#define forr(i,a,b) for(int i=a;i<=b;i++)

#define N 105
#define K 11
#define E 26
#define modul 10009

int t,test;
char s[200],tek[200];
int n,k,kk,m,l,i;
int a[N][E],c[E];
int f[K];
int ans;

void dfs(char d)
{
	if(d==kk)
	{
		int sum=0,cur=1;
		rep(i,m)
		{
			if(s[i]=='+')
			{
				sum=(sum+cur)%modul;
				cur=1;
			}else
			{
				cur=(cur*c[s[i]-'a'])%modul;
			}
		}
		sum=(sum+cur)%modul;
		ans=(ans+sum)%modul;
	}else
	{
		int i,j;
		rep(i,n)
		{
			f[d]=i;
			rep(j,E)
				c[j]+=a[i][j];
			dfs(d+1);
			rep(j,E)
				c[j]-=a[i][j];
		}
	}
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&test);
	forr(t,1,test)
	{
		fprintf(stderr,"%d\n",t);
		scanf("%s",&s);
		scanf("%d",&k);
		m=strlen(s);
		scanf("%d",&n);
		getchar();
		memset(a,0,sizeof(a));
		memset(c,0,sizeof(c));
		rep(i,n)
		{
			scanf("%s",&tek);
			getchar();
			l=strlen(tek);
			rep(j,l)
				a[i][tek[j]-'a']++;
		}
		printf("Case #%d:",t);
		for(kk=1;kk<=k;kk++)
		{
			ans=0;
			dfs(0);
			printf(" %d",ans);
		}
		printf("\n");
	}
    return 0;
}
