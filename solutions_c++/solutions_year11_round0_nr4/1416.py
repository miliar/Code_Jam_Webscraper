#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

//encore un fake, comme le C

int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        int n;
        fscanf(input, "%d", &n);
        int t[n];
        for(int i = 0; i < n; i++) fscanf(input, "%d", &t[i]);
        bool libre[n];
        for(int i = 0; i < n; i++) libre[i] = true;
        double res = 0.;
        for(int i = 0; i < n; i++)
            if(libre[i])
            {
                libre[i] = false;
                int cycle = 1;
                int ni = t[i] - 1;
                while(ni != i)
                    { cycle++; libre[ni] = false; ni = t[ni] - 1; }
                if(cycle > 1) res += (double) cycle;
            }
        fprintf(output,"Case #%d: %.6f\n", cas, res);
    }
	return 0;
}
