#include <cstdio>

int dic[5000][15];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int l,d,n,ans;
	scanf("%d%d%d",&l,&d,&n);
	char buf[1000];
	for(int i=0;i<d;i++)
	{
		scanf("%s",buf);
		for(int j=0;j<l;j++)
			dic[i][j]=(1<<(buf[j]-'a'));
	}
	for(int T=1;T<=n;T++)
	{
		scanf("%s",buf);
		ans=0;
		int k=0,q[15]={0};
		for(int j=0;j<l;j++)
			if(buf[k]=='(')
			{
				++k;
				while(buf[k]!=')')
					q[j]|=(1<<(buf[k++]-'a'));
				++k;
			}
			else
				q[j]=(1<<(buf[k++]-'a'));
		for(int i=0;i<d;i++)
		{
			for(k=0;k<l;k++)
				if(!(dic[i][k]&q[k]))
					break;
			if(k>=l)
				ans++;
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}
