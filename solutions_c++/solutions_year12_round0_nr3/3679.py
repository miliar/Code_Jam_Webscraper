#include <iostream>
#include <stdio.h>
#include <set>
#include <queue>
#include <map>
using namespace std;
int N;
char graph[40][41];
int ones[40];

int main()
{
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		int A, B, count = 0;
		cin >> A >> B;
		int t = A, downbase = 1, len = 0;
		while (t)
		{
			t /= 10;
			downbase *= 10;
			len++;
		}
		for (int n = A; n < B; n++)
		{
			int saved[10], size = 0;
			if (n == 1212) {
				int a = 1;
			}
			for (int l = 1, base = 10, dbase = downbase / 10; l < len; l++, base *= 10, dbase /= 10)
			{
				int back = n % base, front = n / base;
				if (back == 0) continue;
				int m = back * dbase + front;
				if (m >= A && m <= B && m > n) 
				{
					int p;
					for (p = 0; p < size; p++)
						if (saved[p] == m) break;
					if (p == size)
					{
						saved[size++] = m;
						count++;
						//cout << n << ' ' << m << endl;
					}
				}
			}
		}
		cout << "Case #" << cases << ": " << count << endl;

	}
	return 0;
}

