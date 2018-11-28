#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b)
{
	if(b == 0) return a;
	else gcd(b, a%b);
}

int main()
{
	int C, N, i, k;
	long long t[3] = {0};
	long long dif[2] = {0};
	long long j;
	long long small, tmp;


	cin >> C;

	for(i = 0; i < C; ++i)
	{
		cin >> N;
		for(j = 0; j < N; ++j)
			cin >> t[j];
		if(N < 3) t[2] = 0;

		sort(t, t+3);

		dif[0] = t[2] - t[1];
		if(N == 3) dif[1] = t[1] - t[0];
		else dif[1] = 0;
		
		if(dif[0] > dif[1]) tmp = gcd(dif[0], dif[1]);
		else tmp = gcd(dif[1], dif[0]);

		if(tmp == 1) tmp = 0;
		else
		{
			if(N == 3)
				small = t[0];
			else
				small = t[1];

			j = 1;
			while(tmp*j++ < small);
			tmp = tmp*(j-1) - small;
		}
		cout << "Case #" << i+1 << ": " << tmp << endl;
	}
	return 0;
} 