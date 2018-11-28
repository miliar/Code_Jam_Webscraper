#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for( int C = 1; C <= T; ++C )
	{
		int n, k;
		scanf("%d %d", &n, &k);
		
		int msk = ((1<<n)-1);
		bool on = ((k & msk) == msk);
		printf("Case #%d: %s\n", C, (on ? "ON" : "OFF"));
	}
	return 0;
}