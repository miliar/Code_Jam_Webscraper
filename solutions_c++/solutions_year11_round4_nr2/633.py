#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <queue>
#include <stack>

using namespace std;

int solve() {
    int r,c,d;
    vector<string> field;
    int res = -1;
    cin >> r >> c >> d;
    for(int i=0; i<r; i++) {
        string tmp;
        cin >> tmp;
        field.push_back(tmp);
    }
    for (int i=min(r,c); i>=3; i--) {
        for (int j=0; j<r-i+1; j++) {
            for (int k=0; k<c-i+1; k++) {
                int xw=0,yw=0;
                for (int l=0; l<i; l++) {
                    for (int m=0; m<i; m++) {
                        if (l==0&&m==0||l==0&&m==i-1||l==i-1&&m==0||l==i-1&&m==i-1){
                            continue;
                        }
                        //cout << l+j << "," << m+k;
                        xw+=(field[l+j][m+k]-'0')*(i-(l*2+1));
                        yw+=(field[l+j][m+k]-'0')*(i-(m*2+1));
                        //cout << "," << xw << "," << yw << endl;
                    }
                }
                if (xw==0&&yw==0) {
                    res=i;
                    goto end;
                }
            }
        }
    }
end:
    return res;
}

int main() {
    int T;
    cin >> T;
    cout << setprecision(16);
    for (int i=0; i<T; i++) {
        int ret = solve();
        cout << "Case #" << i+1 << ": ";
        if (ret == -1)cout << "IMPOSSIBLE" << endl;
        else cout << ret << endl;
    }
    return 0;
}
