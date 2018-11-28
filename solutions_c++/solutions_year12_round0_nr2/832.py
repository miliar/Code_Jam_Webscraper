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
    int n,s,p,x,ans,rem,quotient;

    scanf("%d", &T);

    for0(tt,T) {
        scanf("%d %d %d", &n,&s,&p);

        ans = 0;
        for0 (i,n) {
            scanf("%d", &x);

            if (x == 0) {
                if (p==0)
                    ans++;
            }
            else {
                quotient = x / 3;
                rem = x % 3;
                if (quotient >= p)
                    ans++;
                else if (quotient+1 == p) {
                    if (rem == 1 || rem == 2)
                        ans++;
                    else if (s>0) {//rem == 0
                        s--;
                        ans++;
                    }
                }else if (quotient+2 == p && rem == 2 && s>0) {
                    s--;
                    ans++;
                }
            }
        }



        printf("Case #%d: %d\n", tt+1, ans);
    }
}
