#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double ldouble;
using namespace std;
int main(){
    int test;
    cin>>test;
    for(int z=1;z<=test;z++){
            int64 n,k;
            cin>>n>>k;
            int64 val=(int64)pow(2,(double)n);
            int64 rem=k%val;
            if(rem==(val-1))
                     cout<<"Case #"<<z<<": ON\n";
            else
                     cout<<"Case #"<<z<<": OFF\n";
    }
    return 0;
}
