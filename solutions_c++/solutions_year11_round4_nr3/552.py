#include <iostream>
#include <string>
#include <algorithm>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;

#define N 1000000
typedef long long LL;

bool prime[N];
int p[100000];
int pcnt;


void GetPrime()
{
	memset(prime, true, sizeof(prime));
	
	prime[0] = prime[1] = false;
	
	for (int i = 4; i < N; i += 2)
		prime[i] = false;


	for (int i = 3; i < 1000; i += 2)
		if (prime[i])
			for (int j = i * i;  j < 1000000; j += 2*i)
				prime[j] = false;

	for (int i = 2; i < 1000000; ++i)
		if (prime[i])
			p[pcnt++] = i;

}




int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);


	GetPrime();
	int total;
	cin >> total;
	int n;
	
	for (int test = 1; test <= total; ++test)
	{
		LL ans = 0;
		cin >> n;
		if (1 == n)
			ans = 0;
		else ans = 1;

		for (int i = 0; i < pcnt && p[i] <= n; ++i)
		{
			LL tmp = n;
			int cnt = 0;
			while (tmp >= p[i])
			{
				++cnt;
				tmp /= p[i];
			}
			ans += cnt - 1;
		}
	

		cout << "Case #" << test << ": " << ans << endl;
		//cerr << "Case #" << test << " finished!" << endl;
	}
	return 0;
}