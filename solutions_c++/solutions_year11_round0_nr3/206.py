#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	
	
	int T;	cin >> T;
	for(int cas=1; cas<=T; cas++)
	{
		int N;	cin >> N;
		int MIN = 1 << 29;
		int sum = 0, Xor = 0;
		while(N --)
		{
			int x;	
			cin >> x;
			sum += x;
			Xor ^= x;
			MIN = min(MIN, x);	
		}
		printf("Case #%d: ", cas);
		if(Xor)	puts("NO");
		else	printf("%d\n", sum - MIN);
	}
	
	
	return 0;	
}
