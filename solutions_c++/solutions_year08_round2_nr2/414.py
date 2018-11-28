#include <cstdio>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

long long A,B,P;

int primes[10000] = {0};
int countp[10000] = {0};

void resheto()
{
	primes[0] = 1;
	primes[1] = 1;
	for (int i=2; i<10000; i++)
	{
		if (primes[i] == 0)
		{
			countp[i] = countp[i-1]+1;
			for (int j=i+i; j<10000; j+=i)
				primes[j] = 1;
		}
		else
		{
			countp[i] = countp[i-1];
		}
	}
}

int mas[10000];

int bigprimes(int a, int b)
{
	int end = min(a,b);
	for (int i=end; i>=2; i--)
	{
		if (primes[i] == 0)
		{
			if (((a % i) == 0 )&&((b % i) == 0 ))
				return i;
		}
	}
	return -1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	resheto();
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		cerr<<tt<<endl;
		scanf("%lld%lld%lld", &A, &B, &P);
		for (int i=0; i<=B; i++)
		{
			mas[i] = i;
		}
		for (int p=0; p<10;p++)
		for (int i=A; i<=B; i++)
		{
			for (int j=i+1; j<=B; j++)
			{
				if (mas[i] == mas[j])
					continue;
				if (bigprimes(i,j) >= P)
				{
					int old = max(mas[j],mas[i]);
					int gnew = min(mas[i],mas[j]);
					for (int k=i; k<=B; k++)
					{
						if (mas[k] == old)
							mas[k] = gnew;
					}
				}
			}
		}
		set<int> seta;
		for (int i=A; i<=B; i++)
		{
			seta.insert(mas[i]);
		}
		long long res = seta.size();
		printf("Case #%d: %lld\n", tt, res);
	}
	return 0;
}