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

const int maxn = 2000;

int test,n;
int pow2[maxn];
int sum;
int a[maxn];
int res;

void solve(){
    int temp = 0;
    int nmin = 1000000000;
    for(int i = 0;i<n;i++){
        nmin = min(nmin,a[i]);
        temp = temp^a[i];
    }
    if (temp==0){
        res = sum - nmin;
    } else res = -1;
}

int main(){

    ifstream fin("Clarge.in");
    fin>>test;
    for(int i = 1;i<=test;i++){
        memset(a,0,sizeof(a));
        fin>>n;
        sum = 0;
        for(int j = 0;j<n;j++){
            fin>>a[j];
            sum += a[j];
        }
        solve();
        
        if (res!= -1){
            cout<<"Case #"<<i<<": "<<res<<endl;
        }else{
            cout<<"Case #"<<i<<": "<<"NO"<<endl;
        }
    }        
}
