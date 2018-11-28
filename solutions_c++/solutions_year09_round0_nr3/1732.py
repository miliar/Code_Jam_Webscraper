#include<iostream>
using namespace std;
char s[50009];
int ans[50009];
char p[]="welcome to code jam";
const int M=10000;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c_big_out.txt","w",stdout);
	int n,i,j,k;
	cin>>n;
	getchar();
	int lp=strlen(p);
	for(i=0;i<n;i++)
	{
		gets(s);
		int ls=strlen(s);
		memset(ans,0,sizeof(ans));
		for(j=ls-1;j>=0;j--)
			if(s[j]==p[lp-1])
				ans[j]=1;
			else
				ans[j]=0;
		for(k=lp-2;k>=0;k--)
		{
			int cnt=0;
			for(j=ls-1;j>=0;j--)
			{
				int tmp=ans[j];
				if(s[j]==p[k])
					ans[j]=cnt;
				else
					ans[j]=0;
				if(s[j]==p[k+1])
					cnt=(cnt+tmp)%M;
			}
		}
		int myans=0;
		for(j=ls-1;j>=0;j--)
			myans=(myans+ans[j])%M;
		printf("Case #%d: %.4d\n",i+1,myans);
	}
	//while(3);
}
