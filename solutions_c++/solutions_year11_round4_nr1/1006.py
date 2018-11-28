#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;

int w[1001],b[1001],e[1001],back[2059];
double dp[2059];

struct Node {
    int x,ei;
    vector<pair<int,double> > edges;
    Node(int x) : x(x) {;}
};

bool operator<(const Node &n,const Node &m) {
    return n.x < m.x;
}

int main() {
    int testcase,tc=1;
    cin>>testcase;

    int n,s,r,t,X;
    for(tc=1; tc<=testcase; ++tc) {
        cin>>X>>s>>r>>t>>n;

        map<int,int> d;
        for(int i=0; i<n; ++i) {
            cin>>b[i]>>e[i]>>w[i];
            d[w[i]] += e[i] - b[i];
        }

        sort(b,b+n);
        sort(e,e+n);

        d[0] += b[0];
        for(int i=0; i<n-1; ++i) {
            d[0] += b[i+1] - e[i];
        }
        d[0] += X - e[n-1];

        vector<pair<int,int> > pv;
        for(map<int,int>::iterator it = d.begin(); it != d.end(); ++it) {
            pv.push_back(make_pair(it->first,it->second));
        }

        sort(pv.begin(), pv.end());
//        reverse(pv.begin(), pv.end());
        double rem = t,ans = 0;
        for(vector<pair<int,int> >::iterator it = pv.begin(); it != pv.end(); ++it) {
            int speed;
            speed = r+it->first;
//            cout<<it->first<<" "<<it->second<<" "<<speed<<endl;
            double ut = (double)it->second/speed;
//            cout<<"ut = "<<ut<<endl;
            if(ut > rem) {
                double dist = it->second - rem*speed;
                ans += rem;
                rem = 0;
                ans += dist/(it->first+s);
            }else{
                ans += ut;
                rem -= ut;
            }
        }
        printf("Case #%d: %.8f\n", tc, ans);
    }
}
