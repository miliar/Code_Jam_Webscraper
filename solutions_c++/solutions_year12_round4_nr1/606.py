#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

ll reach[10001];

bool solve(const VI& d, const VI& l, int D)
{
	int N = d.size();
	memset(reach, 0, sizeof(reach));
	reach[0] = d[0];
	for (int i = 0; i < N; i++) {
		ll r = reach[i];
		if (r == 0)
			return false;
		if (d[i] + r >= D)
			return true;
		for (int j = i+1; j < N && d[j] <= d[i] + r; j++)
			reach[j] = max<ll>(reach[j], min<ll>(l[j], d[j] - d[i]));
	}
	return false;
}

int main(int argc, const char* argv[])
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int N;
		VI d, l;
		int D;
		cin >> N;
		for (int j = 0; j < N; j++) {
			int x, y;
			cin >> x >> y;
			d.push_back(x);
			l.push_back(y);
		}
		cin >> D;
		cout << "Case #" << i << ": " << (solve(d, l, D) ? "YES" : "NO") << endl;
//		for (int j = 0; j < N; j++)
//			cout << "reach[" << j << "] = " << reach[j] << endl;
	}
    return 0;
}
