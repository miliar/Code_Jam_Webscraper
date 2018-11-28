#include <iostream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

string w[100];
int tot[100];
int won[100];
double rowp[100], rwp[100], roowp[100];
int main() {
    int T;
    cin>>T;
    int t = 0;
    while (T--) {
        t++;
        int N;
        cin>>N;
        for (int i=0;i<N;i++) {
            cin>>w[i];
        }
        memset(tot,0,sizeof(tot));
        memset(won,0,sizeof(won));
        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                if (w[i][j] == '.') continue;
                if (w[i][j] == '1') {
                    tot[i]++;
                    won[i]++;
                } else {
                    tot[i]++;
                }
            }
        }
        for (int i=0;i<N;i++) {
            double wp=0, owp = 0, oowp = 0;
            wp = tot[i] / (double)won[i];
            rwp[i] = 1.0 / wp;
            int cnt = 0;
            for (int j=0;j<N;j++) {
                if (w[i][j] == '.') continue;
                cnt++;
                if (w[i][j] == '1') {
                    owp += won[j] / (double)(tot[j]-1);     
                } else {
                    owp += (won[j]-1) / (double)(tot[j]-1);     
                }
            }
            owp /= cnt;
            rowp[i] = owp;
        }
        for (int i=0;i<N;i++) {
            roowp[i] = 0;
            int cnt = 0;
            for (int j=0;j<N;j++) {
                if (w[i][j] == '.') continue;
                cnt++;
                roowp[i] += rowp[j];
            }
            roowp[i] /= cnt;
        }
        cout << "Case #" << t << ":" << endl;
        for (int i=0;i<N;i++) {
            cout << 0.25 * rwp[i] + 0.5 * rowp[i] + 0.25 * roowp[i] << endl;
        }
    }
}
