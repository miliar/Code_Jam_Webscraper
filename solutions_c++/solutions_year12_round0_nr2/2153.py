//============================================================================
// Name        : dancing_with_the_googlers.cpp
// Author      : Yoram Versluis
//============================================================================
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv) {

	if (argc < 2) {
		cerr << "Usage: " << argv[0] << " <input_file>" << endl;
		return 1;
	}

	ifstream input(argv[1]);
	if (!input.is_open()) {
		cerr << "error opening " << argv[1] << endl;
		return 1;
	}

	//now the real work
	int testCases = 0;
	int N, S, P, c;
	N = S = P = c = 0;

	input >> testCases;
	cerr << "testCases: " << testCases << endl;

	while (input.good() && c < testCases) {
		c++;
		input >> N >> S >> P;
		cerr << N << " " << S << " " << P << " ";
		int result = 0;
		for (int i = 0; i < N; i++) {
			int score;
			input >> score;
			cerr << score << " ";
			int avg = score / 3;
			int mod = score % 3;
			int max = avg + mod;
			if (avg >= P)
				result++;
			else {
				if (max > P)
					result++;
				if (max == P && mod == 1)
					result++;
				if (max == P && mod == 2 && S > 0) {
					//a surprising score is needed
					S--;
					result++;
				}
				if (avg > 0 && avg + 1 == P && mod == 0 && S > 0) {
					//a surprising score is needed
					S--;
					result++;
				}
			}
			cerr << ": " << score << ":" << result << ":" ;
		}
		cout << "Case #" << c << ": " << result  << endl;
	}

	return 0;
}
