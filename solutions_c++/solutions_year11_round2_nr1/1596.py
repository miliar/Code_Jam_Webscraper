#include <iostream>
#include <vector>
using namespace std;

int main(void){
	int T;
	cin >> T;
	for(int i=1; i <= T; ++i){
		cout << "Case #" << i << ":" << endl;
		int N;
		cin >> N;
		vector<vector<char> >teams;
		teams.resize(N);
		vector<double> WP, OWP, OOWP;
		WP.resize(N);
		OWP.resize(N);
		OOWP.resize(N);
		for(int j = 0; j < N; ++j){
			teams[j].resize(N);
			int played = 0;
			int won = 0;
			for(int k = 0; k < N; ++k){
				char input;
				cin >> input;
				teams[j][k] = input;
				if(input != '.'){
					++played;
				}
				if(input == '1'){
					++won;
				}
			}
			WP[j] = (double)won/played;
			//cout << "WP = " << WP[j] << endl;
		}
		for(int j = 0; j < N; ++j){
			//cout << "for team " << (char)('A' + j) << endl;
			int opponents = 0;
			double sum = 0;
			for(int k = 0; k < N; ++k){
				if(k == j) continue;
				if(teams[k][j] == '.') continue;
				++opponents;
				int played = 0;
				int won = 0;
				//cout << "team " << (char)('A'+k);
				for(int l = 0; l < N; ++l){
					if(l == j) continue;
					if(teams[k][l] == '.') continue;
					++played;
					//cout << " played " << (char)('A' + l);
					if(teams[k][l] == '1') ++won;
				}
				sum += (double)won/played;
			}
			OWP[j] = sum / opponents;
			//cout << "OWP = " << OWP[j] << endl;
		}
		for(int j = 0; j < N; ++j){
			double sum = 0;
			int played = 0;
			for(int k = 0; k < N; ++k){
				if(teams[k][j] == '.') continue;
				sum += OWP[k];
				++played;
			}
			OOWP[j] = sum / played;
			//cout << OOWP[j] << endl;
		}
		cout.precision(12);
		for(int j = 0; j < N; ++j){
			cout << 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j] << endl;
		}
		
	}
}
