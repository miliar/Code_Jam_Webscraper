#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>

using namespace std;

struct tt
{
	int x, y;
};


int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int r;
	cin >> r;
	for (int y = 1; y <= r; y++)
	{
		long long a, b, p;
		cin >> a >> b >> p;
		vector<char> prime (b+1, true);
		prime[0] = prime[1] = false; 
		for (int i=2; i*i<=b; ++i)
			if (prime[i])
				for (int j=i+i; j<=b; j+=i)
					prime[j] = false;
		vector<long long> v(b+1, -1);
		int l = 0;
		for (int i = a; i <= b; i++)
		{
			v[i] = i;
		}
		bool fl = true;
		while (fl)
		{
			fl = false;
			for(int i = a; i <= b; i++)
				for(int j = i + 1; j <= b; j++) 
				{
					if(v[i] == v[j])
						continue;
					int mint = min(i , j);
					for(int	q = p; q <= mint; q++)
						if(prime[q] && i % q == 0 && j % q == 0)
						{
							for(int w = a; w <= b; w++)
								if(v[w] == v[j])								
									v[w] = v[i];
							fl = true;
							break;
						}
				}			
		}
		long long cnt = 0;
		set<int> res;
		for(int i = a; i <= b; i++)
			res.insert(v[i]);
		cnt = res.size();
		cout << "Case #" << y << ": " << cnt << endl;
	}
	return 0;
}