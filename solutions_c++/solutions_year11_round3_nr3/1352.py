//B.cpp
//_are89
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minEI(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxEI(x)  max_element(x.begin(),x.end())-(x).begin()

#define UNS(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acuSum(x)  accumulate(x.begin(),x.end(),0)
#define acuMul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>()); 
#define bits(x)     __builtin_popcount( x )

template<class F, class T> T convert(F input, int width = 0, int prec = -1) {
	stringstream A;
	T res;
	if (prec > -1)
		A << fixed << setprecision(prec);
	A << setw(width) << setfill('0') << input;
	A >> res;
	return res;
}

vector<string> split(string s) {
	stringstream A(s);
	vector<string> res;
	string t;
	while (A >> t)
		res.push_back(t);
	return res;
}
long long GCD(long long a, long long b) {
	if (b == 0)
		return a;
	return GCD(b, a % b);
}
long long LCM(int a, int b) {
	return b * a / GCD(a, b);
}
bool chk(vector<long long> v, long long n) {
	for (int i = 0; i < sz(v); i++)
		if (v[i] % n != 0 && n % v[i] != 0)
			return false;
	return true;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("output_C_S.txt", "wt", stdout);
#endif

	int tests;
	cin >> tests;
	for (int tc = 1; tc <= tests; tc++) {
		int n, low, high;
		cin >> n >> low >> high;
		vector<long long> v;
		for (int i = 0; i < n; i++) {
			long long nm;
			cin >> nm;
			v.pb(nm);
		}
		//sort(v.rbegin(),v.rend());
		long long res = -1;
		for (int k = low; k <= high; k++) {
			if (chk(v, k)) {
				res = k;
				break;
			}
		}

		if (res == -1)
			cout << "Case #" << tc << ": " << "NO" << endl;
		else
			cout << "Case #" << tc << ": " << res << endl;


	}

	return 0;
}

