#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
using namespace std;


int main()
{
	freopen("c1in.txt","r",stdin);
	freopen("c1out.txt","w",stdout);

	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n,k;
		cin>>n>>k;
		vector<int> chart[20];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<k;j++)
			{
				int sb;
				cin>>sb;
				chart[i].push_back(sb);
			}
		}

		//get the graph
		bool con[20][20]={0};
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if(chart[i][0]==chart[j][0])continue;

				bool ok=1;
				for(int kk=0;kk<k;kk++)
				{
					if(
						(chart[i][0]<chart[j][0] && chart[i][kk] >= chart[j][kk])
					||
						(chart[i][0]>chart[j][0] && chart[i][kk] <= chart[j][kk]) )
						ok=false;
				}
				if(ok)
				{
					con[i][j] = con[j][i]=1;
				}
			}
		}

		
		int dp[66666];
		memset(dp,0x7f,sizeof(dp));

		//find clique
		for(int bt=1;bt<(1<<n);bt++)
		{
			int v[20];
			int vi=0;
			for(int j=0;j<n;j++)
			{
				if( bt & (1<<j))
					v[vi++]=j;
			}
			bool ok=1;
			for(int i=0;i<vi;i++)
			{
				for(int j=i+1;j<vi;j++)
				{
					int c1=v[i];
					int c2=v[j];
					if(con[c1][c2]==false)
						ok=false;
				}
			}

			if(ok)dp[bt]=1;
		}

		//begin dp
		for(int bt=1;bt<(1<<n);bt++)
		{
			if(dp[bt]==0x7f7f7f7f)continue;

			int v[20];
			int vi=0;

			for(int j=0;j<n;j++)
			{
				if(bt & (1<<j))continue;

				//pos j is 0
				v[vi++]=j;
			}

			//the rest positions
			for(int bt2=1;bt2<(1<<vi);bt2++)
			{
				int rest=0;
				for(int j=0;j<vi;j++)
				{
					if(bt2&(1<<j))
					{
						rest += (1 << v[j]);
					}
				}
				if(dp[rest]==0x7f7f7f7f)continue;

				if(dp[bt]+dp[rest]<dp[bt+rest])
					dp[bt+rest]=dp[bt]+dp[rest];
			}
		}

		cout << "Case #" << t << ": " << dp[(1<<n)-1] << endl;
	}
}

