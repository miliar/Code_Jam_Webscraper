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

vector<double> length, speed;
int n;
double s, r, t, x;

pair<double, double> compute(double length, double speed) {
    double otime=length/speed;
    double newspeed=speed+r-s;
    double treq=length/newspeed;
    double ntime=0;
    if(treq>t) {
        double ndist=t*newspeed;
        ntime=t+(length-ndist)/speed;
    } else {
        ntime=treq;
    }
    return make_pair(otime-ntime, min(treq, t));
}

void solve() {
    cin>>x>>s>>r>>t>>n;
    length=vector<double>();
    speed=vector<double>();
    int start,end,sp;
    int last=0;
    for(int i=0;i<n;i++) {
        cin>>start>>end>>sp;
        if(start!=last) {
            length.push_back(start-last);
            speed.push_back(s);
        }
        length.push_back(end-start);
        speed.push_back(sp+s);
        last=end;
    }
    if(last!=x) {
        length.push_back(x-last);
        speed.push_back(s);
    }
    double ret=0;
    for(int i=0;i<length.size();i++)
        ret+=length[i]/speed[i];
    vector<int> vis(length.size());
    for(int i=0;i<length.size();i++) {
        pair<double,double> best=make_pair(0,1);
        int bestidx=-1;
        for(int j=0;j<length.size();j++) if(!vis[j]) {
            //saved, takes
            pair<double, double> val=compute(length[j], speed[j]);
            if(val.first/val.second>best.first/best.second) {
                best=val;
                bestidx=j;
            }
        }
        if(bestidx!=-1) {
            ret-=best.first;
            t-=best.second;
            vis[bestidx]=1;
        }
    }
    cout.setf(ios::fixed);
    cout<<setprecision(9)<<ret<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int cnum=1;cnum<=cases;cnum++) {
        cout<<"Case #"<<cnum<<": ";
        solve();
    }
}
