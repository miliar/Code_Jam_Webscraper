#include <iostream>

using namespace std;

int main(){
	int t,n;
	char data[100][100];
	int win[100];
	int sum[100];
	double wp[100];
	double owp[100];
	double oowp[100];
	double tmp;
	int count;
	
	cin >> t;
	
	for (int i = 0; i < t; i++) {
		cin >> n;
		for (int j = 0; j < n; j++) {
			sum[j] = 0;
			win[j] = 0;
			for (int k = 0; k < n; k++){
				cin >> data[j][k];
				if (data[j][k] != '.')
					sum[j]++;
				if (data[j][k] == '1')
					win[j]++;
			}
		}
		
		for (int j = 0; j < n; j++) {
			wp[j] = (double)win[j] / sum[j];
		}
		
		for (int j = 0; j < n; j++) {
			tmp = 0;
			count = 0;
			for (int k = 0; k < n; k++) {
				if (data[j][k] == '.')
					continue;
				count++;
				if (data[j][k] == '1')
					tmp += (double)win[k] / (sum[k] - 1);
				else
					tmp += (double)(win[k] - 1) / (sum[k] - 1);
			}
			owp[j] = tmp / count;
		}
		
		for (int j = 0; j < n; j++) {
			tmp = 0;
			count = 0;
			for (int k = 0; k < n; k++) {
				if (data[j][k] == '.')
					continue;
				tmp += owp[k];
				count++;
			}
			oowp[j] = tmp / count;
		}
		
		cout << "Case #" << (i + 1) << ":" << endl;
		
		cout.precision(10);
		
		for (int j = 0; j < n; j++) {
			cout << (wp[j] * 0.25 + owp[j] * 0.5 + oowp[j] * 0.25) << endl;
		}
	}
	
	return 0;
}