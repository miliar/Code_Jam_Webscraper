#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
using namespace std;

pair<pair<long double, long double>, long double> b[100000];

const long double eps=1e-8;

bool eq0(long double a){
     return (-eps<a && a<eps);
}

bool cmp0(pair<pair<long double, long double>, long double> a, pair<pair<long double, long double>, long double> b){
     if (a.second!=b.second)
        return a.second<b.second;
     else
         return a.first<b.first;
}

void solve(){
     int n;
     long double r, s, x, t;   
     cin>>x>>s>>r>>t>>n;
     r-=s;
     long double ans=0;
     for (int i=0; i<n; ++i){
         cin>>b[i].first.first>>b[i].first.second>>b[i].second;
         b[i].second+=s;
     }
     sort(b, b+n);
     long double cur=0;
     int n0=n;
     for (int i=0; i<n0; ++i){
         if (!eq0(b[i].first.first-cur)){
            b[n++]=make_pair(make_pair(cur, b[i].first.first), s);
         }
         cur=b[i].first.second;
     }
     b[n++]=make_pair(make_pair(b[n0-1].first.second, x), s);
     sort(b, b+n, cmp0);
     for (int i=0; i<n; ++i){
         if (!eq0(t)){
            if ((b[i].first.second-b[i].first.first)<(b[i].second+r)*t){
               t-=(b[i].first.second-b[i].first.first)/(b[i].second+r);
               b[i].second+=r;
            }
            else{
                 b[i].first.first+=t*(b[i].second+r);
                 ans+=t;
                 t=0;
            }
         }
     }
     sort(b, b+n);
     for (int i=0; i<n; ++i){
         ans+=(b[i].first.second-b[i].first.first)/b[i].second;
     }
     cout<<fixed<<setprecision(15)<<ans;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin>>t;
    for (int i=0; i<t; ++i){
        cout<<"Case #"<<i+1<<": ";
        solve();
        cout<<endl;
    }
}
