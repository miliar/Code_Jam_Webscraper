#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin>>n;
    cin.get();
    for (int i = 1; i <= n; ++i) {
        int m;
        cin>>m;
        int po = 1, pb = 1, so = 0, sb = 0;
        for (int k = 0; k < m; ++k) {
            char c;
            int d, cd;
            cin>>c>>d;
            if (c == 'O') {
                cd = abs(po - d) + 1;
                so = max(so + cd, sb + 1);
                po = d;
            }
            else {
                cd = abs(pb - d) + 1;
                sb = max(sb + cd, so + 1);
                pb = d;
            }
        }

        cout<<"Case #"<<i<<':';
        cout<<' '<<max(so, sb);
        cout<<'\n';
    }

    return 0;
}
