#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int c = 1; c <= cases; ++c){
		int n, k;
		scanf("%d%d", &n, &k);
		int l = 1<<n;
		printf("Case #%d: ", c);
		printf( ((k%l) == l-1) ? "ON\n" : "OFF\n");
	}
	return 0;
}
