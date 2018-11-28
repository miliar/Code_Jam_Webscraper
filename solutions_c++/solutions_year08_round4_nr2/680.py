#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

class ProblemB
{
	int N, M, A;
public:
	void ReadData()
	{
		cin >> N >> M >> A;
	}
	void SolveSmall(int nCase)
	{
		ReadData();

		cout << "Case #" << nCase << ": ";

		long long x1, x2, y1, y2;
		for (x2=1; x2<=N; ++x2)  for (y2=1; y2<=M; ++y2)
		for (x1=0; x1<=x2; ++x1)  for (y1=0; y1<=y2; ++y1)
			if (A==x2*y2-x1*y1)  goto ok;

		cout << "IMPOSSIBLE" << endl;
		return;
ok:     cout << 0 << " " << 0 << " " << x1 << " " << y2 << " " << x2 << " " << y1 << endl;
	}
};

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	ProblemB sol;	for (int i=1; i<=N; ++i)  sol.SolveSmall(i);
	return 0;
}