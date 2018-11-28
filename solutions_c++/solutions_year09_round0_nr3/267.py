#include<iostream>
#include<string>
using namespace std;

const char t[25]="welcome to code jam";
string s;
int l1,l2;
int dp[1000][30];
bool used[1000][30];

int dfs(int p1,int p2)
{
	if (used[p1][p2]) return dp[p1][p2];
	if (p2>p1) return 0;
	if (p2==0) return 1;

	used[p1][p2]=true;
	dp[p1][p2]=0;
	int i;
	for (i=1;i<=p1;i++)
		if (s[p1-i]==t[p2-1]) dp[p1][p2]=(dp[p1][p2]+dfs(p1-i,p2-1))%10000;
	return dp[p1][p2];
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);

	int tt,tc;

	cin>>tc;
	int i,j;

	l2=strlen(t);

	getline(cin,s);

	for (tt=1;tt<=tc;tt++)
	{
		getline(cin,s);
		l1=s.length();
		memset(used,0,sizeof(used));
		int ans=dfs(l1,l2);

		printf("Case #%d: ",tt);
		if (ans<1000) cout<<0;
		if (ans<100) cout<<0;
		if (ans<10) cout<<0;
		cout<<ans<<endl;
	}
}
