#include <iostream>
#include <bitset>

#include <fstream>


using namespace std;


int main() {
	const int bsSize = 32;
	int T;
	ifstream inF;
	inF.open("A-large.in");
	ofstream outF;
	outF.open("A-large.out");
	inF >> T;
	for (int tests = 0; tests < T; ++tests)
	{
		int N, K;
		inF >> N >> K;
		bitset<bsSize> bs (K);

		bool on = true;

		for(int i=0; i<N; ++i)
			if (!bs.test(i))
			{
				on = false;
				break;
			}

		outF << "Case #" << tests+1 << ": " << ((on)?"ON":"OFF") << endl;
	}

	inF.close();
	outF.close();
	return 0;
}