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

int T; cin>>T;
cout.setf(ios::fixed, ios::floatfield); cout.precision(9);
for (int tt=0;tt<T;tt++) {
    int X,S,R,N;
    double t;
    cin>>X>>S>>R>>t>>N;
    R-=S;
    vector<pair<double,double> > a;
    int dist=0;
    for (int i=0;i<N;i++) {
        int B,E,w;
        cin>>B>>E>>w;
        a.PB(MP(w+S,E-B));
        dist+=E-B;
       // cout<<"$$ "<<a[i].second<<" , "<<a[i].first<<" "<<a[i].second/a[i].first<<endl;
    }
    if (X-dist>0) { a.PB(MP(S,X-dist));}
    sort (a.begin(),a.end());
    for (int i=0;i<a.size();i++) if (t>1e-9) {
        double vzd=a[i].second;
        double rych = a[i].first;
        double cas = vzd/(rych+R);
        if (cas<=t) {
           t-=cas;
           a[i].first+=R;           
        } else {
           double d1 =(rych+R)*t;
           double d2 = vzd-d1;
           a[i].first+=R;
           a[i].second = d1;
           a.PB(MP(rych,d2));
           break;
        }
    }   
    double res=0;
    for (int i=0;i<a.size();i++) {
        //cout<<"! "<<a[i].second<<" , "<<a[i].first<<" "<<a[i].second/a[i].first<<endl;
        res+=a[i].second/a[i].first;    
    }
    
    cout<<"Case #"<<tt+1<<": "<<res<<endl;
}
    
}
