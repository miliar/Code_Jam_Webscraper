#include<iostream>
using namespace std;

bool played[100][100];
bool won[100][100];

int wonc[100];
int lostc[100];

double wp[100], owp[100], oowp[100];

int main() {
	int T, c=1, N, i, j;
	char str[100];
	cin >> T;
	while(T--) {
		cin >> N;
		for(i=0; i<N; i++) {
			wonc[i]=0;
			lostc[i]=0;
			cin>>str;
			for(j=0; j<N; j++) {
				played[i][j] = (str[j]!='.');
				won[i][j] = (str[j]=='1');
			}

			for(j=0; j<N; j++) {
				if(played[i][j] && won[i][j]) {
					wonc[i]++;
				} else if (played[i][j]) {
					lostc[i]++;
				}
			}

			wp[i] = wonc[i];
			wp[i] /= (wonc[i]+lostc[i]);
			cerr << "wp["<<i<<"] = "<<wp[i]<<endl;

		}

		for(i=0; i<N; i++) {
			double totowp = 0;
			int n=0;
			for(j=0; j<N; j++) {
				if(played[i][j]) {
					double wp = wonc[j];
					if(won[j][i]) {
						wp = wp - 1;
					}
					wp /= (wonc[j] + lostc[j] - 1);
					totowp += wp;
					n++;
				}
			}
			owp[i] = totowp / n;
			cerr << "owp["<<i<<"] = "<<owp[i]<<endl;
		}

		cout << "Case #"<< c++<<":\n";
		for(i=0; i<N; i++) {
			double totowp = 0;
			int n=0;
			for(j=0; j<N; j++) {
				if(played[i][j]) {
					totowp += owp[j];
					n++;
				}
			}
			oowp[i] = totowp / n;
			cerr << "oowp["<<i<<"] = "<<oowp[i]<<endl;
			double rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			cout<<rpi<<endl;

		}
	}
}
