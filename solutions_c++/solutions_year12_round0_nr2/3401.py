#include<iostream>
using namespace std;
int main()
{
    int t;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    cin >> t;
    for (int tt = 1; tt <= t; tt ++) {
        int n,s,p;
        int ans = 0;
        int m;
        cin >> n >> s >> p;
        for (int i = 0; i < n; i ++ ) {
            cin >> m;
            
            if (p == 1) {
                if (m >= 1) ans ++;
                continue;
            }

            if (m >= 3*p - 2) ans ++;
            else if (m >= 3*p - 4) {
                if (s > 0) ans ++, s--;
            }
        }
        cout <<"Case #"<< tt <<": "<< ans << endl;
    }
    return 0;
}
