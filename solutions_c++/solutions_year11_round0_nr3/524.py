/*
 * Author: fatboy_cw
 * Created Time:  2011/5/7 11:18:05
 * File Name: C.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())

typedef long long lint;
int test,ca,n;
vector<lint> v;
lint flag,sum;

int main() {
    freopen("C.out","w",stdout);
    std::ios::sync_with_stdio(false);
    cin>>test;
    while(test--){
        v.clear();
        cin>>n;
        flag=0;
        sum=0;
        for(int i=1;i<=n;i++){
            lint num;
            cin>>num;
            v.push_back(num);
            flag^=num;
            sum+=num;
        }
        //printf("Case #%d: ",++ca);
        cout<<"Case #"<<++ca<<": ";
        if(flag){
            cout<<"NO"<<endl;
        }
        else{
            sort(v.begin(),v.end());
            cout<<sum-v[0]<<endl;
        }
    }
    return 0;
}

