#include <fstream>

using namespace std;

string solve(int N, int K)
{
	K = K % (1 << N);

	if (K == (1 << N) - 1)
		return "ON";

	return "OFF";
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;

	for (int i = 0; i < T; i++)
	{
		int N, K;
		fin >> N >> K;

		fout << "Case #" << (i + 1) << ": " <<
			solve(N, K) << endl;
	}

	return 0;
}
