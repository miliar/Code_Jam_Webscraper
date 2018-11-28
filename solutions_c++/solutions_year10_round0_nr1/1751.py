#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
	int kases;

	cin >> kases;

	for(int kase = 1; kase <= kases; ++kase)
	{
		bool res = false;
		long long N, K;
		cin >> N >> K;
		
		res = ((K>>(N-1))&1)?true:false;
		
		if(res)
		{
			long long interval = 1ll<<(N-1);

			K %= interval;

			if((K + 1) != interval) res = false;
		}

		printf("Case #%d: %s\n", kase, (res == false)?"OFF":"ON");
	}
	return 0;
}