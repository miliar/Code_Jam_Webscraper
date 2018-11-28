#include <iostream>
#include <map>
#include <string>
#include <boost/foreach.hpp> // http://www.boost.org

using namespace std;

#define foreach BOOST_FOREACH

typedef long long Long;

const int N = 2 * 3 * 5 * 7;

struct State
{
	int sum; // mod N
	int buf; // mod N
public:
	State(int sum, int buf) : sum(sum), buf(buf) { }
	State() { }
public:
	bool operator <(const State &other) const
	{
		if(sum != other.sum) { return sum < other.sum; }
		if(buf != other.buf) { return buf < other.buf; }
		return false;
	}
};

bool is_ugly(int n)
{
	return (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0);
}

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		string s;
		cin >> s;

		map<State,Long> ans;
		map<State,Long> tmp;

		typedef pair<State,Long> Pair;

		ans[State(N, 0)] = 1;

		foreach(const char& ch, s) {
			tmp.clear();

			foreach(const Pair& p, ans) {
				int sum = p.first.sum;
				int buf = p.first.buf;
				int num = (buf * 10 + static_cast<int>(ch - '0')) % N;
				tmp[State((sum + num) % N, N)] += p.second;
				if(sum != N) { tmp[State((sum - num + N) % N, N)] += p.second; }
				tmp[State(sum, num)] += p.second;
			}

			swap(ans, tmp);
		}

		Long out = 0;

		foreach(const Pair& p, ans) {
			int sum = p.first.sum;
			int buf = p.first.buf;
			if(is_ugly(sum) && buf == N) { out += p.second; }
		}

		cout << "Case #" << iCase << ": " << out << endl;
	}

	return 0;
}
