#include<iostream>

using namespace std;

int search(int *ar, int r, int n)
{
	for (int i = r; i < n; i++)
	{
		if (ar[i] < r) return i;
	}
}

int main()
{
	int t;
	cin >> t;
	for (int l = 1; l <= t; l++)
	{
		int n;
		cin >> n;
		int *ar;
		ar = new int[n];
		for (int i = 0; i < n; i++)
		{
			string s;
			cin >> s;
			bool flag = false;
			for (int k = s.size() - 1; k >= 0; k--)
			{
				if (s[k] == '1') 
				{
					ar[i] = k;
					flag = true;
					break;
				}
			}
			if (!flag) ar[i] = 0;
		}
		int x = 0;
		for (int i = 0; i < n - 1; i++) 
		{
			int k;
			if (ar[i] > i)
			{
				k = search(ar, i + 1, n);
				for (int j = 0; j < k - i; j++)
				{
					swap(ar[k - j], ar[k - j - 1]);
					x++;
				}
			}
		}
		cout << "Case #" << l << ": " << x << endl;
	}
	return 0;
}
