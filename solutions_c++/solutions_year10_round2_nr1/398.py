#include<iostream>
#include<string>
#include<map>
using namespace std;
char s[100][1000];
char t[100][1000];
int main()
{
	int T,cs,i,j,n,m,ans;
	string ss;
	freopen("A-Large.in","r",stdin);
	freopen("A-Large.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		map<string,bool>d;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%s",s[i]);
		for(i=0;i<m;i++)
			scanf("%s",t[i]);
		for(i=0;i<n;i++)
		{
			for(j=0;s[i][j];j++)
				if(s[i][j+1]=='/')
				{
					s[i][j+1]=0;
					ss=s[i];
					d[ss]=true;
					s[i][j+1]='/';
				}
			ss=s[i];
			d[ss]=true;
		}
		ans=0;
		for(i=0;i<m;i++)
		{
			for(j=0;t[i][j];j++)
				if(t[i][j+1]=='/')
				{
					t[i][j+1]=0;
					ss=t[i];
					if(d[ss]==false)ans++;
					d[ss]=true;
					t[i][j+1]='/';
				}
			ss=t[i];
			if(d[ss]==false)ans++;
			d[ss]=true;
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}