#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

bool is_prime(int x)
{
	if (x==2) return true;
	if (x % 2 == 0) return false;
	int t = 3;
	while (t*t <=x )
	{
		if (x % t == 0)
		{
			return false;
		}
		t+=2;
	}
	return true;
}

#define MAXN 10000

int pr[MAXN];
int cnt[MAXN];
int a[MAXN];
int min_v, max_v;

void get_min(int n)
{
	if (n==1)
	{
		min_v = max_v = 1;
		return;
	}
	int k = 0;
	for(int i=2; i<=n; ++i)
		if (is_prime(i))
		{
			pr[k] = i;
			cnt[k] = 1;
			k++;
		}
		else
		{
			int j = i;
			for(int z=0; z<k; ++z)
				if (j % pr[z] == 0)
				{
					int x = 0;
					while (j % pr[z] == 0)
					{
						x++;
						j /= pr[z];
					}
					if (x > cnt[z]) cnt[z] = x;
				}
		}
		min_v = 1;
		for(int i=0; i<k; ++i) min_v += cnt[i];		
		for(int i=0; i<k; ++i)
		{
			a[i] = 1;
			for(int j=0; j<cnt[i]; ++j) a[i] *= pr[i];			
		}
		max_v = 0;
		a[k] = n + 1;
		for(int i=0; i<k; ++i)
		{
			int v = 1;
			while (v * a[i] <= n)
			{
				v = v * a[i];
				i++;
			}
			max_v++;
			i--;
		}
		//fprintf(stderr, "min=%i max=%i\n", min_v, max_v);
}

int main()
{
    int tc, n;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
		scanf("%i", &n);
		get_min(n);
		printf("Case #%i: %i\n", tt, min_v - max_v);
    }
}