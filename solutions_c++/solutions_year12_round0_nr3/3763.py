#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;
int npairs;
FILE* out;

int numDigits( int n )
{
    char a[5];
    sprintf(a, "%d", n);
    return strlen(a);
}

int ror( int n, int digs )
{
    int power=1, digit;
    for (int i=0; i<digs-1; i++)
        power *= 10;
    digit = n % 10;
    n /= 10;
    n += (digit*power);
    return n;
}

bool matchedPair( int n, int m )
{
    if (n < m && numDigits(n) == numDigits(m))
       return true;
    return false;
}

void check( int n, int digs, int b )
{
    int i, j, rotn, *rots;
    rots = (int*)malloc( sizeof(int) * digs );
    rots[0] = n;
    rotn = n;
    for (i=1; i<digs; i++)
    {
        rotn = ror(rotn, digs);
        rots[i] = rotn;
    }
    
    for (i=0; i<digs; i++)
    {
        for (j=0; j<i; j++)
        {
            if (rots[i] == rots[j])
               rots[i] = 0;
        }
    }
    
    for (i=1; i<digs; i++)
    {
        rotn = rots[i];
        if (rotn > n && rotn <= b && matchedPair(n, rotn))
            npairs++;
    }
    free(rots);
}

int main()
{
    int cases, tctr, i, j;
    int a, b, n, m, digits;
    FILE* in = fopen("C-large.in", "r");
    out = fopen("output.txt", "w");
    
    fscanf(in, "%d\n", &cases);
    
    for (tctr=0; tctr<cases; tctr++)
    {
        npairs=0;
        fscanf(in, "%d %d\n", &a, &b);
        digits = numDigits(a);
        if (digits == 1)
        {
           fprintf(out, "Case #%d: %d\n", tctr+1, npairs);
           continue;
        }
        for (n=a; n<=b; n++)
            check(n, digits, b);
        fprintf(out, "Case #%d: %d\n", tctr+1, npairs);
    }
    
    fclose(in);
    fclose(out);
    return 0;   
}
