#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(){
    int ncasos,n,k;
    cin>>ncasos;
    for(int i=1;i<=ncasos;i++){
        cin>>n>>k;
        long long base=pow((double)2,(double)n)-1;
        if((base)==(base&k))
        cout<<"Case #"<<i<<": ON"<<endl;
        else
        cout<<"Case #"<<i<<": OFF"<<endl;
    }
}
/*
4
1 0
1 1
4 0
4 47
*/
