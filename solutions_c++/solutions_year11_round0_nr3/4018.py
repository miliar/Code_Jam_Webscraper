#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int i=1; i<=N; i++)
	{
		int n;
		cin >> n;
		int v[n];
		for (int k=0; k<n; k++)
			cin >> v[k];

		int Max = (int) pow(2.0, (double)n);

		bool f=false;
		int res = 0;
		for (int k=1; k<Max-1; k++)
		{
			int Sean = 0, Patrick = 0, sum = 0;
			for (int l=0; l<n; l++)
			{
				if (k & (1 << l))
				{
					Sean = Sean ^ v[l];
					sum += v[l];
				}
				else
				{
					Patrick = Patrick ^ v[l];
				}
			}

			if (Sean == Patrick)
			{
				f = true;
				res = (res < sum) ? sum : res;
			}
		}

		cout << "Case #" << i << ": ";
		if (f)
			cout << res;
		else
			cout << "NO";
		cout << endl;
	}

	return 0;
}
