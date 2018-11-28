#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("output.txt", "wt", stdout);
	int tc; cin >> tc;
	for(int it = 0; it < tc; it++)
	{
		int n, k; cin >> n >> k;
		printf("Case #%d: %s\n", it+1, ((k & ((1 << n)-1)) == ((1 << n)-1))?("ON"):("OFF"));
	}
}
