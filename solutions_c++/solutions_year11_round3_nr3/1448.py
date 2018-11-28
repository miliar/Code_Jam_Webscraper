#include <iostream>
#include <string>
#include <iomanip>
#include <algorithm>
using namespace std;

long long int num[10100];

bool test(long long int num[],long long int t,long long int n){
     for (long long int x=0; x<n;x++)
        if (!(t%num[x]==0 || num[x]%t==0))
            return false;
     return true;
}

int main(){
   long long int t,n,l,h;
   cin>>t;
   for (long long int z=0; z<t; z++){
       cin>>n>>l>>h;
       for (long long int y=0; y<n;y++)
           cin>>num[y];
       sort(num, num+n);
       bool ok=0;
       long long int target;
       for (long long int x=l; x<=h;x++){
           if (test(num, x,n)){
              target=x;
              ok=1;
               break;
           }
       }
       printf("Case #%d: ",z+1);
          if (ok)
             cout<<target<<endl;
          else
             cout<<"NO"<<endl;
       }
       }
