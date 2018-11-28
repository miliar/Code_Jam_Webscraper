#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <limits>

using namespace std;

int T;
int P;
vector<int> M;
vector< vector<int> > prices;

int Solve(size_t left, size_t right, int depth)
{
	if (depth == P)
		return 0;

	int minimum = numeric_limits<int>::max();
	for (size_t i = left; i != right; ++i)
		minimum = min(minimum, M[i]);

	int result = 0;

	if (minimum < P - depth)
		++result;

	result += Solve(left, (left + right)/2, depth+1);
	result += Solve((left + right)/2, right, depth+1);

	return result;
}

int main()
{
	ifstream input("TestInput.txt");
	ofstream output("TestOutput.txt");
	input >> T;

	for (int i = 0; i != T; ++i) {
		input >> P;
		M.resize(1 << P);
		for (size_t j = 0; j != M.size(); ++j)
			input >> M[j];
		prices.resize(P);
		for (int j = 0; j != P; ++j) {
			prices[j].resize(1 << (P-j-1));
			for (size_t k = 0; k != prices[j].size(); ++k)
				input >> prices[j][k];
		}

		output << "Case #" << i+1 << ": " << Solve(0, M.size(), 0) << endl;
	}

	return 0;
}