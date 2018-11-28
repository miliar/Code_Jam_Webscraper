/* 
 * File:   main.cpp
 * Author: CONQUERER
 *
 * Created on May 9, 2010, 12:31 AM
 */

#include <stdlib.h>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <math.h>

/*
 * 
 */
int main(int argc, char** argv) {
    freopen ("C-small-attempt0.in", "r", stdin);
    freopen ("C-small-attempt0.out", "w", stdout);
    long long int T,R,k,N,x,sum,y,l,tsum=0,cn=0;
    long long int* g=NULL;
    long long int* temp=NULL;
    scanf("%llu",&T);
    while(T--)
    {
       scanf("%llu",&R);
       scanf("%llu",&k);
       scanf("%llu",&N);
       g=new long long int[N];
       temp=new long long int[N];
       for(x=0;x<N;x=x+1)
       {
           scanf("%llu",&g[x]);
       }
       while(R>=1)
      {
           x=0;
           sum=0;
           l=0;
          while(sum<=k)
          {
              if((sum+g[x])<=k)
                  sum=sum+g[x];
              else
                  break;
              x++;
          }
           for(y=x;y<N;y=y+1)
           {
             temp[l]=g[y];
             //printf("%llu",g[l]);
             l++;
           }
           for(y=0;y<x;y=y+1)
           {
               temp[l]=g[y];
               //printf("%llu",g[l]);
               l++;
           }
           for(y=0;y<N;y=y+1)
           {
           g[y]=temp[y];    
           }

           tsum=tsum+sum;
           R--;

      }
       printf("Case #%llu: %llu\n",cn+1,tsum);
       tsum=0;
       cn=cn+1;

    }

    return (EXIT_SUCCESS);
}

