#include <iostream>
#include <queue>
using namespace std;

int main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int r,k,n;
		cin >> r >> k >> n;
		queue <int> q1;
		queue <int> q2;
		int g;
		for (int i = 0; i < n; i++)
		{
			cin >> g;
			q1.push(g);
		}

		int tot = 0;
		int rides = 0;
		int num = 0;
		while (rides < r)
		{
			while (!q2.empty())
			{
				q1.push(q2.front());
				q2.pop();
			}
			while (true)
			{
				if (q1.empty()) break;
				if (num + q1.front() > k) break;
				num += q1.front();
				q2.push(q1.front());
				q1.pop();
			}	
			tot += num;
			rides++;
			num = 0;
		}
		cout << "Case #" << T << ": " << tot << "\n";
	}
	return 0;
}
