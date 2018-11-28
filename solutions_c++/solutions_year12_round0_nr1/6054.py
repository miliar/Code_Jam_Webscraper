// In the name of God
#include <algorithm>
#include <iostream>
#include <complex>
#include <cstdlib>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;


typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef complex<double> point;

#define error(x) cerr << #x << " = " << x << endl;

#define X first
#define Y second
// #define X real()
// #define Y imag()

const double eps = 1e-8;
char mp[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};



int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	string c;
	getline(cin, c);
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		string s;
		getline(cin, s);
		for (int i = 0; i < int(s.size()); i++) {
			if (s[i] != ' ')
				s[i] = mp[s[i] - 'a'];
		}
		cout << s << endl;
	}



	return 0;
}
