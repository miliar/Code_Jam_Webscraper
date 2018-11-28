#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>

using namespace std;

class TaskB
{
	int T;
	vector<int> dep[2], arr[2];
public:
	void ReadData()
	{
		int N[2];
		cin >> T >> N[0] >> N[1];
		for (int d=0; d<2; ++d)
		{
			dep[  d].resize(N[d]);
			arr[1-d].resize(N[d]);
			for (int i=0; i<N[d]; ++i)
			{
				int h, m;  char c;
				cin >> h >> c >> m;  dep[  d][i] = h*60+m;
				cin >> h >> c >> m;  arr[1-d][i] = h*60+m;
			}
		}
	}
	void Solve(int nCase)
	{
		ReadData();

		int bus[2] = {0, 0};
		for (int d=0; d<2; ++d)
		{
			sort(dep[d].begin(), dep[d].end());
			sort(arr[d].begin(), arr[d].end());
			int free = 0;
			for (int i=0, j=0; i<dep[d].size(); ++i)
			{
				for (; j<arr[d].size() && arr[d][j]+T<=dep[d][i]; ++j)  ++free;
				if (free)  --free;  else  ++bus[d];
			}
		}

		cout << "Case #" << nCase << ": " << bus[0] << " " << bus[1] << endl;;
	}
};

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;

	TaskB sol;  for (int i=1; i<=N; ++i)  sol.Solve(i);

	return 0;
}