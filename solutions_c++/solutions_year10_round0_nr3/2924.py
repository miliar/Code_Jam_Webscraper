#include <deque>
#include <fstream>
using namespace std;

int main()
{
	int nCases, r, k, n, index, input, sum, profit;
	deque<int> q;

	ifstream fin("C-small.in");
	ofstream fout("C-small.out");

	fin >> nCases;

	for (int currentCase = 1; currentCase <= nCases; currentCase++)
	{
		fin >> r >> k >> n;
		sum = profit = 0;
		q.clear();

		for (index = 0; index < n; index++)
		{
			fin >> input;
			sum += input;
			q.push_back(input);
		}

		if (sum <= k)
			profit = r * sum;
		else
			for (index = 0; index < r; index++)
			{
				sum = 0;

				while ((sum + q.front()) <= k)
				{
					sum += q.front();

					q.push_back(q.front());
					q.pop_front();
				}
				
				profit += sum;
			}

		fout << "Case #" << currentCase << ": " << profit << endl;
	}

	return 0;
}