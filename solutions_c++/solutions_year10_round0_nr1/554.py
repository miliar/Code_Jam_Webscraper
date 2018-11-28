#include <cstdio>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int i=0; i<t; i++)
	{
		long n, k, p;
		scanf("%ld%ld", &n, &k);
		p=1<<n;
		printf("Case #%d: %s\n", i+1, (k%p+1 == p)?"ON":"OFF");
	}
	return 0;
}