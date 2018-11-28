//This program is made by Rakshit Jain
#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    unsigned long int t;
    cin>>t;
    unsigned long int c=0;
    while( t-- )
    {
           for( int i=0; i<c; i++ )
           {
                i++;
           }
           c++;
           unsigned long int n,k;
           cin>>n>>k;
           k++;
           n=pow(2,n);
           if ( k%n==0 )
           {
                cout<<"Case #"<<c<<": ON";
           }
           else 
           {
                cout<<"Case #"<<c<<": OFF";
           }
           cout<<endl;
    }
    return 0;
}
