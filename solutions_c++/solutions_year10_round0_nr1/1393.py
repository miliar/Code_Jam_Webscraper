#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;



long long n,k;
int t;


//

//freopen ("myfile.txt","w",stdout);

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&t);
    
    for(int gl=1;gl<=t;gl++)
    {
        
        scanf("%d%d",&n,&k);
        long long a;
        a= pow(2.0,(double) n);
        k= k%a;
        
        cout<<"Case #"<<gl<<": ";
        
        if(k==0) cout<<"OFF\n";
        else
        {
            a=a-1;
            if(k==a) cout<<"ON\n";
            else cout<<"OFF\n";
        }
        
        //cout<< a;
        //cin>>t;
    
    }
    return 0;
}
    
