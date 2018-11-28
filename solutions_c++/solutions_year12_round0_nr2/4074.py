#include <cstdlib>
#include <string>
#include <iostream>

using namespace std; 
int main(void) {
    int i,j,t,n,s,p,sc,res,z;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n>>s>>p;
        z=(p*3)-2;
        z=(z<0?0:z);
        for(j=1,res=0;j<=n;j++)
        {
            cin>>sc;           
            if(sc>=z)
                 res++;
            else if((sc>=(z-2)) && s>0 && (z-2>0))
            { 
                res++;
                s--;
            }
        }
        cout<<"Case #"<<i<<": "<<res<<"\n"; 
   }
return 0;
}