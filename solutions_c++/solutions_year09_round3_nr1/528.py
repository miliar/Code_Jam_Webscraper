#include<iostream>

using namespace std;

int num[10],c[26],t,maxnum,l,;
char s[100];
long long ans,p,d[100];

/*
struct bignum
{
	int d[10000],h;
}g[100],ans,p;*/

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	for(int k=1;k<=t;++k)
	{
		memset(num,-1,sizeof(num));
		memset(c,-1,sizeof(c));
		scanf("%s",s);
		l=strlen(s);
		if(s[0]>='0'&&s[0]<='9')
			d[0]=num[s[0]-'0']=1;
		else
			d[0]=c[s[0]-'a']=1;
		maxnum=1;
		bool flag=true;
		for(int i=1;i<l;++i)
		{
			if(s[i]>='0'&&s[i]<='9')
			{
				if(num[s[i]-'0']==-1)
					if(flag)
						flag=num[s[i]-'0']=0;
					else
						num[s[i]-'0']=++maxnum;
				d[i]=num[s[i]-'0'];
			}
			else
			{
				if(c[s[i]-'a']==-1)
					if(flag)
						flag=c[s[i]-'a']=0;
					else
						c[s[i]-'a']=++maxnum;
				d[i]=c[s[i]-'a'];
			}
		}
		++maxnum;
		p=1;
		ans=0;
		for(int i=l-1;i>=0;--i)
		{
			ans+=p*d[i];
			p*=maxnum;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
/*
		for(int i=l-1;i>=0;--i)
			if(s[i]>='0'&&s[i]<='9')
			{
				g[i].b[1]=num[s[0]-'0'];
				h=1;
				if(g[i].b[1]>9)
				{
					h=2;
					g[i].b[2]=g[i].b[1]/10;
					g[i].b[1]%=10;
				}
			}
			else
			{
				g[i].b[1]=c[s[0]-'0'];
				h=1;
				if(g[i].b[1]>9)
				{
					h=2;
					g[i].b[2]=g[i].b[1]/10;
					g[i].b[1]%=10;
				}
			}
		p.d[1]=1;
		p.h=1;
		*/
	}
	return 0;
}
