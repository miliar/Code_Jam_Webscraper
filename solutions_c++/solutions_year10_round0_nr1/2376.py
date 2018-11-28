using namespace std;
#include<iostream>
#include<cstdio>
#include<bitset>
int main()
{   int y,T,x,N;
    long long K,P;
    scanf("%d",&T);
    for(x=0;x<T;x++)
    {
        scanf("%d %lld",&N,&K);
        for(y=0,P=1;y<N;y++) P*=2;
        K%=P;
        //cout<<K<<" "<<P<<endl;
        printf("Case #%d: ",x+1);
        if(K==P-1)
          printf("ON\n");
        else
          printf("OFF\n");
    }
    return 0;
}           
               
           
