#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	int T;
	in >> T;
	for(unsigned t = 0; t < T; ++t)
	{
		int N, K;
		in >> N >> K;

		bool yes = (K & ((1 << N) - 1)) == ((1 << N) - 1);

		cout << "Case #" << (t + 1) << ": " << (yes ? "ON" : "OFF") << endl;
	}
	return 0;
}

