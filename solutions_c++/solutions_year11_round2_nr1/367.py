
#include "cstdio"
#include "cstring"
#include "cmath"
#include "iostream"
//#include "vector"
//#include "map"
//#include "string"

using namespace std;


int algo() {
	int tn;
	scanf("%d", &tn);

	for (int ti = 1; ti <= tn; ti++) {

		int n;
		scanf("%d", &n);

		char m[200][200];
		for (int i = 0; i < n; i++) {
			scanf("%s", m[i]);
		}		

		double wp[200];
		int w[200];
		int played[200];
		for (int i = 0; i < n; i++) {
			w[i] = 0;
			played[i] = 0;
			for (int j = 0; j < n; j++) {
				if (m[i][j] != '.') {
					played[i]++;
				};
				if (m[i][j] == '1') {
					w[i]++;
				};
			}
			wp[i] = ((double) w[i]) / ((double)played[i]);
		}		

		double owp[200];
		for (int i = 0; i < n; i++) {
			owp[i] = 0;
			for (int j = 0; j < n; j++) {
				if (m[i][j] != '.') {
					int minuswin = 0;
					if (m[i][j] == '0') { minuswin = 1;}
					double cowp = ((double) (w[j]-minuswin)) / ((double)(played[j]-1));
					owp[i] += cowp;
				};
			}		
			owp[i] /= ((double)(played[i]));
		}		
	
		double oowp[200];
		for (int i = 0; i < n; i++) {
			oowp[i] = 0;
			for (int j = 0; j < n; j++) {
				if (m[i][j] != '.') {
					double cowp = owp[j];
					oowp[i] += cowp;
				};
			}		
			oowp[i] /= ((double)(played[i]));
		}			

		double rpi[200];
		for (int i = 0; i < n; i++) {
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		}			

		printf("Case #%d:\n", ti);
		for (int i = 0; i < n; i++) {
			printf("%.12f\n", rpi[i]);
		}			

	}

	return 0;
}








//STANDARD COMMON CODE BELOW

int main(int argc, char *argv[]) {
	char str[80];
	strcpy(str, argv[1]);
	strcat(str, ".in");
  freopen(str, "r", stdin);
	strcpy(str, argv[1]);
	strcat(str, ".out");
	freopen(str, "w", stdout);

	int rv = algo();

	fclose(stdout);

	return rv;
}





