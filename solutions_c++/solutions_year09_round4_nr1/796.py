#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;
const int INF = 1000000000;
int n;
int main() {
    int t; cin >> t;
    for (int z=1;z<=t;++z) {
        cin >> n;
        vector<string> T(n);
        for (int i=0;i<n;++i) cin >> T[i];
        vector<int> v(n,0);
        for (int i=0;i<n;++i) {
            for (int j=n-1;j>=0;--j) if (T[i][j]=='1') {
                v[i]=j;
                break;
            }
        }
        
        int ans=0;
        for (int i=0;i<n;++i) if (v[i]>i) {
            //cerr << "mal posat a " << i << " : " << v[i] << endl;
            int pos=-1;
            for (int j=i+1;j<n;++j) if (v[j]<=i) {
                pos=j;
                break;
            }
            //cerr << "trobo amic " << v[pos] << " a " << pos << endl;
            ans+=pos-i;
            for (int j=pos;j>i;--j) swap(v[j],v[j-1]);
            //for (int j=0;j<n;++j) cerr << v[j] << " "; cerr << endl;
            
        }
            
        cout << "Case #"<<z<<": " << ans << endl;
    }
}
