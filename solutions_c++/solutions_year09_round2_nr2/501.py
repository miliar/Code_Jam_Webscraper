#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
using namespace std;

class ProblemB
{
public:
	void Solve(int nCase)
	{
		string N;  cin >> N;

		if (!next_permutation(N.begin(), N.end()))
		{
			N = "0"+N;
			int pos = N.find_first_not_of('0');
			N = N[pos] + N.substr(0, pos)+N.substr(pos+1);
		}

		cout << "Case #" << nCase << ": " << N << endl;
	}
};

int main()
{
	int N;  cin >> N;
	ProblemB sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}