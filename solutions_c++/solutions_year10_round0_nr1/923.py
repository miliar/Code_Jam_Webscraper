#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

int num,tot,N,K;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tot);
    while (tot--)
      {
        ++num;
        scanf("%d%d",&N,&K);
        K%=(1<<N);
        if (K+1==(1<<N))   printf("Case #%d: ON\n",num);
        else   printf("Case #%d: OFF\n",num);
      }
}
