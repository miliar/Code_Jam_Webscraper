#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;
vector<pair<double, double> > peta;

int main() {

    int t;
    cin >> t;
    for(int i=1;i<=t;i++) {
        peta.clear();
        double x,s,r,tt,n;
        cin >> x >> s >> r >> tt >> n;
        double a,b,c,p = 0;
        for(int j=0;j<n;j++) {
            cin >> a >> b >> c;
            if((p-a) < 0.0000001) {
                peta.push_back(make_pair(0, a-p));
            }
            peta.push_back(make_pair(c, b-a));
            p = b;
        }

        if((p-x)<0.0000001) {
            peta.push_back(make_pair(0, x-p));
        }

        sort(peta.begin(), peta.end());
        p = 0;
        double time = 0;
        for(vector<pair<double, double> >::iterator it=peta.begin();it!=peta.end();it++) {
            if(time<tt-0.0000001) {
                if(it->second/(r+it->first) > tt-time) {
                    time += (tt-time) + (it->second-(r+it->first)*(tt-time))/(s+it->first);
                } else {
                    time += it->second/(it->first+r);
                }
            } else {
                time += it->second/(s+it->first);
            }
        }

        printf("Case #%d: %.7f\n", i, time);
    }

    return 0;
}

