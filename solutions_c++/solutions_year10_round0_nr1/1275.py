#include <iostream>
#include <string>
#include <cmath>
using namespace std;


int main(){
 int t;
 cin>>t;
for(int i=0;i<t;i++){
   string a;
   int n,k;
   cin>>n>>k;
   if((k&((1<<n)-1))==((1<<n)-1))
       a="ON";
   else
      a="OFF";
   cout<<"Case #"<<(i+1)<<": "<<a<<endl;
}
 return 0;
}
