#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#define MAX(X,Y) ((X)>(Y)?(X):(Y))
#define MIN(X,Y) ((X)<(Y)?(X):(Y))
#define ABS(X)  ((X)>0?(X):(-(X)))
#define SWAP(TYPE,X,Y) {TYPE T=X; X=Y; Y=T;}
int nCase;
using namespace std;
#define SMALL
int main()
{
    #ifdef SMALL
    	freopen("C-small-attempt0.in","rt",stdin);
        freopen("C-small.out","wt",stdout);
    #endif
    
    scanf("%d",&nCase);
    for(int iCase=1; iCase<=nCase; iCase++)
    {
        int a, b, dg=0, ct=0, pow=1;
        printf("Case #%d: ",iCase);
        scanf("%d%d",&a,&b);
        dg = ( (int)log10(a) )+1;
        for(int i=1; i<dg; i++)  pow *= 10;
        for(int n=a; n<=b; n++)
        {
            int m = n;
            for(int i=1; i<=dg; i++)
            {
                m = m/10 + m%10*pow;
                if( a<=n && n<m && m<=b )
                    ct++;
            }
        }
        printf("%d\n",ct);
    }
    scanf(" ");
    return 0;
}
