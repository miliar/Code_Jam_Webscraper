#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;


int main()
{
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++)
    {
	int n, s, p;
	scanf("%d%d%d", &n, &s, &p);
	int result = 0;
	for(int i = 0; i < n; i++)
	{
	    int tot;
	    scanf("%d", &tot);
	    if (tot >= 2*max(p-1,0) + p) //not surprising win
		result++;
	    else if (tot >= 2*max(p-2,0) + p && s > 0) //surprising win
	    { result++; s--; }
	}
	printf("Case #%d: %d\n", cas, result);
    }
    return 0;
}
