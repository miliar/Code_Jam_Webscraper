#include<iostream>
using namespace std;
long long a[31],a1,a2;
int t,k;
void init(){
     a[0]=1;
     for(int i=1;i<31;i++)
       a[i]=a[i-1]*2+1;
}
int main(){
    init();
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--){
      cin>>a1>>a2;
      cout<<"Case #"<<++k<<": "; 
      if((a2+1)%(a[a1-1]+1)==0)
        cout<<"ON"<<endl;
      else cout<<"OFF"<<endl;
    }
    return 0;
}
