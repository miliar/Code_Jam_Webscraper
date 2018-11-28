#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
    
    int nc,cont = 0,a,b,c,d,p10,ans,aux;
//    freopen("c3.in","r",stdin);
//    freopen("c.out","w",stdout);
    cin>>nc;
    while(nc--){
      cont++;
      cin>>a>>b;
      p10 = 1;
      ans = 0;
      while(p10<=a){p10*=10;}
      p10 /= 10;
      for(int i=a;i<=b;i++){
         aux = i;
         if(p10*10<=i)p10*=10;
         do{
           c = ((aux%10) * p10) + aux/10;
           //cout<<c<<" "<<i<<endl;
           if(c>a && c<=b && c>i) ans++;
           aux = c;
           }while(c != i);
         }
      cout<<"Case #"<<cont<<": "<<ans<<endl;
      }    
    }
