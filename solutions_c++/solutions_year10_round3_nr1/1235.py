#include<iostream>
#include<vector>

using namespace std;

struct interval
{
	int A, B;
};

int main()
{
	int T;
	cin >> T;

	vector<interval> intervals;

	for(int x = 1; x <= T; ++x)
	{
		int N;
		cin >> N;

		intervals.resize(N);

		for(int i = 0; i < N; ++i)
			cin >> intervals[i].A >> intervals[i].B;

		int y = 0;

		for(int i = 0; i < N - 1; ++i)
			for(int j = i + 1; j < N; ++j)
				if(intervals[i].A < intervals[j].A)
				{
					if(intervals[i].B > intervals[j].B)
						++y;
				}
				else
				{
					if(intervals[j].B > intervals[i].B)
						++y;
				}

		cout << "Case #" << x << ": " << y << "\n";
	}

	return 0;
}