#include <vector>
#include <iostream>
#include <string> 
#include <limits>

using namespace std;

int main()
{
	int T;
	cin>> T;

	for(int t = 0; t<T;++t) {
		int N;
		cin>>N;


		vector<double> number(N, 0);
		vector<double> won(N, 0);
		vector<double> WP(N, 0);
		vector<double> OWP (N, 0);
		vector<double> OOWP (N, 0);
		vector< vector <char>> data(N, vector<char>(N,'.'));

		for(int i = 0; i<N; ++i ){
			for(int j = 0; j<N; ++j ){

				char tmp;
				
				cin>>tmp;
				if (tmp != '.') {
					++number[i];
				}
				if (tmp == '1') {
					++won[i];
				}
				data[i][j] = tmp;
			}
		}
		for (int i = 0; i < N; ++i) {
			WP[i] = won[i] / number[i];
		}
		for(int i = 0; i<N; ++i ){
			for (int j = 0; j < N; ++j) {
				if(data[i][j] != '.') {
					if (data[i][j] == '1') {
						OWP[i] += WP[j]*number[j]/(number[j]-1);
					}
					else
					{
						OWP[i] += (WP[j]*number[j]-1.0)/(number[j]-1.0);
					}
				}
			}
		}
		for(int i = 0; i<N; ++i ){
			OWP[i] /= number[i];
		}
		for(int i = 0; i<N; ++i ){
			for (int j = 0; j < N; ++j) {
				if (i != j) {
					if(data[i][j] != '.') {
						OOWP[i] += OWP[j];
					}
				}
			}
		}
		for(int i = 0; i<N; ++i ){
			OOWP[i] /= number[i];
		}
		cout<<"Case #"<<t+1<<": "<<endl;
		for(int i = 0; i<N; ++i ){
			cout<<0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]<<endl;
		}
	}
}
