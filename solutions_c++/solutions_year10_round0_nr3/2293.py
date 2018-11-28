using namespace std;
#include<iostream>
#include<cstdio>
#include<vector>
int main()
{   long long x,y,z,H,T,R,S,k,N,euro;
    scanf("%lld",&T);
    for(x=0;x<T;x++)
    {
        scanf("%lld %lld %lld",&R,&k,&N);
        vector <int> G(N);
        S=0;
        for(y=0;y<N;y++)
        {  scanf("%lld",&G[y]); S+=G[y]; }
        euro=0;
        for(y=0,z=0;y<R;y++)
        { H=0;
          while(((H+G[z])<=k) && (H+G[z])<=S)
          { H+=G[z]; z++;
            if(z==N) z=0;  }
          //cout<<H<<" ";
          euro+=H;
        }    
        //cout<<endl;
        printf("Case #%lld: %lld\n",x+1,euro);
    }    
    return 0;
}    
