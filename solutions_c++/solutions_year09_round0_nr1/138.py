#include<cstdio>
#include<cstring>

int l,d,n,count[20];
char s[5005][20];
bool b[20][50];
int main()
{
	freopen("alien.in","r",stdin);
	freopen("alien.out","w",stdout);
	scanf("%d%d%d\n",&l,&d,&n);
	for (int i=1;i<=d;++i) gets(s[i]);
	int cnt=1;
	for (int i=1;i<=n;++i,++cnt)
	{
		int len=0;
		memset(count,0,sizeof(count));
		memset(b,false,sizeof(b));
		char ch;
		bool stop=false,inb=false;
		for (scanf("%c",&ch);ch!='\n';scanf("%c",&ch))
		if (!stop)
		{
			if (ch=='(')
			{		
				++len;inb=true;
				if (len>l) stop=true;	
			}
			else if (ch==')') inb=false;
			else 
			{
				if (!inb) ++len;
				b[len][ch-'a']=true;
			}
		}
		if (len!=l) printf("Case #%d: %d\n",cnt,0);
		else 
		{
			int ans=0;
			for (int i=1;i<=d;++i)
			{
				bool ok=true;
				for (int j=1;j<=l && ok;++j)
				if (!b[j][s[i][j-1]-'a']) ok=false;
				if (ok) ++ans;
			}
			printf("Case #%d: %d\n",cnt,ans);
		}
	};
	return 0;
}
