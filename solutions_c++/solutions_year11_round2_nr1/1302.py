#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
#define N 110

struct data
{
	string s;
	int v;
	bool operator < (const data &t)const
	{
		return v>t.v;
	}
};

char map[N][N];
int n,t;

int win[N];
int total[N];

vector <int> op[N];

int main()
{
	freopen("F:\\DownLoad\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	scanf("%d",&t);
	for ( int c = 1; c <= t; c++ )
	{
		memset(map,0,sizeof(map));
		memset(win,0,sizeof(win));
		memset(total,0,sizeof(total));

		double wp[N]={0};
		double owp[N]={0};
		double oowp[N]={0};

		for ( int i = 0; i < N; i++ )
			op[i].clear();
		scanf("%d",&n);
		for ( int i = 0; i < n; i++ )
			scanf("%s",map[i]);
		for ( int i = 0; i < n; i++ )
		{
			for ( int j = 0; j < n; j++ )
			{
				if ( map[i][j]=='1' )
				{
					op[i].push_back(j);
					win[i]++;
					total[i]++;
				}
				else
					if ( map[i][j]=='0' )
					{
						op[i].push_back(j);
						total[i]++;
					}
			}
		}

		for ( int i = 0; i < n; i++ )
			wp[i] = (double)win[i]/total[i];

		for ( int i = 0; i < n; i++ )
		{
			for ( int j = 0; j < op[i].size(); j++ )
			{
				int k = op[i][j];
				if ( map[i][k]=='1' )
					owp[i] += (double)win[k]/(total[k]-1);
				else if ( map[i][k]=='0' )
					owp[i] += (double)(win[k]-1)/(total[k]-1);
			}
			owp[i] /= op[i].size();
			//printf("%f\n",owp[i]);
		}
		for ( int i = 0; i < n; i++ )
		{
			for ( int j = 0; j < op[i].size(); j++ )
			{
				int k = op[i][j];
				oowp[i] += owp[k];
			}
			oowp[i] /= op[i].size();
		}
		printf("Case #%d:\n",c);
		for ( int i = 0; i < n; i++ )
		{
			printf("%lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}
}