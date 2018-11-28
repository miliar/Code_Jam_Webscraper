#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <queue>
using namespace std;

#define llong long long

llong l,t,n,c;

vector<pair<llong, llong> > dists;
vector<llong> psum;

llong score(const pair<llong,llong> &a) {
    llong dist=a.first;
    llong star=a.second;
    if(psum[star]<t) {
        if(psum[star]+dist<=t) return 0;
        else return (psum[star]+dist-t)/2;
    } else {
        return dist/2;
    }
}

bool best(const pair<llong,llong> &a, const pair<llong, llong> &b) {
    llong aa=score(a), bb=score(b);
    return aa>bb;
}

void solve() {
    llong tot=0;
    cin>>l>>t>>n>>c;
    vector<llong> as(c);
    psum.clear();
    dists.clear();
    psum.push_back(0);
    for(int i=0;i<c;i++) {
        cin>>as[i];
        as[i]*=2;
    }
    llong idx=0;
    while(idx<n) {
        for(int i=0;i<c&&idx<n;i++) {
            dists.push_back(make_pair(as[i], idx++));
            psum.push_back(psum.back()+as[i]);
            tot+=as[i];
        }
    }
    sort(dists.begin(),dists.end(),best);
    llong ret=0;
    for(int i=0;i<dists.size()&&i<l;i++) {
        llong save=score(dists[i]);
        ret+=save;
    }
    llong res=tot-ret;
    cout<<res<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int cnum=1;cnum<=cases;cnum++) {
        cout<<"Case #"<<cnum<<": ";
        solve();
    }
}
