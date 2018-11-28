#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

/// is bulb ON ?
inline bool solve_snapper_case(long long N, long long K)
{
	return K % (1 << N) == ((1 << N)-1);
}

void solve_snapper(istream & in, ostream & out)
{
	int T;
	long long N, K;
	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		in >> N >> K;
		bool isON = solve_snapper_case(N,K);
		out << "Case #" << t << ": " << (isON?"ON":"OFF") << "\n";
	}
}

int main()
{
	assert(sizeof(long long) == 8);
	//ifstream small("A-sample.in");
	//ofstream small_out("A-sample.txt");
	//ifstream small("A-small-attempt0.in");
	//ofstream small_out("A-small-out.txt");
	ifstream small("A-large.in");
	ofstream small_out("A-large-out.txt");

	solve_snapper(small,small_out);

	return 0;
}