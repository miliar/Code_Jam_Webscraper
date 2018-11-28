#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

#define pii pair< int, int >

ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout

int t, test = 1;
int x, n, s, r;
double tim;
pii stair[2000];

int main() {
	for( cin >> t; t--; ) {
		cin >> x >> s >> r >> tim >> n;
		for( int i = 0; i < n; i++ ) {
			int b, e;
			cin >> b >> e >> stair[i].first;
			stair[i].second = e - b;
			x -= stair[i].second; 
		}
		stair[n].first = 0;
		stair[n].second = x;
		n++;
		sort( stair, stair + n );
		double res = 0.;
		for( int i = 0; i < n; i++ ) {
			double req = (double)stair[i].second / (r + stair[i].first);
			if( req > tim ) {
				double len = stair[i].second - tim * (r + stair[i].first);
				res += tim + len / (s + stair[i].first);
				tim = 0;
			} else {
				res += req;
				tim -= req;
			}
		}
		cout.precision( 7 );
		cout.setf(ios::fixed | ios::showpoint );
		cout << "Case #" << test++ << ": " << res << endl;
	}
	return 0;
}