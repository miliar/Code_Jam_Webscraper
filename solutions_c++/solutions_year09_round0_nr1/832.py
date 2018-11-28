#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int l,n;
char d[5010][19],s[999];
bool a[19][30];
int main()
{
	int _;
	scanf("%d%d%d",&l,&n,&_);
	for(int i=0; i<n; i++)
		scanf("%s",d[i]);
	for(int t=1; t<=_; t++)
	{
		scanf("%s",s);
		memset(a,0,sizeof(a));
		for(int j=0,k=0; s[j]; )
			if(s[j]=='(')
			{
				for(j++; s[j]!=')'; j++)
					a[k][s[j]-'a']=true;
				j++,k++;
			}
			else
				a[k++][s[j++]-'a']=true;
		int ans=0;
		for(int i=0; i<n; i++)
		{
			bool flag=true;
			for(int j=0; j<l&&flag; j++)
				flag&=a[j][d[i][j]-'a'];
			if(flag)
				ans++;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
