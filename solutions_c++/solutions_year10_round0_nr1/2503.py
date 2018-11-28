#include<iostream>
using namespace std;
int main(){
        long long t,a,n,k,c=1;
        freopen("A-large.in","rt",stdin);
        freopen("a.txt","wt",stdout);
        cin>>t;
        while(t--){
             a=1;
             cin>>n>>k;
             a<<=n;
             if((k%a)==(a-1))
               cout<<"Case #"<<c++<<": ON"<<endl;
               else
                  cout<<"Case #"<<c++<<": OFF"<<endl;            
        }
} 
