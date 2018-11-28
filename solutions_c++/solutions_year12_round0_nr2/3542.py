#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void load(vector<int> &vm1, vector<int> &vm2)
{
	for (int i = 0; i <= 30; i ++)
	{
		for (int j = 0; j <= 10; j ++)
		{
			for (int k = j; k <= j+2; k ++)
			{
				if (k > 10) continue;
				for (int h = k; h <= k+2; h ++)
				{
					if (h > 10) continue;
					if (h-j > 2 || k-j > 2) continue;
					if (j+k+h == i)
					{
						if (h-j == 2 || k-j == 2)
							vm2[i] = max(vm2[i], h);
						else
							vm1[i] = max(vm1[i], h);
					}
				}
			}
		}
	}
}

int main(int argc, const char *argv[])
{
	vector<int> vm1(31, 0);
	vector<int> vm2(31, 0);
	load(vm1, vm2);
	//for (int i = 0; i <= 30; i ++)
	//{
	//	cout << i << ": " << vm1[i] << ", " << vm2[i] << endl;
	//}
	int T;
	cin >> T;
	for (int i = 0; i < T; i ++)
	{
		int N, S, p;
		cin >> N >> S >> p;
		vector<int> v(N);
		for (int j = 0; j < N; j ++)
			cin >> v[j];

		int r = 0;

		for (int j = 0; j < v.size(); j ++)
		{
			if (vm1[v[j]] >= p)
				r++;
			else if (vm2[v[j]] >= p && S > 0)
			{
				r++;
				S --;
			}
		}

		cout << "Case #" << i+1 << ": " << r << endl;
	}
	return 0;
}
