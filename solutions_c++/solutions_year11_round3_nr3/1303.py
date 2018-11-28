#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
int t;
int n,l,h;
bool gane;
bool anda(int a,int n){
    if(a%n==0) return 1;
    if(n%a==0) return 1;
    return 0;}
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    cin>>t;
    for (int z=1;z<=t;z++){
        gane=0;
        cin>>n>>l>>h;
        int pepe[n];
        for (int i=0;i<n;i++) cin>>pepe[i];
        for (int i=l;i<=h;i++){
            int fail=0;
            for (int j=0;j<n;j++){
                if (anda(i,pepe[j])==0)fail=1;}
            if (fail==0){
                cout<<"Case #"<<z<<": "<<i<<endl;
                gane=1;
                break;}}
        if (gane==0){
            cout<<"Case #"<<z<<": NO"<<endl;}}}
