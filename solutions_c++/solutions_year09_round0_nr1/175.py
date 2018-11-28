#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;

char s[5005][20],t[2000];

int main()
{
	int l,d,n,c,i,j,k;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",s[i]);
	for(c=1;c<=n;c++)
	{
		scanf("%s",t);
		int ans=0;
		for(i=0;i<d;i++)
		{
			k=0;
			for(j=0;j<l;j++)
			{
				bool f[26]={0};
				if(t[k]=='(')
				{
					k++;
					while(t[k]!=')')
						f[t[k]-'a']=1,k++;
					k++;
				}
				else
					f[t[k++]-'a']=1;
				if(!f[s[i][j]-'a'])
					break;
			}
			if(j==l)
				ans++;
		}
		printf("Case #%d: %d\n",c,ans);
	}
}