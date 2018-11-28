#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

class TaskC
{
	string line;
	static const string sample;
	static const MOD = 10000;
public:
	void Solve(int nCase)
	{
		getline(cin, line);

		vector<vector<int> > a(line.size(), vector<int>(sample.size(), 0)); // a[i, j] - number of sequences of sample[0:j] ending in line[i];

		for (int i=0; i<line.size(); ++i)  a[i][0] = line[i]==sample[0];

		for (int j=1; j<sample.size(); ++j)
		for (int i=0; i<line.size(); ++i)
			if (line[i]==sample[j])
				for (int k=0; k<i; ++k)  ( a[i][j] += a[k][j-1] ) %= MOD;

		int res = 0;
		for (int i=0; i<line.size(); ++i)  ( res += a[i][sample.size()-1] ) %= MOD;

		cout << "Case #" << nCase << ": " << setw(4) << setfill('0') << res << endl;
	}
};

const string TaskC::sample = "welcome to code jam";

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	TaskC sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}