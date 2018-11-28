#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	unsigned int T, N, K;
	fin >> T;
	for (unsigned int i=1; i<=T; ++i)
	{
		fin >> N >> K;
		unsigned int max = 1<<N;
		unsigned int ans = K%max;
		bool on = (ans+1 == max);

		fout << "Case #" << i << ": " << (on ? "ON" : "OFF") << endl;
	}

	return 0;
}