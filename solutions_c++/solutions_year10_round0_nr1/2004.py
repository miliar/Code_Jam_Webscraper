#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;


int main()
{
    FILE *in=fopen("snap.in","r");
    freopen("snap.out","w",stdout);
    int c,c2;
    int tests;
    fscanf(in,"%d",&tests);
    int testn=1;
    while (tests)
    {
        printf("Case #%d: ",testn);
        tests--;
        int n,k;
        fscanf(in,"%d%d",&n,&k);
        k%=(1<<n);
        if (k+1==(1<<n))printf("ON\n");
        else printf("OFF\n");
        testn++;
    }
//    system("pause");
    return 0;
}
