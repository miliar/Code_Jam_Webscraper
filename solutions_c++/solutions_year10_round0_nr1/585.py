#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;

#define fore(i,n) for(int i = 0; i < (n); i++)
#define fort(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

#define err(...) fprintf(stderr, __VA_ARGS__)

void test()
{
	int n,k;
	scanf("%d%d", &n, &k);
	k &= (1 << n) - 1;
	printf("%s\n", k == (1<<n) - 1 ? "ON" : "OFF");
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		test();
	}
}
