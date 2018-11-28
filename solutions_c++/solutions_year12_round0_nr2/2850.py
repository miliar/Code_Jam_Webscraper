#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;



int main()
{
	ifstream in("large.in");
	ofstream out("large.out");

	

	int T;
	in>>T;

	
	for ( int i = 1; i <= T; i++)
	{
		int f[120][120];
		int t[120];
		int n, s, p;
		in>>n>>s>>p;

		for (int j = 1; j <= n; j++)
		{
			in>>t[j];
		}

		f[0][0] = 0;

		for ( int j = 1; j <= n; j++)
		{
			int up = j > s ? s : j;
			int normal;
			int surp;
			int mod = t[j] % 3;

			if (t[j] == 0)
			{
				normal = 0;
				surp = -100;
			}
			else
			{

				
				if (mod == 0)
				{
					normal = t[j]/3;
					surp = normal + 1;
				}
				else if (mod == 1)
				{
					normal = t[j]/3 + 1;
					surp = normal;
				}
				else if (mod == 2)
				{
					normal = t[j]/3 + 1;
					surp = normal + 1;
				}
			}

			for ( int k = 0; k <= up; k++)
			{
				

				
					int maxn, maxs;
					if (k > j-1)  maxn = -1;
					else
					{
						if (normal >= p) maxn = f[j-1][k] + 1;
						else maxn = f[j-1][k];
					}

					if ( k == 0) maxs = -1;
					else if (surp >= p) maxs = f[j-1][k-1] + 1;
					else maxs = f[j-1][k-1];

					f[j][k] = maxn > maxs ? maxn : maxs;



				
			}
		}

		int ans = 0;
		ans = f[n][s] > ans ? f[n][s] : ans;
		out<<"Case #"<<i<<": "<<ans<<endl;
	}
}