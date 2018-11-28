#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main(){
	int t;
	ifstream fin("A-large.in");
	ofstream fout("a2.out");
	fin >> t;
	for(int i = 0; i < t; i++){
		string s[101];
		int n;
		fin >> n;
		for(int i = 0; i < n; i++)
			fin >> s[i];
		double wp[101], owp[101], oowp[101];
		int win[101], lo[101];
		for(int i = 0; i < n; i++){
			lo[i] = 0, win[i] = 0;
			for(int j = 0; j < n; j++){
				if(s[i][j] == '1')
					win[i]++;
				else if(s[i][j] == '0')
					lo[i]++;
			}
			wp[i] = (double)win[i] / (lo[i] + win[i]);
		}
		for(int i = 0; i < n; i++){
			owp[i] = 0;
			int op = 0;
			for(int j = 0; j < n; j++){
				if(s[i][j] != '.'){
					op++;
					if(s[i][j] == '1')
						owp[i] += ((double)win[j] / (lo[j] + win[j] - 1));
					else
						owp[i] += (double)(win[j] - 1) / (lo[j] + win[j] - 1);
				}
			}
			owp[i] /= op;
		}
		for(int i = 0; i < n; i++){
			int op = 0;
			oowp[i] = 0;
			for(int j = 0; j < n; j++)
				if(s[i][j] != '.'){
					oowp[i] += owp[j];
					op++;
				}
				oowp[i] /= op;
		}
		fout << "Case #" << i + 1 << ":" << endl;
		fout.precision(12);
		for(int i = 0; i < n; i++){
			double ans = wp[i] / 4. + owp[i] * .5 + oowp[i] / 4.;
			fout << ans << endl;
		}
	}
	return 0;
}