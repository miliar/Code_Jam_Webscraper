								/* in the name of Allah */
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <cstdio>
#include <cmath>
#include <map>

using namespace std;

ifstream fin("A_RPI.in");
ofstream fout("A_RPI.out");

#define cin fin
#define cout fout

int n;
int tot[110], win[110];
char mat[110][110];
double wp[110], owp[110], oowp[110];

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		memset(tot, 0, sizeof tot);
		memset(win, 0, sizeof win);
		cin >> n;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> mat[i][j];
				if(mat[i][j] != '.')
					tot[i]++;
				if(mat[i][j] == '1')
					win[i]++;
			}
			wp[i] = (double)win[i] / tot[i];
		}
		for(int i = 0; i < n; i++){
			owp[i] = 0;
			for(int j = 0; j < n; j++){
				if(mat[i][j] == '.')
					continue;
				owp[i] += (double)(win[j] - (mat[j][i] - '0')) / (tot[j] - 1);
			}
			owp[i] /= tot[i];
		}
		for(int i = 0; i < n; i++){
			oowp[i] = 0;
			for(int j = 0; j < n; j++)
				if(mat[i][j] != '.')
					oowp[i] += owp[j];
			oowp[i] /= tot[i];
		}
		cout << "Case #" << ++test << ":" << endl;
		cout.precision(7);
		cout.setf(ios::fixed | ios::showpoint);
		for(int i = 0; i < n; i++){
			//cout << wp[i] << ' ' << owp[i] << ' ' << oowp[i] << endl;
			cout << (wp[i] + owp[i] + owp[i] + oowp[i]) / 4 << endl;
		}
	}
	return 0;
}
