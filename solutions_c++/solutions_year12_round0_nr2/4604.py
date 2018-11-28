#include<iostream>
#include<fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main()
{
    
    freopen ("B-large.in","r",stdin);
    freopen ("B-large-output.out","w",stdout);
    
    
    int k;
    int t=0;
    
    cin>>k;
    while(t<k)
    {
            int N;
            int S;
            int P;
              
            cin>>N;
            cin>>S;
            cin>>P;
            
            int g;
            int s=0;
            int p=0;
            for(int j=0;j<N;j++)
            {
                     cin>>g;
                     if(g<P)
                               continue;
                     if(g>=(P*3)-2)
                     {
                                      p++;
                                      continue;
                     }
                     if(P-((g-P)/2)==2)
                     {
                                 s++;
                     }
            
            }
            
            cout<<"Case #"<<t+1<<": "<<p+(s<S?s:S);
            
               
            cout<<endl;             
            t++;
    }
    
}
