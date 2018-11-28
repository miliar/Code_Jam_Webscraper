#include <iostream>
#include <set>
#include <utility>

using namespace std;

int main()
{
    int np;
    cin >> np;
    
    for (int i=0; i<np; ++i) {

        int n, a, b, c, d, x0, y0, m;

        cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
        
        set<pair<int,int> > pts;
        int X = x0;
        int Y = y0;
        pts.insert(make_pair(X,Y));
        for (int k=1; k<n; ++k) {
            X = ((long long)a*(long long)X + b) % m;
            Y = ((long long)c*(long long)Y + d) % m;
            pts.insert(make_pair(X,Y));
        }
        
        int cnt = 0;
        set<pair<int,int> > :: iterator it, jt, kt;
        for (it=pts.begin(); it!=pts.end(); ++it) {
            jt = it;
            ++jt;
            for (; jt!=pts.end(); ++jt) {
                kt = jt;
                ++kt;
                for (; kt!=pts.end(); ++kt) {
                    if ((it->first + jt->first + kt->first) % 3)
                        continue;
                    if ((it->second + jt->second + kt->second) % 3)
                        continue;
                    ++cnt;
                }
            }
        }

        cout << "Case #" << i+1 << ": " << cnt;
        cout << endl;
    }
}
