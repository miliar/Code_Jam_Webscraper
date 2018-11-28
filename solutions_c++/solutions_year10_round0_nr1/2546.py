#include<iostream>
#include<cmath>
using namespace std;


int main()
{
      freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);
     long long i,j,t,N,K,cas=1;
     cin>>t;
    while(t--)
    {
       cin>>N>>K;
       j=(1<<N)-1;
       i=K%(1<<N);
       if(j==i)
        printf("Case #%d: ON\n",cas++);
       else
        printf("Case #%d: OFF\n",cas++);
    }

    return 0;
}
