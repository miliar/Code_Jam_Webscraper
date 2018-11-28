#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;

int Googlers;
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int i,j,k,len,N,P,S,t=1,mx;
    scanf("%d",&k);
    while(k--)
    {
        scanf("%d %d %d",&N,&S,&P);
        mx=0;
        for(i=0;i<N;i++)
        {
            scanf("%d",&Googlers);
            if(Googlers>=P)
            {
                Googlers-=P;
                if(Googlers>=(2*P)) mx++;
                else
                {
                      len=Googlers/2;
                      j=Googlers-len;
                      if(abs(len - P)<=1 && abs(j-P)<=1) mx++;
                      else
                      {
                            if( (abs(len - P)==2 && abs(j-P)<=2)&&S>0)
                            {mx++;S--;}
                          else if((abs(j - P)==2 && abs(len-P)<=2)&&S>0)
                            {mx++;S--;}
                      }
                }
            }
        }
        printf("Case #%d: %d\n",t++,mx);
    }
    return 0;
}
