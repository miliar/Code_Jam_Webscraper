#include<iostream>
#include<vector>
#include<string>
using namespace std;


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int l,d,n;
	cin>>l>>d>>n;
	vector<string> dict(d);
	for(int i=0;i<d;i++)
		cin>>dict[i];

	for(int i=1;i<=n;i++)
	{
		cout<<"Case #" << i <<": ";

		bool dp[20][128]={0};
		for(int j=0;j<l;j++)
		{
			char c;
			cin>>c;
			if(c=='(')
			{
				while(cin>>c,c!=')')
				{
					dp[j][c]=1;
				}
			}
			else
			{
				dp[j][c]=1;
			}
		}

		int ans=0;
		for(int j=0;j<d;j++)
		{
			bool ok=true;
			for(int k=0;k<l;k++)
			{
				if(dp[k][dict[j][k]]==0)
					ok=false;
			}
			if(ok)ans++;
		}

		cout<<ans<<endl;
	}
}
