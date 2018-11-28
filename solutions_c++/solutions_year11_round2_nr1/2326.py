
#include <iostream>
#include <vector>
using namespace std;

struct wp_item
{
    int won;
	int lost;

	double wp;
};

vector < wp_item > wp_cache;
vector <double> owp_cache;
vector <double> oowp_cache;


void populate_wp_cache(vector < vector <char> > &board)
{
	for (int i=0; i<board.size(); i++)
	{
	    int num_won = 0, num_lost = 0, num_dots = 0;
		for (int j=0; j<board.size(); j++)
		{
			if (board[i][j] == '1')
			{
			    num_won++;
			}
			else if (board[i][j] == '0')
			{
			    num_lost++;
			}
			else
			{
				num_dots;
			}
		}
		wp_item temp;
		temp.wp = (double)num_won/(double)(num_won + num_lost);
		temp.won = num_won;
		temp.lost = num_lost;
		wp_cache.push_back(temp);
	}
}

void populate_owp_cache(vector < vector <char> > &board)
{
	for (int i=0; i<board.size(); i++)
	{
		double temp_owp = 0;
		int ops=0;
		for (int j=0; j<board.size(); j++)
		{
			if (j!=i)
			{
				if (board[j][i] == '1')
				{
					temp_owp += (double)(wp_cache[j].won-1)/(double)(wp_cache[j].won-1+wp_cache[j].lost);
					ops++;
				}
				else if (board[j][i] == '0')
				{
				    temp_owp += (double)(wp_cache[j].won)/(double)(wp_cache[j].won-1+wp_cache[j].lost);
					ops++;
				}
				else
				{
				    //temp_owp += wp_cache[j].wp;
				}
			}
		}
		owp_cache.push_back(temp_owp/(ops));
	}
}

void populate_oowp_cache(vector < vector <char> > &board)
{
	for (int i=0; i<board.size(); i++)
	{
		double temp_oowp = 0;
		int ops = 0;
		for (int j=0; j<board.size(); j++)
		{
			if ((j!=i)&&(board[j][i] != '.'))
			{
				temp_oowp += owp_cache[j];
				ops++;
			}
		}
		oowp_cache.push_back(temp_oowp/(ops));
	}
}
double calculate_rpi(int team, vector < vector <char> > &board)
{
	double rpi;
	rpi = 0.25 * wp_cache[team].wp + 0.50 * owp_cache[team] + 0.25 * oowp_cache[team];
	return rpi;
}

int main(void)
{
    int num_of_cases;
	cin>>num_of_cases;

	cout.precision(10);

	int tc_count = 1;
	while(tc_count <= num_of_cases)
	{

		int num_of_teams;
		cin>>num_of_teams;

		vector < vector <char> > board;
        wp_cache.resize(0);
		owp_cache.resize(0);
		oowp_cache.resize(0);
		for (int i=0; i<num_of_teams; i++)
		{
			vector <char> temp1;
			for (int j=0; j<num_of_teams; j++)
			{
			    char temp2;
				cin>>temp2;
				temp1.push_back(temp2);
			}
			board.push_back(temp1);
		}

        populate_wp_cache(board);
		populate_owp_cache(board);
		populate_oowp_cache(board);

		cout<<"Case #"<<tc_count<<":\n";

		for (int i=0; i<num_of_teams; i++)
		{
            double rpi = calculate_rpi(i, board);
			cout<<rpi<<"\n";
		}
		tc_count++;
	}
    return 0;
}