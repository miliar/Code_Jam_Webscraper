#include <iostream>
#include <cstdio>
#define Max 100
using namespace std;

int T, n, s, p;
int a[Max];
int b[Max][3];

int main()
{
	//freopen("B-large.in", "r", stdin);
	
//	for (int sum = 0; sum <= 30; sum++)
//	{
//		cout << "sum: " << sum << endl;
//		for (int i = 0; i <= 10; i++)
//		for (int j = i; j <= 10; j++)
//		for (int k = j; k <= 10; k++)
//		if (i + j + k == sum && k - i <= 2)
//		{
//			printf("%d %d %d\n", i, j, k);
//		}
//	}
	
	cin >> T;
	for (int test = 0; test < T; test++)
	{
		cin >> n >> s >> p;
		int r = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			b[i][0] = a[i] / 3;
			b[i][1] = (a[i] - b[i][0]) / 2;
			b[i][2] = a[i] - b[i][0] - b[i][1];
			
			int m = max(b[i][0], max(b[i][1], b[i][2]));
			if (m >= p) r++;
			else if (s > 0 && m > 0 && m == p - 1 && (a[i] % 3) != 1)
			{
				r++;
				s--;
			}
		}
				
		printf("Case #%d: %d\n", test + 1, r);
	}
	
	return 0;
}
