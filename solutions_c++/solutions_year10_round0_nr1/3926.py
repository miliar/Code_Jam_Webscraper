#include<iostream>
using namespace std;

int main()
{
//	freopen("g:\\A-large.in", "r", stdin);
//	freopen("g:\\A-large.out", "w", stdout);
	int testnum;
	cin >> testnum;
	for (int ti = 1; ti <= testnum; ++ti)
	{
		int n, k;
		cin >> n >> k;
		printf("Case #%d: ", ti);
		bool res = true;
		for (int i = 1; i <= n; ++i)
			if (((1 << (i - 1)) & k) == 0)
				res = false;

		if (res)
			printf("ON\n");
		else 
			printf("OFF\n");
	}

	return 0;
}