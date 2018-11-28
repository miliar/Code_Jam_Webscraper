#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

class ProblemA
{
	int P, K, L;
	vector<long long> freq;
public:
	void ReadData()
	{
		cin >> P >> K >> L;
		freq.resize(L);  for (int i=0; i<L; ++i)  cin >> freq[i];
	}
	void Solve(int nCase)
	{
		ReadData();

		sort(freq.rbegin(), freq.rend());
		long long res = 0;
		for (int l=0, p=0, k=0; l<L; ++l)
		{
			res += freq[l]*(p+1);
			if (++k==K)  ++p, k=0;
		}

		cout << "Case #" << nCase << ": " << res << endl;
	}
};

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	ProblemA sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}