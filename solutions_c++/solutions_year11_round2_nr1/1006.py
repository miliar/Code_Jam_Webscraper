#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int T, N;
	char c;
	int played[100][100];
	int W[100], G[100];
	double OWP[100], RPI[100];

	cin >> T;
	for (int cnt = 1; cnt <=T; ++cnt){
		cin >> N; 
		for (int i=0; i<N; ++i){
			W[i] = 0;
			G[i] = 0;
			for (int j=0; j<N; ++j){
				cin >> c;
				if (c=='1'){
					played[i][j] = 1;
					W[i]++;
					G[i]++;
				} else if (c=='0'){
					played[i][j] = 0;
					G[i]++;
				} else {
					played[i][j] = -1;
				}
			}
		}
		for (int i=0; i<N; ++i){
			RPI[i] = 0.25* W[i]*1.0 / G[i];
			double sum_OWP=0;
			int cnt_OWP=0;
			for (int j=0; j<N; ++j){
				if (played[i][j] == 1){
					sum_OWP += W[j]*1.0 / (G[j]-1);
					cnt_OWP++;
				} else if (played[i][j] == 0){
					sum_OWP += (W[j]-1)*1.0 / (G[j]-1);
					cnt_OWP++;
				}
			}
			OWP[i] = sum_OWP / cnt_OWP;
			//cout << i << " " << OWP[i] << endl;
			RPI[i] += 0.5 * sum_OWP / cnt_OWP;
		}
		for (int i=0; i<N; ++i){
			double sum_OOWP = 0;
			int cnt_OOWP = 0;
			for (int j=0; j<N; ++j){
				if (played[i][j] != -1){
					sum_OOWP += OWP[j]; 
					cnt_OOWP ++;
				}
			}
			RPI[i] += 0.25 * sum_OOWP / cnt_OOWP; 
		}

		cout << "Case #" << cnt << ":" << endl;
		for (int i=0; i<N; ++i)
			cout << setprecision(8) << RPI[i] << endl;

	}
	return 0;
}
