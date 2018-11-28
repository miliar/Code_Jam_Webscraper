#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifstr("a-large.in");
	int T = 0;
	ifstr >> T;
	ofstream ofstr("a-large.out");
	for (int t = 0; t < T; ++t)
	{
		int N = 0, K = 0;
		ifstr >> N >> K;
		K %= 1 << N;
		string res = "ON";
		for (int i = 0; i < N; ++i)
			if ((K & (1 << i)) == 0)
			{
				res = "OFF";
				break;
			}

		cout << "Case #" <<  t + 1 << " passed.\n";
		ofstr << "Case #" <<  t + 1 << ": " << res << "\n";
	}
	return 0;
}