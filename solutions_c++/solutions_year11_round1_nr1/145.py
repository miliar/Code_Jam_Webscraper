#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
const int MaxN = 110;

LL gcd(LL a, LL b)
{
	return b ? gcd(b, a%b) : a;	
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	
	int T;	cin >> T;
	
	for(int cas=1; cas<=T; cas++)
	{
		printf("Case #%d: ", cas);
		
		LL N, x, y;
		cin >> N >> x >> y;
		
		if((x < 100 && y == 100) || (x > 0 && y == 0))
		{
			puts("Broken");
			continue;	
		}
		
		x = 100 / gcd(x, 100);
		puts(x <= N ? "Possible" : "Broken");
	}
	
	
	return 0;	
}
