#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

int num_trials;
int num_teams;
char match_table[100][100];
int team_total_games[100];
int team_won_games[100];
double wp[100];
double owp[100];
double oowp[100];

int main(int argc, const char* argv[])  {
    ofstream fout ("a.out");
    ifstream fin ("a.in");

	fin >> num_trials;
	for (int trial = 1; trial <= num_trials; trial++) {
		fin >> num_teams;
		for (int i = 0; i < num_teams; i++) {
			team_total_games[i] = 0; //reset
			team_won_games[i] = 0;
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
			string next_row;
			fin >> next_row;
			for (int j = 0; j < num_teams; j++) {
				match_table[i][j] = next_row[j];
				if (match_table[i][j] == '1') {
					team_won_games[i]++;
				}
				if (match_table[i][j] != '.') {
					team_total_games[i]++;
				}
				wp[i] = (double) team_won_games[i] / team_total_games[i];
			}
		}
		
		/*for (int i = 0; i < num_teams; i++) {
			for (int j = 0; j < num_teams; j++) {
				cout << match_table[i][j]  << " ";
			}
			cout << endl;
		}*/

		for (int i = 0; i < num_teams; i++) {
			int opp_count = 0;
			double opp_alt_wp_sum = 0;
			for (int opp = 0; opp < num_teams; opp++) {
				if (match_table[i][opp] != '.') { // if they played against each other
					opp_count++;
					double opp_wp;
					if (match_table[i][opp] != '1') { // i wins
						opp_wp = (double) (team_won_games[opp]-1) / (team_total_games[opp]-1);
					} else {
						opp_wp = (double) (team_won_games[opp]) / (team_total_games[opp]-1);
					}
					opp_alt_wp_sum += opp_wp;
				}
			}
			owp[i] = opp_alt_wp_sum/opp_count;
		}
		
		for (int i = 0; i < num_teams; i++) {
			int opp_count = 0;
			double opp_owp_sum = 0;
			for (int opp = 0; opp < num_teams; opp++) {
				if (match_table[i][opp] != '.') { // if they played against each other
					opp_owp_sum += owp[opp];
					opp_count++;
				}
			}
			oowp[i] = opp_owp_sum/opp_count;
		}
		
		fout << "Case #" << trial << ":" << endl;
		for (int i = 0; i < num_teams; i++) {
			//cout << i  << ":" << endl;
			//cout  << wp[i] << "  " <<  owp[i] << "  " << oowp[i] << endl;
			fout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
		}		

	}

}
