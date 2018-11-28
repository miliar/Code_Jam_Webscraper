#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("B-large.in", "rt" ,stdin);
	freopen("B-large.out", "wt", stdout);
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		int n, s, p;
		cin >> n >> s >> p;
		int count = 0, x1 = 2*(p-2)+p, x2 = x1 + 1;
		for (int j=0; j<n; j++)
			{
				int x;
				cin >> x;
				if (p <= x && (p - (x-p)/2 <= 1))
				{
					count++;
					continue;
				}
				if (p <= x && (p - (x-p)/2 <= 2))
					if (s-->0)
						count++;
			}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}