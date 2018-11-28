#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T,totalcase;
    cin>>T;
    totalcase = T;
    
    while(T)
    {
            int N,t;
            cin>>N;
            
            int patxor,seanxor,seansum;
            patxor=0;
            seanxor=0;
            seansum =0;
            
            vector<int> c;
            for(int i =0;i<N;i++)
            {
                    cin>>t;
                    c.push_back(t);
                    
                    seanxor = seanxor^t;
                    seansum = seansum + t;
            }
            
            if(seanxor !=0)
            {
                       cout<<"Case #"<<(totalcase+1-T)<<": NO"<<endl;
            }
            else
            {
                sort(c.begin(),c.end());
                for(int i =0; i < c.size();i++)
                {
                        seanxor=seanxor^c[i];
                        patxor=patxor^c[i];
                        seansum = seansum - c[i];
                        
                        if(patxor==seanxor)
                                           break;
                }
                
                cout<<"Case #"<<(totalcase+1-T)<<": "<<seansum<<endl;
                
                
            }
            
            T--;
    }
}
