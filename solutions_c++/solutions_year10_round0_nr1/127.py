#include<iostream>
using namespace std;
int T,N,K;
int Solve(int rank)
{
    printf("Case #%d: ",rank);
    scanf("%d %d",&N,&K);
    bool Ans=true;
    for (int i=0;i<N;++i)
    {
        if (K % 2 == 0) Ans=false;
        K/=2;
    }
    if (Ans) printf("ON\n"); else
             printf("OFF\n");
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int i=0;i<T;++i) Solve(i+1);    
    return 0;
}
