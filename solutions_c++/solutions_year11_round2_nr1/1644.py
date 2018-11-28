#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <iterator>
#include <cassert>

#define FOR(i,s,n) for((i)=(s);(i)<(int)(n);(i)++)
#define FORD(i,s,n) for((i)=(s);(i)>=(int)(n);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

#define isnbit(d, n) ((d>>n)&1)

using namespace std;

int wins[101];
int num[101];
double wps[101];
double owps[101];
double oowps[101];

int run(int ncase){
    int i, j, k;
    int N;
    vector<string> sche;
    double wp, owp, oowp;

    cin >> N;
    sche.resize(N);

    FOR(i, 0, N)
        cin >> sche[i];

    int win;
    int n;

    FOR(i, 0, N){
        win = 0;
        n = 0;
        FOR(j, 0, N){
            char c = sche[i][j];
            if(c == '0'){
                n++;
            }else if(c == '1'){
                win++;
                n++;
            }
        }

        wins[i] = win;
        num[i] = n;
        wps[i] = (double)wins[i]/num[i];
    }

    FOR(i, 0, N){
        owp = 0;
        n = 0;
        FOR(j, 0, N){
            char c = sche[i][j];
            if(c == '0'){
                if(num[j] != 1){
                    owp += (double)(wins[j]-1)/(num[j]-1);
                    n++;
                }
            }else if(c == '1'){
                if(num[j] != 1){
                    owp += (double)(wins[j]  )/(num[j]-1);
                    n++;
                }
            }
        }
        owp = owp/n;
        owps[i] = owp;
    }

    double sum = 0;
    FOR(i, 0, N){
        sum += owps[i];
    }

    FOR(i, 0, N){
        n = 0;
        oowps[i] = 0;
        FOR(j, 0, N){
            char c = sche[i][j];
            if(c == '.') continue;
            oowps[i] += owps[j];
            n++;
        }
        oowps[i] = oowps[i]/n;
    }

    cout << "Case #" << ncase << ":" << endl;
    FOR(i, 0, N){
        double ans;
        ans = wps[i] * 0.25 + owps[i] * 0.5 + oowps[i] * 0.25;
        cout << ans << endl;
    }

        

    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    //cin.ignore();
    FOR(i, 0, test_set) run(i+1);
    return 0;
}
