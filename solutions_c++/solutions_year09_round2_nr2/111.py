#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	int ti;
	for (ti = 1;ti <= t;ti++)
	{
		string N;
		cin >> N;

		printf("Case #%d: ", ti);

		string N2 = N;
		if (next_permutation(N2.begin(), N2.end()))
			cout << N2 << endl;
		else
		{
			N += '0';
			sort(N.begin(), N.end());
			int i;
			for (i = 0;i < N.size();i++)
				if (N[i] != '0')
					break;
			swap(N[0], N[i]);
			cout << N << endl;
		}
	}
	return 0;
}
