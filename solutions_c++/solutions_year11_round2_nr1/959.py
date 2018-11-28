#include <cstdio>
#include <string>
#include <map>
#include <cmath>

using namespace std;

char TABLE[100][100];
double WP[100];
double OWP[100];
double OOWP[100];
int N;

double calWP(int n, int skip = -1)
{
	int total = 0, win = 0;
	for(int i=0;i<N;i++) {
		if(i == skip) continue;
		if(TABLE[n][i] != '.') {
			total++;
		}
		if(TABLE[n][i] == '1') {
			win++;
		}
	}
	return (double)win/(double)total;
}

void cal()
{
	for(int n=0;n<N;n++) {
		double O = 0;
		int total = 0;
		WP[n] = calWP(n, -1);
		for(int i=0;i<N;i++) {
			if(TABLE[n][i] != '.') {
				total++;
				O += calWP(i, n); 
			}
			OWP[n] = O / total;
		}
	}
	for(int n=0;n<N;n++) {
		double O = 0;
		int total = 0;
		for(int i=0;i<N;i++) {
			if(TABLE[n][i] != '.') {
				total++;
				O += OWP[i]; 
			}
			OOWP[n] = O / total;
		}
	}
}

int main()
{
	int cc, ccN;
	scanf("%d", &ccN);
	for(cc = 0;cc < ccN;cc++) {
		scanf(" %d ", &N);
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++){
				scanf(" %c ", &TABLE[i][j]);
			}
		}
		cal();
		printf("Case #%d:\n", cc+1);
		for(int i=0;i<N;i++) {
			printf("%.8lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}
