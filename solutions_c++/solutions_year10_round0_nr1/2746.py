#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int t,n,i ;
    long int bin,k ;
    cin>>t ;
    for(i=0;i<t;i++)
    {
        cin>>n>>k;
        bin = int(pow(2,n)) ;
        k+=1 ;
        if(k%bin==0)
        {
            cout<<"Case #"<<i+1<<": ON"<<endl ;
        }
        else
        {
            cout<<"Case #"<<i+1<<": OFF"<<endl ;
        }
    }
    return 0 ;
}
