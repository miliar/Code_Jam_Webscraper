#include <iostream>
#include <vector>

using namespace std;

typedef long long int LLI;

struct Loc {
    Loc(LLI xx, LLI yy) : x(xx), y(yy) {}
    LLI x;
    LLI y;
};

main() {
    int nc;
    cin >> nc;
    for (int ic=1; ic<=nc; ic++) {
        
        vector<Loc> locs;
        LLI n, a, b, c, d, x0, y0, M;
        cin >> n >> a >> b >> c >> d >> x0 >> y0 >> M;
        LLI x = x0;
        LLI y = y0;
        locs.push_back(Loc(x, y));
        // cout << x << " " << y << endl;
        for (int i=1; i<=n-1; i++) {
            x = (a*x+b)%M;
            y = (c*y+d)%M;
            locs.push_back(Loc(x, y));
            // cout << x << " " << y << endl;
        }
        int cnt = 0;
        for (int i=0; i<n; i++) {
            const Loc &li = locs[i];
            for (int j=i+1; j<n; j++) {
                const Loc &lj = locs[j];
                for (int k=j+1; k<n; k++) {
                    const Loc &lk = locs[k];
                    if ((li.x+lj.x+lk.x)%3 != 0) continue;
                    if ((li.y+lj.y+lk.y)%3 != 0) continue;
                    cnt++;
                }
            }
        }


        cout << "Case #" << ic << ": " << cnt << endl;
    }
}
