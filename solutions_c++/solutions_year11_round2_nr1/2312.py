#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve()
{
	int teamscnt;
	cin >> teamscnt;
	vector<string> sched(teamscnt);
	int i, j, k;
	vector<int> wins(teamscnt), totalgames(teamscnt);
	for( i = 0; i < teamscnt; ++i )
	{
		cin >> sched[i];
		wins[i] = 0;
		totalgames[i] = 0;
		for( k = 0; k < sched[i].size(); ++k )
			if( sched[i][k] != '.' ) {
				++totalgames[i];
				if( sched[i][k] == '1' )
					++wins[i];
			}
	}
	vector<double> wp(teamscnt), owp(teamscnt), oowp(teamscnt);
	for( i = 0; i < teamscnt; ++i )
	{
		wp[i] = double(wins[i]) / totalgames[i];
		owp[i] = 0;
		for( j = 0; j < teamscnt; ++j )
		{
			if( sched[i][j] != '.' )
				owp[i] += double(wins[j] - (sched[j][i] - '0')) / (totalgames[j] - 1);
		}
		owp[i] /= totalgames[i];
	}
	for( i = 0; i < teamscnt; ++i )
	{
		oowp[i] = 0;
		for( j = 0; j < teamscnt; ++j )
		{
			if( sched[i][j] != '.' )
				oowp[i] += owp[j];
		}
		oowp[i] /= totalgames[i];
	}
	for( i = 0; i < teamscnt; ++i )
		cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int testscnt;
	cin >> testscnt;
	for( int t = 1; t <= testscnt; ++t )
	{
		cout << "Case #" << t << ":" << endl;
		solve();
	}
	return 0;
}