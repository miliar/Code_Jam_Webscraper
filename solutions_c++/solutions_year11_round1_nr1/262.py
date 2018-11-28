#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("outa_l.txt", "w", stdout);
    int T;
    cin>>T;
    
    for(int t = 1; T--; ++t)
    {
        int PD, PG;
        long long N;
        cin>>N>>PD>>PG;
        
        if(PG == 100)
        {
            if(PD != 100)
                cout<<"Case #"<<t<<": Broken"<<endl;
            else
                cout<<"Case #"<<t<<": Possible"<<endl;
            continue;
        }
        if(PG == 0)
        {
            if(PD != 0)
                cout<<"Case #"<<t<<": Broken"<<endl;
            else
                cout<<"Case #"<<t<<": Possible"<<endl;
            continue;
        }

            
        int i;
        for(i = 1; i <= 100; i++)
           if(100%i == 0)
              if( PD%(100/i) == 0 && (100-PD)%(100/i)==0 )
              {
                   break;
              }
        
        if(N < (long long)i)
            cout<<"Case #"<<t<<": Broken"<<endl;
        else
            cout<<"Case #"<<t<<": Possible"<<endl;
    }
    return 0;
}
