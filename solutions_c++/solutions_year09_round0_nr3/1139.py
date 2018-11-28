#include <stdio.h>
#include <string>
using namespace std;

string str="welcome to code jam";

int dp[505][30];
string inp;
int go(int a, int b)
{
	if (a==inp.length())
		return 0;
	if (b+1==str.length())
		return 1;
	int &ans=dp[a][b];
	if (ans!=-1)
		return ans;
	ans=0;
	int i;
	for (i=a+1; i<inp.length(); i++)
	{
		if (inp[i]==str[b+1]) {
			ans+=go(i,b+1);
			ans=ans%10000;
		}
	}
	return ans;
}

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0x.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out2","w",stdout);
	int T,t;
	char data[1000];
	scanf("%d", &T); gets(data);
	for (t=1; t<=T; t++)
	{
		int i;
		gets(data);
		inp=data;
		memset(dp,-1,sizeof(dp));
		int ans=0;
		for (i=0; i<inp.length(); i++)
			if (inp[i]==str[0]) {
				ans+=go(i,0);
				ans=ans%10000;
			}
		printf("Case #%d: %04d\n",t,ans);
	}
	return 0;
}