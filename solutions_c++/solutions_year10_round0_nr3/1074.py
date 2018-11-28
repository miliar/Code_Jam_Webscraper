// Google Code Jam Qualification Round 2010
// Problem C: Theme Park
// soimort

#include <cstdio>

using namespace std;

int main()
{
    FILE *in, *out;
    in = fopen("C.in", "r");
    out = fopen("C.out", "w");
    
    int t, n;
    long r, k, g[1000];
    
    fscanf(in, "%d", &t);
    
    for(int i=1; i<=t; i++)
    {
        long g_sum=0, s=0;
        
        fscanf(in, "%ld%ld%d", &r, &k, &n);
        for(int j=0; j<n; j++)
        {
            fscanf(in, "%ld", &g[j]);
            g_sum+=g[j];
        }
        
        long rr=0, m=0, tmp, p=0;
        while(rr<r)
        {
            m=0;
            tmp=p;
            do
            {
                m+=g[p%n];
                p++;
            }while(m+g[p%n]<=k && p%n!=tmp%n);
            rr++;
        }
        s=(p/n)*g_sum;
        for(int j=0; j<p%n; j++)
            s+=g[j];
        
        fprintf(out, "Case #%d: %ld\n", i, s);
    }
    
    fclose(in);
    fclose(out);
    return 0;
}
