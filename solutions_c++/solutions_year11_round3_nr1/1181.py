/*
ID: ahaigh1
PROG: A
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <memory>
#include <set>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <limits>
#include <map>
#include <bitset>
#include <ctime>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
#define eps (1e-10)
#define inf (1<<30)
#define ll long long
#define MP make_pair

int gcd(int a, int b) { return (b)?gcd(b, a % b):a; } //gcd

int t, r, c;
char row[55][55];

int main() {
	cin >> t;
	REP(i, t) {
		bool flag = false;
		cin >> r >> c;
		REP(j, r) cin >> row[j];
		
		REP(j, r) { 
			REP(k, c) if (row[j][k] == '#') { 
				//cout << j << " " << k << endl;
				//must colour this red
				if (j+1==r || k+1==c || row[j+1][k] != '#' || row[j+1][k+1] != '#' || row[j][k+1] != '#') flag = true;
				else { 
					row[j][k] = row[j+1][k+1] = '/'; row[j][k+1] = row[j+1][k] = '\\';
				}
			}
			
			//REP(j, r) cout << row[j] << endl; cout << endl;
		}
		
		
		cout << "Case #" << (i+1) << ":" << endl;
		if (!flag) {
			REP(j, r) cout << row[j] << endl;
		} else { 
			cout << "Impossible" << endl;
		}
	}
}