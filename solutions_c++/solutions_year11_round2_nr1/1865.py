#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<cmath>

using namespace std;
char a[101][101];
int win[101], lose[101], w[101], l[101];
double wp[101], owp[101], oowp[101];
int main(){
	int T, N;
	string line;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		memset(win, 0, sizeof(win));
		memset(lose, 0, sizeof(lose));
		memset(w, 0, sizeof(w));
		memset(l, 0, sizeof(l));
		//memset(a, 0, sizeof(a));
		scanf("%d", &N);
		getline(cin, line);
		for(int i = 0; i < N; i++){
			getline(cin, line);
			for(int j = 0; j < N; j++)
				a[i][j] = line[j];
		}

		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(a[i][j] == '0'){
					lose[i]++;
					l[i]++;
				}
				else if(a[i][j] == '1'){
					win[i]++;
					w[i]++;
				}
			}
			wp[i] = (double)win[i]/(win[i]+lose[i]);
		}

		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(a[i][j] == '0'){
					win[j]--;
				}
				else if(a[i][j] == '1')
					lose[j]--;

			}
			double tmp = 0.0;
			for(int j = 0; j < N; j++){
				if(a[i][j] != '.'){
					tmp += (double)win[j]/(win[j]+lose[j]);
				}
			}
			owp[i] = tmp/(w[i]+l[i]);

			for(int j = 0; j < N; j++){
				win[j] = w[j];
				lose[j] = l[j];
			}

		}

		for(int i = 0; i < N; i++){
			double tmp = 0.0;
			for(int j = 0; j < N; j++){
				if(a[i][j] != '.'){
					tmp += owp[j];
				}
			}
			oowp[i] = tmp/(w[i]+l[i]);
		}

		cout << "Case #" << t << ":" << endl;
		for(int i = 0; i < N-1; i++){
			printf("%.6f\n", 0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]);
		}
		printf("%.6f", 0.25*wp[N-1]+0.50*owp[N-1]+0.25*oowp[N-1]);
		if(t < T)
			cout << endl;

	}


	return 0;
}
