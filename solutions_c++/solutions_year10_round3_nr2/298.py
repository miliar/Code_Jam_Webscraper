#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

long long a[1000],b[1000];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long t,col,l,p,c,kol;
    scanf("%I64d",&t);
    for (int j = 0; j < t; j++) {
       col=0;kol=0;
       scanf("%I64d%I64d%I64d",&l,&p,&c);
       while (l<p) {l*=c;kol+=1;}
       l=1;
       while (l<kol) {l*=2;col+=1;}
     printf("Case #%d: %I64d\n",j+1,col);
    }

    return 0;
}
