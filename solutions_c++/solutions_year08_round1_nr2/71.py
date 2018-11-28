#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>
#include <set>
using namespace std;

int main()
{
	int C;
	cin >> C;

	for(int i = 1; i <= C; ++i)
	{
		int N;
		cin >> N;
		int M;
		cin >> M;

		vector<vector<int> > custs;
		vector<int> custs1;
		custs.resize(M);
		custs1.resize(M);

		for(int j = 0; j < M; ++j)
		{
			int T;
			cin >> T;
			custs1[j] = -1;
			for(int k = 0; k < T; ++k)
			{
				int X;
				int Y;
				cin >> X >> Y;
				--X;
				if (Y==0)
				{
					custs[j].push_back(X);
				}
				else
				{
					custs1[j] = X;
				}
			}
		}

		vector<int> ans;
		ans.resize(N);

		{
next1:;

			for(int j = 0; j < M; ++j)
			{
				if (custs1[j] >= 0 && ans[custs1[j]] == 1)
					continue;

				for(int k = 0; k < (int)custs[j].size(); ++k)
				{
					if (ans[custs[j][k]] == 0)
						goto next;
				}

				if (custs1[j] < 0)
				{
					cout << "Case #" << i << ": IMPOSSIBLE" << endl;
					goto nextcase;
				}
				ans[custs1[j]] = 1;
				goto next1;
next:;
			}
			cout << "Case #" << i << ':';
			for(int j = 0; j < N; ++j)
			{
				cout << ' ' << ans[j];
			}
			cout << endl;
		}

nextcase:;
	}
}