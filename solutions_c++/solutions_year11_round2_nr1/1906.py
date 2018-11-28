#include <cstdio>
#include <map>
using namespace std;

int games[100][100];
double wp[100];
double owp[100][100];

char str[101];
int wins[100];
int losses[100];
double rpi[100];
double aowp[100];

int main() {


	

	int z;
	scanf("%d\n", &z);
	for(int i=0; i<z; ++i) {
	
		int n;
		scanf("%d\n", &n);
		for(int j=0; j<100; ++j) {
			wins[j] = 0;
			losses[j] = 0;
			rpi[j] = 0;
			aowp[j] = 0;
			wp[j] = 0;
		}
		

		for(int j=0; j<n; ++j) {
			scanf("%s", str);
			for(int k=0; k<n; ++k) {
				games[j][k] = str[k]=='1' ? 1 : (str[k]=='0' ? 0 : -1);
				if(games[j][k] == 1) {
					wins[j]++;
				}
				else if(games[j][k]==0) {
					losses[j]++;
				}

			}
			wp[j] = (double)wins[j]/(double)(wins[j]+losses[j]);

		}
		for(int j=0; j<n; ++j) 
			for(int k=0; k<n; ++k) {
				double x = 0;
				if(games[j][k] == 1)
					owp[j][k] = (wp[j]*(wins[j]+losses[j])-1)/(wins[j]+losses[j]-1);
				else if(games[j][k] == 0)
					owp[j][k] = (wp[j]*(wins[j]+losses[j]))/(wins[j]+losses[j]-1);
				else owp[j][k] = wp[j];

			}

		for(int j=0; j<n; ++j) {
			for(int k=0; k<n; ++k) {
				if(k!=j && games[k][j] >=0)
					aowp[j] += owp[k][j];
			}
			aowp[j]/=wins[j]+losses[j];
		}

		for(int j=0; j<n; ++j) {
			rpi[j] = 0.25 *wp[j];
			rpi[j] += 0.5 *aowp[j];

			double x = 0;
			for(int k=0; k<n; ++k)
				if(k!=j && games[k][j] >=0) x+=aowp[k];
			x/=wins[j]+losses[j];
			rpi[j] += 0.25 * x;
		}

		printf("Case #%d:\n", i+1);
		for(int j=0; j<n; ++j) {
			printf("%.12f\n", rpi[j]);
		}

	}

}