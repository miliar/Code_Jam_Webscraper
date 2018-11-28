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



// BEGIN CUT HERE
int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	int T;
	cin >> T;

	int t = 0;

	while(T--)
	{
		int N, K;
		cin >> N >> K;

		int num = K % (1<<N);

		bool res = true;

		for(int i = 0; i < N; ++i)
		{
			if ((num & 1)==0)
				res=false;
			num>>=1;
		}

		cout << "Case #" << ++t << ": " << (res?"ON":"OFF") << "\n";
	}


}
// END CUT HERE
