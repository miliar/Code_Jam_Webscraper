#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int T;
    int N;

    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        cin >> N;

        vector<string> v(N);
        vector<double> wp(N), owp(N), oowp(N);
        vector<pair<int, int> > aa(N);
        for(int i=0;i<N;i++) cin >> v[i];

        for(int i=0;i<N;i++) {
            int cnt=0, win=0;
            for(int j=0;j<N;j++) {
                if(v[i][j]=='1') win++;
                if(v[i][j]!='.') cnt++;
            }
            wp[i] = win/(double)cnt;
            aa[i] = make_pair(win, cnt);
        }

        for(int i=0;i<N;i++) {
            int cnt=0;
            double sum=0;
            for(int j=0;j<N;j++) {
                if(v[i][j]!='.') { 
                    if(v[i][j]=='1') sum += (aa[j].first)/(aa[j].second-1.);
                    else sum += (aa[j].first-1.)/(aa[j].second-1.);
                    cnt++;
                }
            }
            owp[i] = sum/cnt;
        }

        for(int i=0;i<N;i++) {
            int cnt=0;
            double sum=0;
            for(int j=0;j<N;j++) {
                if(v[i][j]!='.') { sum+=owp[j]; cnt++; }
            }
            oowp[i] = sum/cnt;
        }

        printf("Case #%d:\n", tc);
        for(int i=0;i<N;i++) {
            cout << 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] << endl;
        }
    }

    return 0;
}
