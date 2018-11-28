#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {
    int t; cin>>t;
    for (int i=0;i<t;i++) {
        cout<<"Case #"<<i+1<<": ";
        ll n,k;
        cin>>n>>k;
        ll x = 1<<n;
        if (x-1==k%x) cout<<"ON"<<endl; else cout<<"OFF"<<endl;    
    }
}
