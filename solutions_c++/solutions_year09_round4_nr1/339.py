#include <iostream>
#include <string>

using namespace std;

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		int n;
		int input[64];
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			string s;
			cin >> s;
			int p;
			for (p = n; p > 1; p--)
				if (s[p-1] == '1')
					break;
			input[i] = p;
		}

		int larger[64] = {0};
		for (int i = 0; i < n; i++)
			for (int k = input[i]; k >= 0; k--)
				larger[k]++;
		
		int res = 0;
		while (n)
		{
			int k;
			for (k = n; k >= 1; k--)
				if (!(larger[k] <= n-k))
					break;
			for (int i = n-1; i >= 0; i--)
				if (input[i] >= k)
				{
					for (int j = input[i]; j >= 0; j--)
						larger[j]--;
					for (int j = i+1; j < n; j++)
					{
						swap(input[j-1], input[j]);
						res++;
					}
					break;
				}
			n--;
		}

		cout << "Case #" << kase << ": " << res << endl;
	}
	return 0;
}
