#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

const int MAX_N = 100 + 5;
int n;
int A[MAX_N][2], P[2], T[2];

int abs(int x)
{
	if (x < 0)
		return -x;
	else
		return x;
}

void solve(int NUM)
{
	P[0] = P[1] = 1;
	T[0] = T[1] = 0;
	for (int i = 0; i < n; ++i)
	{
	//	cout << T[0] << " " << T[1] << endl;
		int ind = A[i][0];
		int pos = A[i][1];
		T[ind] = max(T[!ind], T[ind] + abs(pos - P[ind])) + 1;
		P[ind] = pos;
	}
	
	int res = max(T[0], T[1]);
	printf("Case #%d: %d\n", NUM, res); 
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; ++j)
		{
			char c;
			int x;
			scanf(" ");
			scanf("%c %d", &c, &x);
			//cout << c << " " << x << endl;
			A[j][1] = x;
			A[j][0] = (c == 'O');
		}
		solve(i + 1);
	}
	return 0;
}
