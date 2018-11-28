#include<iostream>

using namespace std;

int l,d,n;
bool g[20][27];
char s[10000][20];

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d %d %d\n",&l,&d,&n);
	for(int i=1;i<=d;++i)
	{
		scanf("%s\n",s[i]);
	//	puts(s[i]);
	}
	for(int i=1;i<=n;++i)
	{
		int ans=0;
		memset(g,0,sizeof(g));
		for(int j=1;j<=l;++j)
		{
			char c;
			scanf("%c",&c);
			//cout<<c;
			if(c!='(')
				g[j][c-'a']=true;
			else
			{
				for(;;)
				{
					scanf("%c",&c);
				//	cout<<c;
					if(c==')')
						break;
					g[j][c-'a']=true;
				}
			}
		}
	//	puts("");
		scanf("\n");
		for(int j=1;j<=d;++j)
		{
			bool flag=1;
			for(int k=1;k<=l;++k)
				flag&=g[k][s[j][k-1]-'a'];
			ans+=flag;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
