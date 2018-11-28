#include<iostream>
#include<cstring>
using namespace std;

char s[5001][20];
int l,d,n;
int q[15];

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d%d%d\n",&l,&d,&n);
	for (int i=1;i<=d;i++)
		scanf("%s",s[i]);
	char t[1025];
	for (int i=1;i<=n;i++)
	{
		scanf("%s",t);
		int ans=0;
		int len=strlen(t);
		bool flag=false;
		int num=0;
		memset(q,0,sizeof(q));
		for (int j=0;j<len;j++)
		{
			if (t[j]=='(')
			{
				flag=true;
			}
			else if (t[j]==')')
			{
				flag=false;
				num++;
			}
			else
			{
				q[num]|=1<<(t[j]-'a');
				if (!flag)
					num++;
			}
		}
		for (int j=1;j<=d;j++)
		{
			flag=true;
			for (int k=0;k<l;k++)
				if (((q[k]>>(s[j][k]-'a'))&1)==0)
					flag=false;
			if (flag)
				ans++;
		}
		printf("Case #%d: %d\n",i,ans);
	}
}