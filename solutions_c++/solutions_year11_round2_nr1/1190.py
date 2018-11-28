#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T(0);
	cin >> T;
	for(int t(0);t < T; ++t)
	{
		int N(0);
		cin >> N;
		vector<vector<pair<int, int> > > g(N);
		vector<double> WP(N, 0.0);
		vector<double> OWP(N, 0.0);
		vector<double> OOWP(N, 0.0);
		vector<string> base(N);
		for(int i(0); i < N; ++i)
		{
			cin >> base[i];
			for(int j(0); j < N; ++j)
			{
				
				if(base[i][j] != '.')
				{
					g[i].push_back(make_pair(j,base[i][j] - '0'));
					if(base[i][j] == '1')
					{
						WP[i]++;
					}
				}
			}
		}
		for(int i(0); i < N; ++i)
		{
			for(int j(0); j < g[i].size(); ++j)
			{

				if(g[i][j].second == 0)
					OWP[i] += ((WP[g[i][j].first] - 1) / (g[g[i][j].first].size() - 1));
				else
					OWP[i] += ((WP[g[i][j].first] - 0) / (g[g[i][j].first].size() - 1));
			}
			OWP[i] /= g[i].size();
		}
		
		for(int i(0); i < N; ++i)
		{
			for(int j(0); j < g[i].size(); ++j)
			{
					OOWP[i] += OWP[g[i][j].first];				
			}
			OOWP[i] /= g[i].size();
			WP[i] /= g[i].size();
		}
		cout << "Case #" << t + 1 << ":" << endl;
		for(int i(0); i < N; ++i)
			cout << fixed << setprecision(8) << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] << endl; 
	}
	return 0;
}