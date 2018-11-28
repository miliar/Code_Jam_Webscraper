#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int T = 0;
		cin >> T;
		int NA = 0, NB = 0;
		cin >> NA >> NB;

		vector<int> arrA(NB), arrB(NA), depA(NA), depB(NB);
		int ca = 0, cb = 0;

		for (int j = 0; j < NA; j++)
		{
			int hour, minute;
			char t;
			cin >> hour >> t >> minute;
			depA[j] = hour * 60 + minute;

			cin >> hour >> t >> minute;
			arrB[j] = hour * 60 + minute + T;
		}

		for (int j = 0; j < NB; j++)
		{
			int hour, minute;
			char t;
			cin >> hour >> t >> minute;
			depB[j] = hour * 60 + minute;
			cin >> hour >> t >> minute;
			arrA[j] = hour * 60 + minute + T;
		}

		sort(arrA.begin(), arrA.end());
		sort(arrB.begin(), arrB.end());
		sort(depA.begin(), depA.end());
		sort(depB.begin(), depB.end());

		int cur = 0, cs = 0;
		for (int j = 0; j < NA; j++)
		{
			int t = depA[j];
			while (cs < NB && arrA[cs] <= t)
			{
				cs++;
				cur++;
			}

			if (cur <= 0)
				ca++;
			else
				cur--;
		}
		cur = 0; cs = 0;
		for (int j = 0; j < NB; j++)
		{
			int t = depB[j];
			while (cs < NA && arrB[cs] <= t)
			{
				cs++;
				cur++;
			}

			if (cur <= 0)
				cb++;
			else
				cur--;
		}
		cout << "Case #" << (i+1) << ": " << ca << ' ' << cb << endl;
	}
	return 0;
}

