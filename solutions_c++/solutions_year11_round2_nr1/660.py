#include <iostream>
#include <stdlib.h>
#include <stdio.h>

#define cyc(i,n) for (i=0; i<n; i++)

using std::cin;
using std::cout;
using std::string;

int n,n1,n2,N;
char win_tab[300][300];
int games_played[300];
int games_won[300];
double WP[300];
double OWP[300];
double OOWP[300];
double RPI[300];

int main()
{
	int t,T;
	
	cin >> T;
	
	cyc(t,T)
	{
		char inp_string[305];
		cin >> N;

		cyc(n1,N)
		{
			cin >> inp_string;
			games_played[n1] = 0;
			games_won[n1] = 0;
			cyc(n2,N)
			{
				win_tab[n1][n2] = inp_string[n2];
				if (inp_string[n2] == '1')
				{
					games_played[n1]++;
					games_won[n1]++;
				}
				if ((inp_string[n2]) == '0')
					games_played[n1]++;
			}
		}
		cyc(n,N)
		{
			WP[n] = double(games_won[n]) / double(games_played[n]);
		}

		// compute OOP
		cyc(n1,N)
		{
			OWP[n1] = 0.0;
			cyc(n2,N)
			{
				if (win_tab[n1][n2] != '.')
				{
					OWP[n1] += (double(games_won[n2] - double((win_tab[n2][n1] == '1')?1:0) ) / double(games_played[n2] - 1));
				}
			}
			OWP[n1] = OWP[n1] / double(games_played[n1]);
		}

		// compute OOWP
		cyc(n1,N)
		{
			OOWP[n1] = 0.0;
			cyc(n2,N)
			{
				if (win_tab[n1][n2] != '.')
				{
					OOWP[n1] += OWP[n2];
				}
			}
			OOWP[n1] = OOWP[n1] / double(games_played[n1]);
		}

		// compute RPI
		cyc(n,N)
		{
			RPI[n] = 0.25 * WP[n] + 0.5 * OWP[n] + 0.25 * OOWP[n];
		}

		cout << "Case #" << t + 1 << ":\n";
		cyc(n,N)
		{
			cout << RPI[n] << "\n";
		}
	}
	return 0;
}
