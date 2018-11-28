/*    muriloadriano @ topcoder
 *    muriloufg @ codeforces
 */
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <deque>
#include <ctime>
#include <cfloat>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>
#include <iomanip>
#include <climits>
#include <sstream>
#include <queue>
#include <utility>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define ti(x) typeof(x.begin())
#define all(x) x.begin(), x.end()
#define fill(x, y) memset(x, y, sizeof(x)) 

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int INF = 0x3f3f3f3f;
const double EPS = 1e-5;

template <typename T> T abs(const T& a) { if (a >= 0) return a; return -a; }


int main()
{
	ios::sync_with_stdio(false);
	
 	int tc;
	cin >> tc;
	
	int n;
	for (int t = 1; t <= tc; ++t) {
		cin >> n;
		string mat[n];
		double wp[n];
		int games[n], won[n];
		
		for (int i = 0; i < n; ++i) {
			cin >> mat[i];
			
			games[i] = won[i] = 0;
			for (int j = 0; j < n; ++j) {
				if (mat[i][j] == '0') {
					games[i]++;
				}
				else if (mat[i][j] == '1') {
					games[i]++;
					won[i]++;
				}
			}
			wp[i] = double(won[i]) / games[i];
		}
		
		double owp[n];
		for (int i = 0; i < n; ++i) {
			owp[i] = 0;
			int cnt = 0;
			
			for (int j = 0; j < n; ++j) {
				if (i != j) {
					if (mat[i][j] == '0') {
						owp[i] += double(won[j]-1) / (games[j]-1);
						cnt++;
					}
					else if (mat[i][j] == '1') {
						owp[i] += double(won[j]) / (games[j]-1);
						cnt++;
					}
				}
			}
			
			if (cnt > 0) owp[i] /= cnt;
			
			//cout << owp[i] << ' ';
		}
		//cout << endl;
		
		double oowp[n];
		for (int i = 0; i < n; ++i) {
			oowp[i] = 0;
			int cnt = 0;
			for (int j = 0; j < n; ++j) {
				if (i != j && mat[i][j] != '.') {
					oowp[i] += owp[j];
					cnt++;
				} 
			}
			
			if (cnt > 0) oowp[i] /= cnt;
			//cout << oowp[i] << ' ';
		}
		//cout << endl;
		
		
		cout << "Case #" << t << ":\n";
		for (int i = 0; i < n; ++i) {
			cout << setprecision(12) << (0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]) << "\n";
		}
	}
	return 0;
}




























