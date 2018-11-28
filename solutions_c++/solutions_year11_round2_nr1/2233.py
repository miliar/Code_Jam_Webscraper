#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define repd(i,n,m) for(int i=n;i<(int)(m);i++)
#define repvi(v,i) for(vector<int>::iterator i = v.begin(); i < v.end();i++)
#define repvs(v,i) for(vector<string>::iterator i = v.begin(); i < v.end();i++)
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

int countChars(string s, char c) {
	int count = 0;
	for (int i = 0; i < s.size(); i++)
		if (s[i] == c) count++;
	return count;
}


int main() {
	freopen("a.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int cases;
	cin >> cases;
	repd(nn, 1, cases+1) {
		cout << "Case #" << nn << ": ";
		int N;
		cin >> N;
		string lines[N];
		getline(cin, lines[0]);
		rep(i, N) {
			getline(cin, lines[i]);
		}
		int ones[N], zeros[N], dots[N];

		rep(i, N) {
			ones[i] = countChars(lines[i], '1');
			zeros[i] = countChars(lines[i], '0');
			dots[i] = countChars(lines[i], '.');
		}

		double WP[N], OWP[N], OOWP[N];
		rep(i, N) {
			WP[i] = ones[i] / (double) (ones[i] + zeros[i]); 

			double tempOWP[N];
			rep(j, N) {
				if (i == j)
					continue;
				int tempones = 0, tempzeroes = 0;
				rep(k, N) {
					if (i ==k) 
						continue;
					if (lines[j][k] == '1')
						tempones++;
					if (lines[j][k] == '0')
						tempzeroes++;
				}
				tempOWP[j] = tempones / (double) (tempones + tempzeroes);
			}
			double total=0;
		   int count = 0;
			rep(j, N) {
				if (i == j) continue;
				if (lines[i][j] == '1' || lines[i][j] == '0') {
					total += tempOWP[j];
					count++;
				}
			}
			OWP[i] = total / (double) (count);

		}
		rep(i, N) {
			//OOWP calc
			double total = 0;
			int count = 0;
			rep(j, N) {
				if (lines[i][j] == '1' || lines[i][j] == '0') {
					total += OWP[j];
					count++;
				}
			}
			OOWP[i] = total/ (double) count;

			double RPI = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			cout << endl;
			cout << fixed << setprecision(12);
			cout << RPI ;
		}
		cout << endl;
	}	
	
	return 0;
}
