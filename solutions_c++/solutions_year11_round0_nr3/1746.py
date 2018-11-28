#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
        freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
   int t;
   cin>>t;
   for(int test_case=0;test_case<t;test_case++)
   {
       int n;
       cin>>n;
       int a=0,x=0;
       int b[1000];
       for(int i=0;i<n;i++)
       {
           cin>>b[i];
       }
       sort(b,b+n);
       for(int i=1;i<n;i++)
       {
           a^=b[i];
           x+=b[i];
       }
       cout<<"Case #"<<test_case+1<<": ";
       if(a!=b[0])
         cout<<"NO"<<endl;
       else
        cout<<x<<endl;
   }
}
