#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)

int main()
{
     freopen("inputC.txt","r",stdin);
     freopen("outputC.txt","w",stdout);

     long int t,i,j,k,n,cn=1,r,c,l,h,arr[110];
     cin>>t;
     while(t--)
     {

           cin>>n>>l>>h;
           FOR(i,n)
           {
               cin>>arr[i];
               if(arr[i]==0)arr[i]=1;
           }
        FORab(i,l,h)
        {
            FOR(j,n)
            {
                if(arr[j]%i==0||i%arr[j]==0)continue;
                else break;
            }
            if(j==n)break;
        }
            if(i==h+1)
            cout<<"Case #"<<cn++<<": NO"<<endl;
            else cout<<"Case #"<<cn++<<": "<<i<<endl;


     }
    return 0;
}
