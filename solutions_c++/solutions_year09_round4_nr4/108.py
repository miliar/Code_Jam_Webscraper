#include <iostream>
#include <cmath>
#include <vector>

using namespace std;


double dist(int x1, int y1, int x2, int y2) {
    return sqrt(1.*(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        int N;
        cin >> N;
        vector<int> x(N);
        vector<int> y(N);
        vector<int> r(N);

        for(int i=0; i<N; i++) cin >> x[i] >> y[i] >> r[i];

        double ans = 0;
        if (N == 1) ans = r[0];
        else if (N == 2) ans = r[0] >? r[1];
        else {
            vector<int> p;
            for(int o=0; o<3; o++) p.push_back(o);
            
            ans = 1E200;
            do {
                double curans = r[p[2]];
                curans >?= (dist(x[p[0]], y[p[0]], x[p[1]], y[p[1]]) + r[p[0]] + r[p[1]]) / 2.0;
                ans <?= curans;
            }while(next_permutation(p.begin(), p.end()));
        }

        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
