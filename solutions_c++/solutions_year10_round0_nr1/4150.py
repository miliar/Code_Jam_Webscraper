#include<iostream>
#include<cstdio>

using namespace std;



int main(){
    freopen("ain.in","r", stdin);
freopen("aout.out", "w", stdout);
    int t;
    cin>>t;
    long long n, k;
    for(int a=1;a<=t;a++){
            cin>>n>>k;
            cout<<"Case #"<<a<<": ";
            long long b=1<<n;
            if((k+(long long)(1)) % b ==0)cout<<"ON\n";
            else cout<<"OFF\n";
            }
    return 0;
}
