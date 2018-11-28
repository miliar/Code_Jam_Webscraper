#include <iostream>
#include <vector>
using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for(int c = 1; c <= T; c++)
	{
		int n, k;
		cin >> n >> k;
		vector<int> v(n, 0);
		int p2 = 2;
		for(int i = 1; i < n; i++)
		{
			p2 *= 2;
		}
		int k2 = k % p2;
		int j = 0;
		while(k2 > 0)
		{
			v[j] = k2 % 2;
			j++;
			k2 /= 2;
		}
		//v.push_back(1);
		bool res = 1;
		for(int i = 0; i < v.size(); i++)
		{
			if(v[i] == 0)
			{
				res = 0;
				break;
			}
		}

		cout << "Case #" << c << ": ";
		if(res == 0)
			cout << "OFF" << endl;
		else
			cout << "ON" << endl;
	}
	return 0;
}