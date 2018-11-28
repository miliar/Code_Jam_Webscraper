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
double s[202];

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int N;
        scanf("%d",&N);
        int X=0;
        for(int i=0;i<N;i++)
        {
            scanf("%lf",&s[i]);
            X+=s[i];
        }
        printf("Case #%d: ",t);
        for(int i=0;i<N;i++)
        {
            double low=0;
            double high=1;
            for(int iters=1;iters<=1000;iters++)
            {
                double mid=(low+high)/2;
                double curr_score = s[i]+X*mid;
                double rest = (1.0-mid);
                bool canelim=true;
                for(int j=0;j<N;j++)
                    if(i!=j)
                    {
                        
                        
                        double other_frac = (curr_score+1e-9-s[j])/(double)X+1e-9;
                        other_frac=max(0.0,other_frac);
                        other_frac=min(other_frac, rest);
                        rest-=other_frac;
                        double other_score = s[j]+X*other_frac;
                        
                        
                        if(other_score<curr_score)
                            canelim=false;
                    }
                if(canelim)
                {
                    low=mid;
                }
                else
                    high=mid;
            }
            printf("%1.7f ",100*low);
        }
        printf("\n");
        
    }
}