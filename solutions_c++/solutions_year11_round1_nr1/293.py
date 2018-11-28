#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int pgcd(int a, int b) //32bit !!
{
    if(a > b) return pgcd(b,a);
    if(a == 0) return b;
    return pgcd(a, b % a);
}

int main()
{
    FILE * input = fopen("input.txt", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        long long n;
        int pd, pg;
        fscanf(input, "%lld%d%d", &n, &pd, &pg);
        //attention aux cas limites, 0 tout ça
        if(((pg != 0 && pg != 100) || (pg == 0 && pd == 0) || (pg == 100 && pd == 100)) && ((100 / pgcd(pd, 100)) <= n))
            fprintf(output,"Case #%d: Possible\n", cas);
        else
            fprintf(output, "Case #%d: Broken\n", cas);
    }
	return 0;
}
