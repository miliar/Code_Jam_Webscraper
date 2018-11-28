#include <cstdio>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

typedef long long ll;

using namespace std;

static void get_max(ll total, ll &nons_max, ll &s_max)
{
	int mod3 = total % 3;
	ll div3  = total / 3;
	switch(mod3) {
	case 0:
		nons_max = div3;
		s_max = div3 + 1;
		break;
	case 1:
		nons_max = div3 + 1;
		s_max = nons_max;
		break;
	case 2:
		nons_max = div3 + 1;
		s_max = nons_max + 1;
		break;
	}
	s_max = std::min(total, s_max);
}

static ll solve_b(ll N, ll S, ll P, vector<ll> &ts)
{
	ll cnt_ns = 0;
	ll cnt_s = 0;
	for(int i=0; i<ts.size(); i++) {
		ll nsmax, smax;	
		get_max(ts[i], nsmax, smax);		
		if (nsmax >= P) {
			cnt_ns++;
		} else if (smax >= P) {
			cnt_s++;
		}
	}
	return cnt_ns + std::min(S, cnt_s);
}

int main(int argc, char *argv[])
{
	int num;
	if (argc < 2) {
		return -1;
	}
	std::ifstream ifs(argv[1]);
	if (!ifs.is_open()) return -1;
	std::string ofilename = std::string(argv[1]) + ".out";
	std::ofstream ofs(ofilename.c_str());
	ifs >> num;
	for(int c=1; c<=num; c++) {
		ll n, s, p;
		vector<ll> ts;
		ifs >> n >> s >> p;
		for(int i=0; i<n; i++) {
			int t;
			ifs >> t;
			ts.push_back(t);
		}
		cout << "Solving " << c << std::endl;
		ll ans = solve_b(n, s, p, ts);
		ofs << "Case #" << c << ": " << ans << std::endl;
	}

	return 0;
}
