#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}

int main(int argc, char* argv[])
{
	int x = 1^2^3^4^5;
	ifstream in("in");
	ofstream out("out");

	int T = 0;
	in >> T;

	REP (t, T)
	{
		int N = 0;
		in >> N;

		vector<int> v;
		REP (i, N)
		{
			int x = 0;
			in >> x;
			v.push_back(x);
		}

		int res = 0;
		REP (i, N)
			res ^= v[i];

		if (res != 0)
		{
			out << "Case #" << t+1 << ": NO" << "\n";
			continue;
		}

		int min = *min_element(v.begin(), v.end());
		int sum = accumulate(v.begin(), v.end(), 0);

		out << "Case #" << t+1 << ": " << sum - min << "\n";	
	}

	in.close();
	out.close();

	return 0;
}
