/*
TASK: Safety in Numbers
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
using namespace std;
#define X first
#define Y second
int N,M,T;
int a[220];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxx1.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int ii=0;
    while(T--)
    {
        ii++;
        printf("Case #%d:",ii);
        scanf("%d",&N);
        M=0;
        for(i=1;i<=N;i++)
        {
            scanf("%d",&a[i]);
            M+=a[i];
        }
        double x=M,y,z;
        x=x*2/N;
        // 
        double xx=x;
        k=N;
        int tm=M;
        for(i=1;i<=N;i++)
        {
            if(a[i]>x)
            {
                k--;
                M-=a[i];
            }
        }
        x=M+tm; x=x/k;
//        printf("%d %d %lf\n",M,tm,x);
        for(i=1;i<=N;i++)
        {
            y=x-a[i];
            z=y*100/tm;
            if(a[i]>xx) printf(" 0.000000");
            else
                printf(" %lf",z);
        }
        printf("\n");
    }
}
