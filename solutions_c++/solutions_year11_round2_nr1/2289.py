#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>

using namespace std;

int main() {
	/* Input data file. */
	string filename;
	getline(cin, filename);
	ifstream inputFile;
	inputFile.open(filename.c_str(), ios::in);
	
	/* Output stored in gcjoutput.txt */
	ofstream outputFile;
	outputFile.open("gcjoutput.txt", ios::out);
	
	int T;
	inputFile >> T;
	for (int i = 0; i < T; i++) {
		int n;
		inputFile >> n;
		
		map<int, vector<char> > teamChart;
		map<int, double> teamRPI;
		map<int, double> WP_map;
		map<int, double> OWP_map;
		map<int, double> OOWP_map;
		
		for (int j = 0; j < n; j++) {
			vector<char> team;
			char row[n];
			inputFile >> row;
			for (int k = 0; k < n; k++) {
				team.push_back(row[k]);
			}
			teamChart.insert(make_pair(j, team));
		}
		
		// WP map construction
		for (int j = 0; j < n; j++) {
			int total = 0, wins = 0;
			for (int k = 0; k < n; k++) {
				if (teamChart[j][k] == '.') continue;
				if (teamChart[j][k] == '0') {total++; continue;}
				if (teamChart[j][k] == '1') {total++; wins++;}
			}
			WP_map.insert(make_pair(j, (double)wins / (total)));
		}
		
		// OWP map construction
		for (int j = 0; j < n; j++) {
			double sum = 0.0;
			int opp = 0;
			for (int k = 0; k < n; k++) {
				if (teamChart[j][k] == '.') continue;
				else {
					int total = 0, wins = 0;
					for (int l = 0; l < n; l++) {
						if (teamChart[k][l] == '.' || l == j) continue;
						if (teamChart[k][l] == '0') {total++; continue;}
						if (teamChart[k][l] == '1') {total++; wins++;}
					}
					sum += double(wins) / total;
					opp++;
				}
			}
			OWP_map.insert(make_pair(j, sum/opp));
		}
		
		// OOWP map construction
		for (int j = 0; j < n; j++) {
			double sum = 0.0;
			int opp = 0;
			for (int k = 0; k < n; k++) {
				if (teamChart[j][k] == '.') continue;
				else {sum += OWP_map[k]; opp++;}
			}
			OOWP_map.insert(make_pair(j, sum/opp));
		}
		
		outputFile << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < n; j++) {
			cout << WP_map[j] << " " << OWP_map[j] << " " << OOWP_map[j] << endl;
			outputFile << 0.25 * WP_map[j] + 0.50 * OWP_map[j] + 0.25 * OOWP_map[j] << endl;
		}
	}
	
	/* Clearing file stream. */
	inputFile.close();
	outputFile.close();
	
	return 0;
}