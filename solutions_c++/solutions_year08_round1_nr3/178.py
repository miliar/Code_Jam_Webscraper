#include <stdio.h>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

int n;

long long ex(int no,int k)
{
    if(k==0)
        return 1;
    if(k==1)
        return no;
    long long t=ex(no,k/2)%1000;
    if(k%2==1)
        return (((t*t)%1000)*no)%1000;
    else
        return (t*t)%1000;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int N;
    scanf("%d",&N);
    for(int I=0;I<N;I++)
    {
        scanf("%d",&n);
        long long a=1;
        long long b=3;
        long long c=3;
        for(int i=2;i<2*n;i++)
        {
            c=(a+b)%1000;
            a=b;
            b=c;
        }
        c=(c*ex(2,n))%1000;
        if(c%1000>99)
            printf("Case #%d: %d\n",I+1,c%1000-1);
        else
        if(c%1000>9)
            printf("Case #%d: 0%d\n",I+1,c%1000-1);
        else
            printf("Case #%d: 00%d\n",I+1,c%1000-1);
    }
}
