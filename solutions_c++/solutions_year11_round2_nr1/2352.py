#include <iostream>
#include <boost/rational.hpp>
using namespace std;
using namespace boost;

struct info {
    int game_n;
    int win_n;
};

enum score { NON , WIN , LOSS };

score sche[100][100];
info teams[100];
int team_n;
rational<int> WPs[100];
rational<int> OPs[100];
rational<int> OPPs[100];

void read_and_initialize()
{
    int n;cin >> n;
    team_n = n;
    for(int i=0;i<team_n;++i)
    {
	int valid_games = 0;
	int wins = 0;
	for(int j=0;j<team_n;++j)
	{
	    char c;cin >> c;
	    sche[i][j] = (c == '1' ? WIN : (c == '0' ? LOSS : NON));

	    if(i == j)
		assert(sche[i][j] == NON);

	    if(sche[i][j] != NON)++valid_games;
	    if(sche[i][j] == WIN)++wins;
	}
	teams[i] = {valid_games,wins};
	rational<int> denom(valid_games);
	rational<int> nume(wins);
	WPs[i] = (nume / denom);
    }
}

void calc_OPs()
{
    for(int i=0;i<team_n;++i)
    {
	rational<int> acc(0);
	for(int j=0;j<team_n;++j)
	{
	    if(sche[i][j]==NON)continue;
	    rational<int> denom(teams[j].game_n - 1);
	    rational<int> nume(teams[j].win_n - (sche[j][i] == WIN));
	    acc += (nume / denom);
	}
	OPs[i] = (acc / rational<int>(teams[i].game_n));
    }
}

void calc_OPPs()
{
    for(int i=0;i<team_n;++i)
    {
	rational<int> acc(0);
	for(int j=0;j<team_n;++j)
	{
	    if(sche[i][j]==NON)continue;
	    acc += OPs[j];
	}
	OPPs[i] = (acc / rational<int>(teams[i].game_n));
    }
}

void output(int i)
{
    rational<int> qual = rational<int>(1) / rational<int>(4);
    rational<int> half = rational<int>(1) / rational<int>(2);

    rational<int> acc(0);
    acc += qual * WPs[i];
    acc += half * OPs[i];
    acc += qual * OPPs[i];

    double d = rational_cast<double>(acc);
    printf("%.10lf\n",d);
}

int main()
{
    int n;cin >> n;
    for(int i=0;i<n;++i)
    {
	printf("Case #%d:\n",i+1);
	read_and_initialize();
	for(int j=0;j<team_n;++j)
	{
	    calc_OPs();
	    calc_OPPs();

	    output(j);
	}
    }
    return 0;
}
