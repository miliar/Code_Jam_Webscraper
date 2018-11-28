#include <fstream>
#include <vector>
#include <queue>

using namespace std;

int solve(int R, int k, vector <int> &groups)
{
	queue <int> q;

	for (int i = 0; i < (int) groups.size(); i++)
		q.push(groups[i]);

	queue <int> q1;

	int total = 0;

	while (R > 0)
	{
		while (!q1.empty())
		{
			q.push(q1.front());
			q1.pop();
		}

		int passengers = 0;

		while (!q.empty() && passengers + q.front() <= k)
		{
			passengers += q.front();
			q1.push(q.front());
			q.pop();
		}

		total += passengers;
		R--;
	}

	return total;
}

int main()
{
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");

	int T;
	fin >> T;

	for (int i = 1; i <= T; i++)
	{
		int R, k, N;

		fin >> R >> k >> N;

		vector <int> groups(N);

		for (int j = 0; j < N; j++)
			fin >> groups[j];

		fout << "Case #" << i << ": " << solve(R, k, groups) << endl;
	}

	return 0;
}
