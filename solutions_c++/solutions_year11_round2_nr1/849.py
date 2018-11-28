#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	cout.precision(9);
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int N;
		cin >> N;
		vector<string> table(N);
		for(int i = 0; i < N; ++i){ cin >> table[i]; }
		vector<int> matchNum(N, 0), winningNum(N, 0);
		for(int i = 0; i < N; ++i){
			for(int j = 0; j < N; ++j){
				if(table[i][j] == '0'){
					++(matchNum[i]);
				}else if(table[i][j] == '1'){
					++(matchNum[i]);
					++(winningNum[i]);
				}
			}
		}
		vector<double> wp(N, 0), owp(N, 0), oowp(N, 0);
		for(int i = 0; i < N; ++i){
			wp[i] = static_cast<double>(winningNum[i]) / matchNum[i];
		}
		for(int i = 0; i < N; ++i){
			double sum = 0.0;
			int count = 0;
			for(int j = 0; j < N; ++j){
				if(table[i][j] != '.' && j != i){
					sum +=
						static_cast<double>(winningNum[j] - (table[j][i] == '1' ? 1 : 0)) /
						(matchNum[j] - 1);
					++count;
				}
			}
			owp[i] = sum / count;
		}
		for(int i = 0; i < N; ++i){
			double sum = 0.0;
			int count = 0;
			for(int j = 0; j < N; ++j){
				if(table[i][j] != '.'){
					sum += owp[j];
					++count;
				}
			}
			oowp[i] = sum / count;
		}
		cout << "Case #" << caseNum << ":" << endl;
		for(int i = 0; i < N; ++i){
			cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}
	return 0;
}
