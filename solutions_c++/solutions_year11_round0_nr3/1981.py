#include <iostream>
#include <algorithm>
using namespace std;

const int N = 1005;
int c[N];

int main()
{
	int n;
	int cases;
	int s = 0;

	freopen("C:\\Users\\Haojian\\Desktop\\C-large.in", "r", stdin);
	freopen("C:\\Users\\Haojian\\Desktop\\output.txt", "w", stdout);
	cin >> cases;
	while (cases--)
	{
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> c[i];

		sort(c, c+n);
		int tmp = 0;
		int tmp1 = 0;
		for (int i = 1; i < n; i++)
		{
			tmp = tmp ^ c[i];
			tmp1 += c[i];
		}
		s++;

		if (tmp == c[0])
			printf("Case #%d: %d\n", s, tmp1);
		else
		    printf("Case #%d: NO\n", s);
	}

	return 0;
}