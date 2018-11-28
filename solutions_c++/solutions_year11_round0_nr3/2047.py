#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<cstring>
using namespace std;
int main()
{
    long i,j,T,N,C,sum,min,x,l;
    scanf("%ld",&T);
    for (l=0;l<T;l++)
    {
        scanf("%ld",&N);
        x=0;
        for (i=0;i<N;i++)
        {
            scanf("%ld",&C);
            if (i==0)
            {
                min=C;
                sum=C;
            }
            else
            {
                if (min>C)
                {
                    min=C;
                }
                sum+=C;
            }
            x=x^C;
        }
        if (x==0)
        {
            printf("Case #%ld: %ld\n",1+l,sum-min);
        }
        else
        {
            printf("Case #%ld: NO\n",l+1);
        }
    }
}
