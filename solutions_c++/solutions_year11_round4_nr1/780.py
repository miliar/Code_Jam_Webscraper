#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <queue>
#include <stack>

using namespace std;

double solve() {
    int x,s,r,n;
    double t;
    double res;
    vector<pair<int,int> > w;
    cin >> x >> s >> r >> t >> n;
    for (int i=0; i<n; i++) {
        int bb,ee,ww;
        cin >> bb >> ee >> ww;
        w.push_back(make_pair(ww,ee-bb));
        x-=ee-bb;
    }
    w.push_back(make_pair(0,x));
    sort(w.begin(), w.end());
    for (int i=0; i<w.size(); i++) {
        if (t<=0) {
            res+=(double)(w[i].second)/(w[i].first+s);
        } else {
            if ((double)(w[i].second)/(w[i].first+r)<=t) {
                t-=(double)(w[i].second)/(w[i].first+r);
                res+=(double)(w[i].second)/(w[i].first+r);
            } else {
                res += (double)((double)(w[i].second)-t*(w[i].first+r))/(w[i].first+s)+t;
                t=0;
            }
        }
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    cout << setprecision(16);
    for (int i=0; i<T; i++) {
        cout << "Case #" << i+1 << ": " << solve() << endl;
    }
    return 0;
}
