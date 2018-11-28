#include<stdio.h>
#include<stdlib.h>
#include<cmath>
#include<set>
#include<cstring>
#include<queue>
#include<list>
#include<algorithm>
#include<iostream>
#define PINF 999999999
#define NINF -999999999
using namespace std;
int n,m,A,B,T,mc;
int a[10],used[2000001];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    a[0]=1;
    a[1]=10;
    a[2]=100;
    a[3]=1000;
    a[4]=10000;
    a[5]=100000;
    a[6]=1000000;
    a[7]=10000000;
    scanf("%d",&T);
    int cnt;
    for(int c=1;c<=T;c++)
    {
        cnt=0;
        scanf("%d %d",&A,&B);
        for(int i=A;i<=B;i++)
            used[i]=0;
        for(int i=0;;i++)
        {
            if(A/a[i]==0)
            {
                mc=i;
                break;
            }
        }
        for(int i=A;i<=B;i++)
        {
            for(int j=i+1;j<=B;j++)
            {   
                for(int k=0;k<mc;k++)
                { 
                    if(j/a[k]==i%(a[mc-k]) && j%a[k]==i/(a[mc-k]))
                    {
                        //printf("-%d %d-\n",i,j);
                        //printf("%d %d\n",j/a[k],i%(a[mc-k]));
                        cnt++;
                        break;
                    }
                }      
            }
        }
        printf("Case #%d: %d\n",c,cnt);
    }
    scanf(" ");
}
