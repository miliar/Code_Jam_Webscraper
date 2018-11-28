#include <iostream>
#include <vector>
#include <stack>
#include <complex>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

typedef vector<char> VC;
typedef vector<VC> VVC;

int main()
{
    int n;
    cin >> n;
    for(int cnt=1;cnt<=n;cnt++) {
        int h, w;
        cin >> h >> w;
        VVI m(h+2, VI(w+2, -1));
        for(int i=1;i<=h;i++) {
            for(int j=1;j<=w;j++)
                cin >> m[i][j];
        }

        VVC ans(h+2, VC(w+2, '!'));
        char c = 'a';
        for(int i=1;i<=h;i++) {
            for(int j=1;j<=w;j++) {
                if(ans[i][j] != '!')
                    continue;

                typedef complex<int> pos;
                stack<pos> s;
                s.push(pos(i, j));
                while(!s.empty()) {
                    pos p = s.top();
                    s.pop();

//                    cout << "%" << real(p) << ' ' << imag(p) << endl;

                    if(ans[real(p)][imag(p)] != '!')
                        continue;
                    ans[real(p)][imag(p)] = c;
                    
                    pos dp[] = {pos(-1, 0), pos(0, -1), pos(0, 1), pos(1, 0)};
                    for(int k=0;k<4;k++) {
                        int ii = real(p+dp[k]), jj = imag(p+dp[k]);
                        if(m[ii][jj] <= m[real(p)][imag(p)])
                            continue;
                        int idx = -1;
                        int mini = 10001;
                        for(int l=0;l<4;l++) {
                            int iii = real(p+dp[k]+dp[l]), jjj = imag(p+dp[k]+dp[l]);
                            if(m[iii][jjj] != -1 && m[iii][jjj] < mini) {
                                idx = l;
                                mini = m[iii][jjj];
                            }
                        }
                        if(p+dp[k]+dp[idx] == p) {
                            s.push(p+dp[k]);
                        }
                    }
                    int idx = -1;
                    int mini = 10001;
                    for(int k=0;k<4;k++) {
                        int ii = real(p+dp[k]), jj = imag(p+dp[k]);
                        if(m[ii][jj] != -1 && m[ii][jj] < m[real(p)][imag(p)] && m[ii][jj] < mini) {
                            idx = k;
                            mini = m[ii][jj];
                        }
                    }
                    if(idx != -1) {
                        s.push(p+dp[idx]);
                    }
                }
                c++;
            }
        }
        cout << "Case #" << cnt << ":" << endl;
        for(int i=1;i<=h;i++) {
            for(int j=1;j<=w;j++) {
                if(j != 1)
                    cout << ' ';
                cout << ans[i][j];
            }
            cout << endl;
        }
    }
    
    return 0;
}
