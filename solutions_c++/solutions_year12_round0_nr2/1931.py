#include<stdio.h>
#include<iostream>
using namespace std;
const int MAXN=110;
int t[MAXN];
int t0[MAXN];
int top;
int main()
{
  // freopen("B-large.in","r",stdin);
   // freopen("B.out","w",stdout);
    int T,N;
    int S;
    int p;
    int iCase=0;
    scanf("%d",&T);
    int res;
    while(T--)
    {
        iCase++;
        scanf("%d%d%d",&N,&S,&p);
        for(int i=0;i<N;i++) scanf("%d",&t[i]);
        top=0;
        res=0;
        int tmp=0;
        for(int i=0;i<N;i++)
        {
            if(t[i]%3==0)
            {
                if(t[i]/3+1==p&&t[i]/3-1>=0) tmp++;
                if(t[i]/3>=p)res++;
            }    
            else if(t[i]%3==1)
            {
               
                if(t[i]/3+1>=p)res++;
            }    
            else
            {
                if(t[i]/3+2==p) tmp++;
                if(t[i]/3+1>=p)res++;
            }    
        }    
        if(S>=tmp)res+=tmp;
        else res+=S;
        printf("Case #%d: %d\n",iCase,res);
    }    
    return 0;
}    
