#include <iostream>
#include <iomanip>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N;
		cin >> N;
		int a[100][100];
		double wp[100][100];
		double owp[100];
		double oowp[100];

		for (int n = 0; n < N; n++) {
			for (int n2 = 0; n2 < N; n2++) {
				char c;
				cin >> c;
				if(c == '1')
					a[n][n2] = 1;
				else if(c == '0')
					a[n][n2] = 0;
				else
					a[n][n2] = -1;
				wp[n][n2] = 0;
			}
			owp[n] = 0;
			oowp[n] = 0;
		}	
		
		for (int n1 = 0; n1 < N; n1++) {
			int WP = 0;;
			int count = 0;
			for (int n2 = 0; n2 < N; n2++) {
				if(a[n1][n2] != -1){
					WP += a[n1][n2];
					count++;
				}
			}
			wp[n1][n1] = WP;
			for (int n2 = 0; n2 < N; n2++) {
			//	if(n1 == n2)
			//		continue;
				int c = count;
				if(n1 != n2 && a[n1][n2] != -1){
					wp[n1][n2] = WP - a[n1][n2];
					c--;
				}
				else if(a[n1][n2] == -1)
					wp[n1][n2] = WP;
				wp[n1][n2] /= c;
				//else if(n1 != n2)
			}
		}

		for (int n = 0; n < N; n++) {
	//		cout<<"WPS "<<wp[0][n]<<endl;
		}

		for (int n1 = 0; n1 < N; n1++) {
			int c = N;
			for (int n2 = 0; n2 < N; n2++) {
				if(n1 == n2)
					continue;
				if(a[n1][n2] == -1)
					c--;
				else
				owp[n1] += wp[n2][n1];
			}
			owp[n1] /= (c-1);
		}
		
	//	cout<<"OWP "<<owp[0]<<endl;
		for (int n1 = 0; n1 < N; n1++) {
			int c = N;
			for (int n2 = 0; n2 < N; n2++) {
				if(n1==n2)
					continue;
				if(a[n1][n2] == -1)
					c--;
				else
					oowp[n1] += owp[n2];
			}
			oowp[n1] /= (c-1);
		}
	//	cout<<"OOWP "<<oowp[0]<<endl;
		
		cout<<fixed<<setprecision(8);
		cout<<"Case #"<<(t+1)<<":"<<endl;
		for (int n = 0; n < N; n++) {
			double rpi = 0.25 * wp[n][n] + 0.5 * owp[n] + 0.25 * oowp[n];
			cout<<rpi;
			//if(n<N-1)
				cout<<endl;
		}


		
	}
}
