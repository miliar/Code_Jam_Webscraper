#include <cstdio>
#include <cmath>
#include <algorithm> 

using namespace std;

long long nsd(long long a, long long b)
{
	if(b == (long long)0)
		return a;
	return nsd(b, a%b);
}

int main()
{
	int T, n;
	long long numbers[10010], l, h;
	freopen("2in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for(int t = 0; t < T; t++)
	{
		long long answer = (long long)-1;
		bool validNsk = true;
		scanf("%d%lld%lld", &n, &l, &h);
		for(int i =0 ; i < n; i++)
			scanf("%lld", numbers + i);
		for(long long i = l; i <= h; i++)
		{
			int j;
			for(j = 0; j < n; j++)
				if(!((i % numbers[j] == 0) || (numbers[j] % i == 0)))
					break;
			if(j >= n)
			{
				answer = i;
				break;
			}
		}
		if(answer == (long long)-1)
			printf("Case #%d: NO\n", t+1);
		else
			printf("Case #%d: %lld\n", t+1, answer);
	}
	return 0;
}

/*

		sort(numbers, numbers+n);
		long long curnsd = numbers[0];
		long long curnsk = numbers[0];
		for(int i = 1; i < n; i++)
		{
			if(curnsk >= l && curnsk <= h && validNsk)
			{
				int j;
				for(j = i; j < n; j++)
					if(numbers[j] % curnsk != 0)
						break;
				if(j >= n)
				{
					if(curnsk < answer || answer == (long long)-1)
						answer = curnsk;
				}
			}
			curnsd = nsd(curnsd, numbers[i]);
			if(validNsk)
			{
				curnsk = curnsk * numbers[i] / nsd(curnsk, numbers[i]);
				if(curnsk > h)
					validNsk = false;
				//double dcurnsk = (double)curnsk * (double)numbers[i] / (double)nsd(curnsk, numbers[i]);
				//if(dcurnsk > 10000000000001000.0)
				//	validNsk = false;
				//else
				//	curnsk = (long long)(dcurnsk + 0.5);
			}
		}
		if(curnsk >= l && curnsk <= h && (curnsk < answer || answer == (long long)-1))
			answer = curnsk;
		if(curnsd >= l && curnsd <= h)
			answer = curnsd;
*/