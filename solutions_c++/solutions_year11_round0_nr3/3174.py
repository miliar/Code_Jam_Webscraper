#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int a[100];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,T,t,s1,s2,s,maxi,n;
    cin>>T;
    bool flag;
    for (t=1; t<=T;t++)
    {
        cin>>n;
        flag=true;
        for (i=0; i<n;i++)
         cin>>a[i];
         maxi=-1;
        for (i=1;i<(1<<n)-1;i++)
        {
            s=s1=s2=0;
         for (j=0; j<n;j++)
          if (i&(1<<j)) { s1^=a[j]; s+=a[j];}
           else s2^=a[j];
         if (s1==s2)
         {
             flag=false;
             maxi=max(s,maxi);

         }
        }
       if (flag)
        cout<<"Case #"<<t<<": "<<"NO"<<endl;
       else
        cout<<"Case #"<<t<<": "<<maxi<<endl;
    }

    return 0;
}
