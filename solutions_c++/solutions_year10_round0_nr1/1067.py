// Google Code Jam Qualification Round 2010
// Problem A: Snapper Chain
// soimort

#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
    FILE *in, *out;
    in = fopen("A.in", "r");
    out = fopen("A.out", "w");
    int t, n; long k;
    long p[31]={1};
    for(int i=1; i<=30; i++)
        p[i]=p[i-1]*2;
    bool s;
    fscanf(in, "%d", &t);
    for(int i=1; i<=t; i++)
    {
        fscanf(in, "%d%ld", &n, &k);
        s = (k + 1) % p[n] == 0;
        fprintf(out, "Case #%d: %s\n", i, s ? "ON" : "OFF");
    }
    fclose(in);
    fclose(out);
    return 0;
}
