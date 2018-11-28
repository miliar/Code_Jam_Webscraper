#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

int n;
int t;
double p[150][150];
double p1[150];
double p2[150];
double wp[150];
double owp[150];
double oowp[150];
char c;

int main(){
	scanf("%d", &n);
	for (int C = 1; C <= n; C++){
		printf("Case #%d:\n", C);
		
		memset(wp, 0, sizeof wp);
		memset(owp, 0, sizeof owp);
		memset(oowp, 0, sizeof oowp);
		scanf("%d", &t);
		for (int i = 0; i < t; i++){
			for (int j = 0; j < t; j++){
				cin >> c;
				if (c == '0'){
					p[i][j] = 0;
				}
				else if (c == '1'){
					p[i][j] = 1;
				}
				else {
					p[i][j] = -1;
				}
			}
		}
		
		for (int i = 0; i < t; i++){
			double w = 0;
			int counter = 0;
			for (int j = 0; j < t; j++){
				if (i != j){
					w += (p[i][j] == 1);
					counter += (p[i][j] != -1);
				}
			}
			p1[i] = w;
			p2[i] = counter;
			wp[i] = w / (counter + 0.0);
		}
		
		for (int i = 0; i < t; i++){
			double w = 0;
			int counter = 0;
			for (int j = 0; j < t; j++){
				if (p[i][j] != -1){
					w += (p1[j] - ((p[j][i] == 1)? 1.0:0.0)) / (p2[j] - 1.0);
					counter++;
				}
			}
			owp[i] = w / (counter + 0.0);
			//cout << owp[i] << ' ' << w << ' ' << counter << endl;
		}
		
		for (int i = 0; i < t; i++){
			double w = 0;
			int counter = 0;
			for (int j = 0; j < t; j++){
				if (p[i][j] != -1){
					w += owp[j];
					counter++;
				}
			}
			oowp[i] = w / (counter + 0.0);
			//cout << oowp[i] << ' ' << w << ' ' << counter << endl;
		}
		
		for (int i = 0; i < t; i++){
			printf("%.12f\n", wp[i] * 0.25 + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
