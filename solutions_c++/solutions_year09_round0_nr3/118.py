#include <iostream>
using namespace std;

int n;
char s[600];
int num[600];
char str[]="welcome to code jam";

int main()
{
	FILE *fp=freopen("out.txt","w",stdout);
	scanf("%d",&n);
	int i,j,k,l;getchar();
	for(i=1;i<=n;i++)
	{
		gets(s);
		//l=strlen(s);
		for(j=0;s[j];j++)
			if(s[j]=='w') num[j]=1;
			else num[j]=0;
		int ans=0;
		for(j=1;j<=18;j++)
		{
			for(k=0;s[k]!=0;k++) if(s[k]==str[j])
			{
				num[k]=0;
				for(l=0;l<k;l++) if(s[l]==str[j-1])
				{
					num[k]+=num[l];
					num[k]%=10000;
				}
				if(j==18) 
				{
					ans+=num[k];ans%=10000;
				}
			}
		}
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}