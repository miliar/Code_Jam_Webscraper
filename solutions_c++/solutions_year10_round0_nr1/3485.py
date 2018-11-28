#include <cstdio> 
using namespace std;

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("data.out", "w", stdout);

	int T, n, k;
	scanf("%d", &T);
	
	for (int x=1; x<=T; x++)
	{
		scanf("%d %d", &n, &k);
		if ((k+1)%(1<<n) == 0) printf("Case #%d: ON\n", x);
		else printf("Case #%d: OFF\n", x);
	}
}