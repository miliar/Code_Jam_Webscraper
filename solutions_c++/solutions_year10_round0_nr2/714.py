#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <map>
using namespace std;
#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 

#include "ttmath.h"

template<class T>
T gcd(T a, T b)
{
	if (a>b)
		return gcd(b,a);

	if (a==0)
		return b;

	return gcd(b%a, a);
}

// BEGIN CUT HERE
int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	typedef ttmath::Int<8> int_; 
	int T;
	cin >> T;

	int t = 0;

	while(T--)
	{
		int N;

		cin >> N;

		std::vector<int_> numbers;

		for(int i = 0; i < N; ++i)
		{
			string s;
			cin >> s;
			int_ n(s);
			numbers.push_back(n);
		}

		sort(ALL(numbers));

		std::vector<int_> numbers_diff;

		for(int i=0;i<numbers.size()-1;++i)
			numbers_diff.push_back(numbers[i+1]-numbers[i]);

		int_ g = numbers_diff[0];

		for(int i = 1;i<numbers_diff.size();++i)
			g = gcd(g, numbers_diff[i]);

		int_ res = 0;


		if (numbers[0] % g != 0)
		{
			int_ one = 1;
			int_ t = (one + numbers[0] / g) * g;
			res = t - numbers[0];
		}


		cout << "Case #" << ++t << ": " << res << "\n";
	}


}
// END CUT HERE
