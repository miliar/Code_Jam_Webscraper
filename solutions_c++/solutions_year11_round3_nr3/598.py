#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<sstream>

using namespace std;

const long long maxn = 2000;

long long test,res;
long long n,l,h;
long long a[maxn];
long long m;


long long gcd(long long i,long long j){
    while (true){
        long long r = i%j;
        if (r==0) return j;
        i = j;
        j = r;
    }
}

bool solve(){
    if (l<=1){
        res = 1;
        return true;
    }
    for(int i = 1;i<=sqrt(m/2)+1;i++){
        if (m%i==0 && i>=l && i<=h){
            bool flag = true;
            for(int j = 1;j<=n;j++){
                if (i%a[j]!=0 && a[j]%i!=0){
                    flag = false;
                    break;
                }
            }
            if (flag){
                res = i;
                return true;
            }
        }
    }
    res = a[1];
    for(long long i = 2;i<=n;i++){
        long long temp = gcd(res,a[i]);
        res = (res*a[i])/temp;
        if (res > h) return false;
    }
    return true;
}

bool solve2(){
    for(int i = l;i<=h;i++){
        bool flag = true;
        for(int j = 1;j<=n;j++){
            if (i%a[j]!=0 && a[j]%i!=0){
                flag = false;
                break;
            }
        }
        if (flag){
            res = i;
            return true;
        }
    }
    return false;
}

int main(){
    ifstream fin("csmall.in");
    fin>>test;
    for(long long i = 1;i<=test;i++){
        fin>>n>>l>>h;
        m = 1000000;
        for(long long j = 1;j<=n;j++){
            fin>>a[j];
            m = max(m,a[j]);
        }
        if (solve2()){
            cout<<"Case #"<<i<<": "<<res<<endl;
        } else{
            cout<<"Case #"<<i<<": "<<"NO"<<endl;
        }
    }
    fin.close();
    return 0;
}
