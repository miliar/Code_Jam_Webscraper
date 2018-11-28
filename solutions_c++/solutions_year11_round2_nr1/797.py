
#include <algorithm>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 



int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	string str;
	getline(cin, str);
	T = atoi(str.c_str());

	REP(t, T)
	{
		string str;
		getline(cin, str);

		int N;
		sscanf(str.c_str(), "%d", &N);

		VS vs;

		REP(i, N)
		{
			string str;
			getline(cin, str);

			vs.push_back(str);
		}

		VI wins(N);
		VI total(N);

		REP(i, N)
		{
			REP(j, N)
			{
				if (vs[i][j] != '.')
					total[i]++;

				if (vs[i][j] == '1')
					wins[i]++;
			}
		}


		vector<double> WP(N);

		REP(i, N)
		{
			WP[i] = (double)wins[i]/total[i];
		}


		vector<double> OWP(N);

		REP(i, N)
		{
			double sum_WPo = 0;
			vector<double> sumWPO_;
			REP(o, N)
			{
				if (i == o)
					continue;

				if (vs[i][o] == '.')
					continue;

				int total=0, wins = 0;
				REP(g, N)
				{
					if (g == i)
						continue;

					if (vs[o][g] != '.')
						total++;

					if (vs[o][g] == '1')
						wins++;
				}

				double WPo = (double)wins/total;
				
				sumWPO_.push_back(WPo);

				sum_WPo += WPo;
			}

			double owp = sum_WPo / sumWPO_.size();

			OWP[i] = owp;
		}


		vector<double> OOWP(N);

		REP(i, N)
		{
			double sum_WPo = 0;
			int cnt=0;
			REP(o, N)
			{
				if (i == o)
					continue;

				if (vs[i][o] == '.')
					continue;

				sum_WPo += OWP[o];
				cnt++;
			}

			double oowp = sum_WPo / cnt;

			OOWP[i] = oowp;
		}

		vector<double> RPI(N);

		REP(i, N)
		{
			RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		}

		cout << "Case #" << (t+1) << ":\n";

		REP(i, N)
		{
			char buf[0xff]={0};
			sprintf(buf, "%.8f", RPI[i]);
			string s(buf);
			cout << s << "\n";
		}

		cout << "\n";



	}


	int Int;
	std::cin >> Int;
}