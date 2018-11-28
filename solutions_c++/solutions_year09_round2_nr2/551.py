#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int main()
{
    FILE *f = fopen("c:\\b.in", "r") , *g = fopen("c:\\b.out", "w");
    
    int tc, a, b;
    char n[100], m[100];
    fscanf(f, "%d", &tc);
    for(int i=0;i<tc;i++)
    {
            fscanf(f, "%s", n);
            strcpy(m, n);
            next_permutation(n, n+strlen(n));
            a = atoi(n);
            b = atoi(m);
            
            if(n[0]=='0')
            {
                int j;
                for(j=0; j<strlen(n) && n[j]=='0'; j++);
                n[0] = n[j];
                n[j] = '0';
                
            }
            if(a>b)
                fprintf(g, "Case #%d: %s\n", i+1, n);
            else
                fprintf(g, "Case #%d: %c0%s\n", i+1, *n, n+1);
                
    
    }
}
