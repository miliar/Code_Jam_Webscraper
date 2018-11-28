#include <iostream>
#include <vector>
#include <string>
using namespace std;

class ProblemA
{
	vector<int> X;
public:
	void ReadData()
	{
		int N;  cin >> N;
		X.resize(N);
		for (int i=0; i<N; ++i)
		{
			string s;  cin >> s;
			X[i] = s.find_last_of('1')==string::npos ? 0 : s.find_last_of('1')+1;
		}
	}
	void Solve(int nCase)
	{
		ReadData();

		int res = 0;
		for (int i=0; i<X.size(); ++i)
		{
			int j=i;
			while (X[j]>i+1)  ++j;
			while (j-->i)
			{
				swap(X[j], X[j+1]);
				++res;
			}
		}

		cout << "Case #" << nCase << ": " << res << endl;
	}
};

int main()
{
	int N;  cin >> N;
	ProblemA sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}