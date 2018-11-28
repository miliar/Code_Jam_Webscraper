#include<cstdio>
#include<iostream>
#include<cmath>

using namespace std;

const int MAXN = 110;
int schedule[MAXN][MAXN];
int winnings[MAXN], total[MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];
int n;

void printSchedule() {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			cout << schedule[i][j] << " ";
		}
		cout << endl;
	}
}

void wps() {
	for(int i = 0; i < n; i++) {
		wp[i] = ((double)winnings[i] / (double)total[i]);
	}
}

void owps() {
	for(int i = 0; i < n; i++) {
		owp[i] = 0.0;
		for(int j = 0; j < n; j++) {
			if(schedule[j][i] != -1)
				owp[i] += (((double)winnings[j] - (double)schedule[j][i]) / (double)(total[j]-1));
		}

		owp[i] /= (double)total[i];
	}
}

void oowps() {
	for(int i = 0; i < n; i++) {
		oowp[i] = 0.0;
		for(int j = 0; j < n; j++) {
			if(schedule[j][i] != -1)
				oowp[i] += owp[j];
		}

		oowp[i] /= (double)total[i];
	}
}

double rpi(int k) {
	return ((0.25 * wp[k]) + (0.5 * owp[k]) + (0.25 * oowp[k]));
}

int main() {
	int T = 0;
	cin >> T;

	for(int caseNum = 1; caseNum <= T; caseNum++) {
		n = 0;
		cin >> n;

		for(int i = 0; i < n; i++) {
			winnings[i] = 0;
			total[i] = 0;
			for(int j = 0; j < n; j++) {
				char x = '\0';
				cin >> x;
				if(x == '.')
					schedule[i][j] = -1;
				else if(x == '0') {
					schedule[i][j] = 0;
					total[i] ++;
				}
				else {
					schedule[i][j] = 1;
					total[i] ++;
					winnings[i] ++;
				}
			}
		}

//		printSchedule();

		printf("Case #%d:\n", caseNum);
		wps();
		owps();
		oowps();

//		printf("wp[0] = %lf\n", wp[0]);
//		printf("wp[1] = %lf\n", wp[1]);
//		printf("wp[2] = %lf\n", wp[2]);

		for(int i = 0; i < n; i++)
			printf("%.10lf\n", rpi(i));
	}

	return 0;
}
