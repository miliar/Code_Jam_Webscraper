#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

double per[3][100];
string inp[100];
int n;
double _cnt[100], wincnt[100];

int main(void)
{
	int t;
	cin>>t;
	for(int caseN=1;caseN<=t;caseN++)
	{
		cin>>n;
		for(int i=0;i<n;i++) 
		{
			cin>>inp[i];
			double win=0, cnt=0;

			for(int j=0;j<n;j++)
			{
				if(inp[i][j]!='.') cnt++;
				if(inp[i][j]=='1') win++;
			}

			_cnt[i]=cnt;
			wincnt[i]=win;

			per[0][i]=win/cnt;
		}

		for(int i=1;i<3;i++)
		{
			for(int j=0;j<n;j++)
			{
				double cnt=0;
				double sum=0;

				for(int k=0;k<n;k++)
				{
					if(inp[j][k]!='.')
					{
						cnt++;
						if(i==1) sum+=(wincnt[k]-(inp[j][k]=='1'?0:1))/(_cnt[k]-1);
						else sum+=per[i-1][k];
					}
				}

				per[i][j]=sum/cnt;
			}
		}

		printf("Case #%d:\n", caseN);
		for(int i=0;i<n;i++) printf("%.10lf\n", per[0][i]*.25 + per[1][i]*.5 + per[2][i]*.25);
	}

	return 0;
}
