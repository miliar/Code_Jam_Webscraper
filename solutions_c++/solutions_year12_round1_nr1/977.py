#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <string>
#include <iostream>
using namespace std;
#define oo 1000000000
int A,B;
double P[1200000];
double prob_right[1200000];


int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d%d",&A,&B);
        for(int i=1;i<=A;i++)
        {
            scanf("%lf",&P[i]);
        }
        prob_right[0]=1;
        for(int i=1;i<=A;i++)
            prob_right[i]=prob_right[i-1]*P[i];
        double answer=2+B;
        for(int i=0;i<=A;i++)
        {
            answer=min(answer, prob_right[i]*(A-i+B-i+1)+(1-prob_right[i])*(A-i+B-i+B+2));
        }
        printf("Case #%d: %1.10f\n",t,answer);
        
    }
        
}