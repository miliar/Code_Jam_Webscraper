#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>

using namespace std;

int n,i,j,r,c,test,dd,t,l;
int d[51][51];
string s[51];
int a[105];

int main(){
    freopen("c://input.txt","r",stdin);
    freopen("c://output.txt","w",stdout);
    cin>>t;
    for(test=1;test<=t;test++){
       
       cout<<"Case #"<<test<<": ";
       cin>>n>>l>>r;
       for (i=0;i<n;i++)
           cin>>a[i];
       for (i=l;i<=r;i++){
           dd=1;
           for (j=0;j<n;j++)
               if ((i%a[j])!=0 && (a[j]%i)!=0){
                  dd=0;
                  break;                 
               }    
           if (dd) {cout<<i<<endl;break;}
       }
       if (dd==0){
          cout<<"NO"<<endl;           
       }
    }
    return 0;    
}
