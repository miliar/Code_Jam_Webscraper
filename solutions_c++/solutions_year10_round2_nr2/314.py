#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
using namespace std;


int n, k , b, t;
int a[100], v[100];
int main(){

    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    
    int ntest;
    cin>>ntest;
    for(int test=1;test<=ntest;test++){
        cin>>n>>k>>b>>t;
        
        for(int i=0;i<n;i++) cin>>a[i];
        for(int i=0;i<n;i++) cin>>v[i];
        
        int passed = 0;
        int cswap = 0;
        int res = 0;
        
        for(int i=n-1;i>=0;i--){
            if (passed >= k) break;
            if (a[i]+t*v[i]>=b){
                res+=cswap;
                passed++;
            } else {
                cswap++;
            }
        }
        
        cout<<"Case #"<<test<<": ";
        if (passed<k) cout<<"IMPOSSIBLE"<<endl;
        else cout<<res<<endl;
    }

    return 0;
}
