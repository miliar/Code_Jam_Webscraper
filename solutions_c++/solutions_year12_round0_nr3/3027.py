#include<cstdio>
#include<map>
#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;
int a,b;
char c[10];
void to_char(int a)
{
	int i=0;
	while(a>0)
	{
		c[i++]=a%10+'0';
		a/=10;
	}
	c[i]='\0';
	reverse(c,c+strlen(c));
}
void solve()
{
	scanf("%d%d",&a,&b);
	int ans=0;
	for(int t=a;t<=b;t++)
	{
		to_char(t);
		int len=strlen(c);
		map<int,int> M;
		for(int i=0;i<len;i++)
		{
		
			int tmp;
			sscanf(c,"%d",&tmp);
			if(M[tmp]==0)
			{
				M[tmp]=1;
				if(tmp<t&&tmp>=a)
				{
					//printf("%d %d\n",t,tmp);
					ans++;
				}
			}
			char tc=c[0];
			for(int j=0;j<len-1;j++)
			c[j]=c[j+1];
			c[len-1]=tc;
		}
	}
	printf("%d\n",ans);
}
int main()
{
	int ca;
	freopen("F:\\TDDOWNLOAD\\C-small-attempt0.in","r",stdin);
	freopen("tmp.txt","w",stdout);
	scanf("%d",&ca);
	for(int ii=1;ii<=ca;ii++)
	{
		printf("Case #%d: ",ii);
		solve();
	}
	return 0;
}
