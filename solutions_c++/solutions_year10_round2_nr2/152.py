#include <iostream>
#include <vector>

using namespace std;



int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        int chickN, chickGoal;
        long long dist, tm;
        cin >> chickN >> chickGoal >>  dist >> tm;

        vector<long long> x(chickN);
        vector<long long> v(chickN);
        for(int i=0; i<chickN; i++) cin >> x[i];
        for(int i=0; i<chickN; i++) cin >> v[i];

        int ans = 0;
        int gotChicks=0, skipChicks=0;
        for(int i=chickN-1; i>=0 && gotChicks<chickGoal; i--) {
            if ((dist - x[i]) <= (v[i] * tm)) { gotChicks++; ans+= skipChicks; }
            else { skipChicks++; }
        }

        cout << "Case #" <<(c+1) << ": ";
        if(gotChicks<chickGoal) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << endl;
    }
}
