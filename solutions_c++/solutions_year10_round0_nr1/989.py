#include<iostream>
using namespace std;
long long power(int a,int b){long long p;
    if(b==0)return 1;
    else if(b==1)return a;
    if(b%2==0){p=power(a,b/2);return p*p;}
    p=power(a,b/2);return a*p*p;
    
    }
int main(){
    long n,k,i=0,t;
    long long p;
    cin>>t;
    while(i<t){i++;
    cin>>n>>k;
    p=power(2,n);
    if((k%p)==p-1)cout<<"Case #"<<i<<": ON\n";
    else cout<<"Case #"<<i<<": OFF\n";
    }
    return 0;
    }
