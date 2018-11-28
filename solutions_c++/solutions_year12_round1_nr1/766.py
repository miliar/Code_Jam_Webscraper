#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <list>

using namespace std;

/*
bool isPrime[];

void prime(int n)
{
    int i,j,end;

    memset(isPrime,true,sizeof(isPrime));

    end = sqrt(n) +1;
    for (i=2; i<end; i++)
        if (isPrime[i]) {
            for(j=i*2; j<1001; j+=i)
                isPrime[j] = false;
        }
}
*/

#define for0(i,n)  for ((i)=0; (i)<(n); (i++))
#define for1(i,n)  for ((i)=1; (i)<=(n); (i++))
#define foriter(i,v)  for ((i)=(v).begin(); (i)!=(v).end(); (i)++)



int main()
{
    int i,j,k,T,tt;
    int a,b;
    double ans, succ;
    double p[100000];

    scanf("%d", &T);

    for0(tt,T) {
        scanf("%d %d", &a,&b);
      //  printf("%d %d\n",a,b);
        double c;

        for0(i,a)
            scanf("%lf", p+i);

        //p[0] = 0.5;
        /*
        for0(i,a)
            printf("%lf ", p[i]);
        printf("\n");
*/
        ans = 500000;
        succ = 1;
        j=0;
        int rest = b-a+1;
        for (i=a; i>=0; i--) {
            ans = min(succ * (2*i+rest) + (1-succ)* (2*i+rest+b+1), ans);
            if (i!=0)
                succ *= p[j++];
        }

        ans = min((double)1+b+1, ans);


        printf("Case #%d: %.8lf\n", tt+1, ans);
    }
}
