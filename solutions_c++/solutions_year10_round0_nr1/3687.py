#include<iostream>
using namespace std;

int main() {
    int p,l=1;
    cin >> p;
    while(p--) {
    int n,k;
    cin >> n >> k;
    long long a = (long long)(1<<n)-1;
    long long b = a+1;
    cout<<"Case #"<<l++<<": ";
    if(a==k) {cout<<"ON\n";continue;}
    else {
         if((k-a)%b==0 ) cout<<"ON\n";
         else cout<<"OFF\n";      
         }
    }




}
