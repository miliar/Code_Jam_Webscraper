#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        long long l, t, n, c;
        cin >> l >> t >> n >> c;

        vector<long long> a(c, 0);
        for(long long i=0;i<c;i++) {
            cin >> a[i];
        }

        vector<long long> d(n, 0);
        for(long long i=0;i<n;i++) {
            d[i] = a[i%c];
        }

        vector<long long> t1, d2;

        long long tt = t;
        for(long long i=0;i<n;i++) {
            if(d[i]*2 >= tt) {
                t1.push_back(tt);
                d2.push_back(d[i]-tt/2);
                for(long long j=i+1;j<n;j++) {
                    d2.push_back(d[j]);
                }
                break;
            }
            else {
                t1.push_back(d[i]*2);
                tt -= d[i]*2;
            }
        }

        sort(d2.begin(), d2.end(), greater<long long>());
        for(int i=min((unsigned int)l,d2.size());i<d2.size();i++) {
            d2[i] *= 2;
        }

        long long ans = 0;
        for(int i=0;i<t1.size();i++) {
            ans += t1[i];
        }
        for(int i=0;i<d2.size();i++) {
            ans += d2[i];
        }

        cout << "Case #" << tc << ": " << ans << endl;
    }

    return 0;
}
