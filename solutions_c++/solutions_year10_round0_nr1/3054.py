#include<iostream>
using namespace std;

int main(){
    int t,n,k;
    cin>>t;
    for(int tn=1;tn<=t;tn++){
               cin>>n>>k;
               bool fl=false;
               for(int i=1, j=0;j<n;j++, i=i<<1){
                   if((k&i)!=i){
                       fl=true;
                       break;
                   }    
               }
               if(fl)
                 cout<<"Case #"<<tn<<": OFF"<<endl;
               else
                 cout<<"Case #"<<tn<<": ON"<<endl;
    }
    //system("PAUSE");
    return 0;
}
