#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>

#define PB push_back
#define MP make_pair

using namespace std;

int main () {
	int cases;
	cin >> cases;
	for(int case_i = 1; case_i <= cases; case_i++){
		cout << "Case #" << case_i << ":" << endl;
		int teams;
		cin >> teams;
		
		char **score;
		double *WP; double *OWP; double *OOWP;
		
		WP = new double[teams];
		OWP = new double[teams];
		OOWP = new double[teams];
		score = new char*[teams];
		// in + WP
		for (int i = 0; i < teams; i++) {
			score[i] = new char[teams];
			WP[i] = 0; double total = 0;
			for (int j = 0; j < teams; j++) {
				cin >> score[i][j];
				if(score[i][j] == '1')
					WP[i] += 1.0;
				if(score[i][j] != '.')
					total += 1.0;
			}
			WP[i] = WP[i] / total;
			//cout << WP[i] << endl;
		}
		// OWP
		for (int i = 0; i < teams; i++) {
			double sum = 0;double total = 0;
			for (int j = 0; j < teams; j++) {
				
				if(score[i][j] != '.'){
					double tt = 0; double twp = 0;
					for (int k = 0; k < teams; k++){
						if (k == i) continue;
						if(score[j][k] != '.')
							tt+=1.0;
						if(score[j][k] == '1')
							twp += 1.0;
					}
					//cout << j << twp << tt << endl<< endl;
					twp = twp / tt;
					sum += twp;
					total += 1.0;
				}
			}
			OWP[i] = sum / (total);
			//cout << OWP[i] << endl;
		}
		
		// OOWP
		for (int i = 0; i < teams; i++) {
			double sum = 0;double total = 0;
			for (int j = 0; j < teams; j++) {
				if(score[i][j] != '.'){
					sum += OWP[j]; //cout << OWP[j] << "+";
					total += 1.0;
				}
			}
			OOWP[i] = sum / total;
			
			//cout << OOWP[i] << endl;
		}
		cout.precision(12);
		for (int i = 0; i < teams; i++) {
			double RPI = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			cout << RPI << endl;
		}
		
		for (int j = 0; j < teams; j++) delete( score[j]);
		delete(score); delete(WP); delete(OWP); delete(OOWP);
	}
    return 0;
}
