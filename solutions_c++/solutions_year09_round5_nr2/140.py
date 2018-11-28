#include <stdio.h>
#include <string>
#include <string.h>
#define M 10009

using namespace std;

string st[200];
int T,t,i,j,k,n,x,l,d[100];
int ch[100];
int a[100],b[100],ans,y,kk;
char str[1000],s[1000];
int cn[100][100];
bool u[100];
int f[]={1,1,2,6,24,120,720,5040};

int po(int x,int k)
{
	int ans=1;
	while(k--)
		ans*=x;
	return ans;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%s",&s);
		l=0;
		memset(u,0,sizeof(u));
		memset(b,0,sizeof(b));
		for(i=0;s[i];i++)
			if(s[i]!='+')
				u[s[i]-'a']=1;
		for(i=0;i<26;i++)
			if(u[i])
				d[l++]=i;
		scanf("%d%d",&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",&str);
			st[i]=str;
		}
		kk=k;
		for(i=0;i<n;i++)
		{
			memset(cn[i],0,sizeof(cn[i]));
			for(j=0;j<st[i].size();j++)
				cn[i][st[i][j]-'a']++;
		}
		while(k)
		{
			memset(a,0,sizeof(a));
			while(1)
			{
				memset(ch,0,sizeof(ch));
				for(i=0;i<k;i++)
					for(j=0;j<l;j++)
						ch[d[j]]+=cn[a[i]][d[j]];
				y=1;
				ans=0;
				for(i=0;s[i];i++)
					if(s[i]=='+')
					{
						ans=(ans+y)%M;
						y=1;
					}
					else
						y=(y*ch[s[i]-'a'])%M;
				ans=(ans+y)%M;
				ans*=f[k];
				y=1;
				for(i=1;i<k;i++)
					if(a[i]==a[i-1])
						y++;
					else
					{
						ans/=f[y];
						y=1;
					}
				ans/=f[y];
				b[k]=(b[k]+ans)%M;
				for(i=k-1;i>=0;i--)
					if(a[i]!=n-1)
						break;
				if(i==-1)
					break;
				a[i]++;
				for(i++;i<k;i++)
					a[i]=a[i-1];
			}
			k--;
		}
		printf("%d",b[1]);
		for(i=2;i<=kk;i++)
			printf(" %d",b[i]);
		printf("\n");
	}
	return 0;
}