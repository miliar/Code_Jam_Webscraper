#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

using namespace std;

int main()
{
	int T;
	std::cin >> T;
	int case_num = 1;

	while(case_num <= T)
	{
		int N;
		std::cin >> N;
		char c;
		vector<vector<int> > sched;
		vector<double> WP;
		vector<double> OWP;
		vector<double> OOWP;
		for(int i = 0 ; i < N; i++)
		{
			vector<int> veci;
			for(int j = 0 ; j < N; j++)
			{
				std::cin >> c ;
				if(c == '.')
				{
					veci.push_back(-1);
				}
				else if(c == '0')
				{
					veci.push_back(0);
				}
				else
				{
					veci.push_back(1);
				}
			}
			sched.push_back(veci);
		}

		for(int i = 0 ; i < N; i++)
		{
			int num_games = 0;
			int num_wins = 0;
			for(int j = 0 ; j < N; j++)
			{
				if(sched[i][j]==0 || sched[i][j]==1 )
				{
					num_games++;
					num_wins += sched[i][j] ;
				}
			}
			if(num_games > 0)
			{
			WP.push_back((double)num_wins/num_games);
			}
			else
			{
				WP.push_back(0);
			}
		}

		for(int i = 0 ; i < N; i++) // opponent to neglect
		{
			vector<double> oWP;
			for(int j = 0 ; j < N; j++)
			{
				//if(i ==j) break;
				if(sched[i][j] == 0 || sched[i][j] == 1)
				{
					int num_games = 0;
					int num_wins = 0;
					for(int k = 0 ; k < N; k++)
					{
						if(k == i) continue;
						if(sched[j][k]==0 || sched[j][k]==1 )
						{
							num_games++;
							num_wins += sched[j][k] ;
						}
					}
					if(num_games > 0)
					{
						oWP.push_back((double)num_wins/num_games);
					}
					else
					{
						oWP.push_back(0);
					}
				}
			}
			vector<double>::iterator it = oWP.begin();
			int count = 0;
			double sum = 0;
			while(it!=oWP.end())
			{
				sum += *it;
				count++;
				it++;
			}
			if(count == 0)
			{
				OWP.push_back(0);
			}
			else
			{
				OWP.push_back((double)sum/count);
			}
		}

		for(int i = 0 ; i < N; i++)
		{
			int count_opp = 0;
			double sum = 0;
			for(int j = 0 ; j < N; j++)
			{
				if(sched[i][j] == 0 || sched[i][j] == 1)
				{
					count_opp++;
					sum += OWP[j];
				}
			}
			if(count_opp == 0)
			{
				OOWP.push_back(0);
			}
			else
			{
				OOWP.push_back(sum/count_opp);
			}
		}

		std::cout << "Case #" << case_num << ":" << std::endl;
		for(int i = 0 ; i < N; i++)
		{
			std::cout << 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << std::endl ;
		}
		case_num++;
	}
	std::cin >> T;
	return 1;
}