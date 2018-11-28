#include <iostream>

#define forn(i,n) for(int i = 0; i < n; ++i)

using namespace std;

char a[120][120];
double wp[120], owp[120], oowp[120];

int main()
{
    cout << fixed;
    cout.precision(15);
    int T, n;
    cin >> T;
    forn(t, T){
        cin >> n;
        string s;
        forn(i, n){
            double cnt = 0, sum = 0;
            cin >> s;
            forn(j, n){
                a[i][j] = s[j];
                cnt += a[i][j] != '.';
                sum += a[i][j] == '1';
            }
            wp[i] = sum / cnt;
        }
        forn(i, n){
            double cnt = 0, sum = 0;
            forn(j, n)
                if(a[j][i] != '.'){
                    double cnt1 = 0, sum1 = 0;
                    forn(k, n)
                        if(k != i && a[j][k] != '.'){
                            cnt1 += 1;
                            sum1 += a[j][k] == '1';
                        }
                    cnt += 1;
                    sum += sum1 / cnt1;
                }
            owp[i] = sum / cnt;
        }
        forn(i, n){
            double cnt = 0, sum = 0;
            forn(j, n)
                if(a[i][j] != '.'){
                    cnt += 1;
                    sum += owp[j];
                }
            oowp[i] = sum / cnt;
        }
        cout << "Case #" << t + 1 << ":" << endl;
        forn(i, n)
            cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
    }
    return 0;
}
