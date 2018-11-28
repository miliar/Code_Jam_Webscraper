#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;


vector<vector<char> *> ScoreTable;
vector<int> match_count;
vector<int> win_count;
vector<double> WP;
vector<double> OWP;
vector<double> OOWP;

int main(int argc, char *argv[])
{
	char c;
	int k, i, j, test_nb, team_numb;
	int win_count_t, match_count_t;

	cin >> test_nb;
	for (k = 0; k < test_nb; k++) {
		cin >> team_numb;
		ScoreTable.clear();
		match_count.clear();
		win_count.clear();
		WP.clear();
		OWP.clear();
		OOWP.clear();
		
		for (i = 0; i < team_numb; i++) {
			win_count_t = 0;
			match_count_t = 0;
			 
			ScoreTable.push_back(new vector<char>);
			for (j = 0; j < team_numb; j++) {
				cin >> c;
				ScoreTable[i]->push_back(c);
				if (c != '.') match_count_t++;
				if (c == '1') win_count_t++;
			}
			match_count.push_back(match_count_t);
			win_count.push_back(win_count_t);
			WP.push_back(((double) win_count[i]) / ((double) match_count[i]));
		}
		
		for (i = 0; i < team_numb; i++) {
			OWP.push_back(0.0);
			for (j = 0; j < team_numb; j++) {
				if ((*(ScoreTable[i]))[j] == '0') OWP[i] += ((double)(win_count[j]-1)) / ((double)(match_count[j]-1));
				else if ((*(ScoreTable[i]))[j] == '1') OWP[i] += ((double)(win_count[j])) / ((double)(match_count[j]-1));
			}
			OWP[i] /= (double) match_count[i];
		}
		
		for (i = 0; i < team_numb; i++) {
			OOWP.push_back(0.0);
			for (j = 0; j < team_numb; j++) {
				if ((*(ScoreTable[i]))[j] != '.') OOWP[i] += OWP[j];
			}
			OOWP[i] /= (double) match_count[i];
		}
		
		cout << "Case #" << k+1 << ":" << endl;
		for (i = 0; i < team_numb; i++) {
			printf("%9lf\n", (0.25 * WP[i]) + (0.5 * OWP[i]) + (0.25 * OOWP[i]));
		}
	}
	
	return 0;
}
