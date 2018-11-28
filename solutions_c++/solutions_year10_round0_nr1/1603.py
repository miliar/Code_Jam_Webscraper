#include <cstdio>
using namespace std;
typedef long long INT;
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for(int it=0;it<t;it++)
	{
		INT n, k;
		scanf("%lld%lld", &n, &k);
		INT step = 1ll<<n;
		INT fst = step-1;		
		bool on = ( (k-fst)%step==0 );
		printf("Case #%d: %s\n", it+1, on?"ON":"OFF");
	}
	fclose(stdout);
	return 0;
}
