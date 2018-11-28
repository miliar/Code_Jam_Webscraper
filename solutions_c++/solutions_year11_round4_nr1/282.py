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

ifstream fin("A_Airport Walkways.in");
ofstream fout("A_Airport Walkways.out");

#define cin fin
#define cout fout
#define P pair<double, double>
int n;
double x, s, r, t;
P arr[1010];

int main(){
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> x >> s >> r >> t >> n;
		r -= s;
		double a, b;
		for(int i = 0; i < n; i++){
			cin >> a >> b >> arr[i].first;
			arr[i].second = b - a;
			arr[i].first += s;
			x -= b - a;
		}
		arr[n++] = P(s, x);
		sort(arr, arr + n);
		double res = 0;
		for(int i = 0; i < n; i++){
			double tmp = min(t, arr[i].second / (arr[i].first + r));
			res += tmp;
			t -= tmp;
			double diff = tmp * (arr[i].first + r);
			res += (arr[i].second - diff) / arr[i].first;
		}
		cout.precision(7);
		cout.setf(ios::fixed | ios::showpoint);
		cout << "Case #" << ++test << ": " << res << endl;
	}
	return 0;
}
	
