#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int T, n, s, p, x;
    cin >>T;
    for(int t=1; t<=T; t++) {
        vector<int> vs, vns;
        cin >> n >> s >> p;
        for(int i=0; i<n; i++) {
            cin >> x;
            if(x==0) {
                vs.push_back(0);
                vns.push_back(0);
                continue;
            }
            int r=x%3;
            if(r==0) {
                vs.push_back(x/3+1);
                vns.push_back(x/3);
            }
            else if(r==1) {
                vs.push_back(x/3+1);
                vns.push_back(x/3+1);
            }
            else if(r==2) {
                vs.push_back(x/3+2);
                vns.push_back(x/3+1);
            }
        }

        int ctr1=0;
        int ctr2=0;
        
        for(int i=0; i<vs.size(); i++) {
            if(vs[i]<p && vns[i]<p) {
                continue;
            }
            if(vs[i]>=p && vns[i]<p) {
                ctr1++;
            }
            if(vs[i]>=p && vns[i]>=p) {
                ctr2++;
            }       
        }
        int ans=0;
        
        if(s < ctr1) {
            ans+=s;
        }
        else
            ans+=ctr1;
        
        ans+=ctr2;         
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
