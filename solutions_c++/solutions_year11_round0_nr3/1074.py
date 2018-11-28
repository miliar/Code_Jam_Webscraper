#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#define TASK "C-large"
#define Max 1000
using namespace std;

int T,N,Piles[Max],Sum,Xor;

int main()
{
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    
    cin>>T;
    
    for(int i=0; i<T; i++)
    {
        Sum=Xor=0;
        
        cin>>N;
        for(int j=0; j<N; j++)
        {
            cin>>Piles[j];
            Sum+=Piles[j];
            Xor^=Piles[j];
        }
        
        sort(Piles, Piles+N);
        
        cout<<"Case #"<<i+1<<": ";
        
        if(Xor==0)
        {
            cout<<Sum-Piles[0]<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
