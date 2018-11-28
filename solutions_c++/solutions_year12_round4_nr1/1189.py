#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int d[10010] , l[10010];
int f[10010];
int n;

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("O.txt" , "w" , stdout);
	int ctest;
	cin >> ctest;
	for (int test = 1 ; test <= ctest ; test ++)
	{
		cout << "Case #" << test << ": ";		
		cin >> n;
		for (int i = 1 ; i <= n ; i ++)
			cin >> d[i] >> l[i];
		cin >> d[n + 1];
		l[n + 1] = 1;
		n ++;
		f[0] = 0;
		f[1] = min(d[1] , l[1]);
		for (int i = 2 ; i <= n ; i ++)
		{
			f[i] = 0;
			for (int j = 1 ; j < i ; j ++)
				if (d[j] + f[j] >= d[i])
					f[i] = max(f[i] , min(l[i] , d[i] - d[j]));
		}
		if (f[n] == 0)
			cout << "NO" << endl;
		else
			cout << "YES" << endl;
	}
	return 0;
}
