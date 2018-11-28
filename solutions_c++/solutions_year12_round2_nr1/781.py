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

int p[210];
bool flag[210];

int main()
{
    int i,j,k,T,tt;
    int n,total, t2;


    scanf("%d", &T);

    for0(tt,T) {
        scanf("%d", &n);

        total = 0;

        for0(i,n) {
            scanf("%d", p+i);
            flag[i] = true;
            total += p[i];
        }
        t2 = total;

        double avg;
        int n2 = n;

        bool again = true;
        while (again) {
            avg = (total +t2) / (double) n2;
            again = false;
            for0(i,n) {
                if (flag[i] && p[i] > avg) {
                    again = true;
                    t2 -= p[i];
                    flag[i] = false;
                    n2--;
                }
            }
        }
        printf("Case #%d:", tt+1);

        double ans;
        for0(i,n) {
            if (avg < p[i])
                ans = 0;
            else
                ans = (avg - p[i])/ total * 100;
          /*
            if (ans < 0)
                ans = 0;
                */
            printf("% lf", ans);
        }
        printf("\n");
    }
}
