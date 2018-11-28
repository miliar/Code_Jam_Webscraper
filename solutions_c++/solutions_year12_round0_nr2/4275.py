#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;


int main()
{
	long long t, n, p, k, s, b, m, ms;
	vl v;
	cin >> t;
	for(long long i = 0; i < t; i++) {
		long long res = 0;

		cin >> n >> s >> p;
	
		for(long long j = 0; j < n; j++) {
			cin >> b;
			m = (b + 2) / 3;
			ms = (b + 1) / 3 + 1;
			if (b == 0) ms = 0;
			if (m >= p) res++;
			else if(ms >= p && s > 0) {
				res++;
				s--;
			}
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}


	return 0;
}
