#include<iostream>
#include<cmath>
using namespace std;

int main()
{
     freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
     int T;
    scanf("%d",&T);
    for(int id=1;id<=T;id++)
    {
            long long N,K;
            printf("Case #%d: ",id);
            scanf("%d %d",&N,&K);
            long long period=(1LL<<N);
            if((K+1)%period==0)
            printf("ON");
            else              
            printf("OFF");
            putchar(10);
    }
    

}
