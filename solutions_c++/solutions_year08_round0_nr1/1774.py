#include<iostream>
#include<string>
using namespace std;

string ss[105],qq[1005];
int dp[1005][105] = {0};

int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int cas,ca=1;
	cin>>cas;
	while(cas--)
	{
		char c[1005];
		int i,j,k,s,q,_max;
		cin>>s;
		scanf("%c",c);
		for(i=0;i<s;i++)
		{
			gets(c);
			ss[i] = c;
		}
		cin>>q;
		scanf("%c",c);
		for(i=0;i<q;i++)
		{
			gets(c);
			qq[i] = c;
		}
		memset(dp,0,sizeof(dp));
		for(i=q-1;i>=0;i--)  //当前字串
			for(j=0;j<s;j++)  //选J器务器
			{
				if( qq[i]!=ss[j])
					dp[i][j] = dp[i+1][j];
				else
				{
					_max = 105;
					for(k=0;k<s;k++)
					{
						if(k==j)
							continue;
						else if( _max > dp[i+1][k] + 1)
							_max = dp[i+1][k]+1;
					}
					dp[i][j] = _max;
				}
			}
		_max = 105;
		for(i=0;i<s;i++)
			if(dp[0][i]<_max)
				_max = dp[0][i];
		printf("Case #%d: %d\n",ca++,_max);
	}
	return 0;
}