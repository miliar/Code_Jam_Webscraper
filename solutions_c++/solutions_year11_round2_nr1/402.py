#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
char gamePlan[110][110];
void solve() {
    int n;
    scanf("%d", &n);
    double WP[110], OWP[110], OOWP[110];
    for (int i = 0; i < n; i++) {
        scanf("%s", gamePlan[i]);
    }

    for (int i = 0; i < n; i++) {
        WP[i] = 0;
        int total = 0;
        for (int j = 0; j < n; j++) {
            if (gamePlan[i][j] == '1') {
                WP[i]++;
                total++;
            }
            else if (gamePlan[i][j] == '0') total++;
        }
        WP[i] /= total;
        cerr<<WP[i]<<endl;
    }

    for (int i = 0; i < n; i++) {
        OWP[i] = 0;
        int total = 0;
        for (int j = 0; j < n; j++)
            if (gamePlan[i][j] != '.') {
                total++;
                int tt = 0;
                double tmp = 0;
                for (int k = 0; k < n; k++)
                    if (k != i && gamePlan[j][k] != '.') {
                        tt++;
                        if (gamePlan[j][k] == '1')
                            tmp++;
                    }
                OWP[i] += (tmp / tt);
            }
        OWP[i] /= total;
        cerr<<OWP[i]<<endl;
    }
    for (int i = 0; i < n; i++) {
        int total = 0;
        OOWP[i] = 0;
        for (int j = 0; j < n; j++)
            if (gamePlan[i][j] != '.') {
                OOWP[i] += OWP[j];
                total++;
            }
        OOWP[i] /= total;
        cerr<<OOWP[i]<<endl;
    }

    for (int i = 0; i < n; i++) {
        printf("%.8lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
    }


}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int totalCase;
    scanf("%d", &totalCase);
    for (int Case = 1; Case <= totalCase; Case++) {
        printf("Case #%d:\n", Case);
        solve();
        cerr<<"Test "<<Case<<" out of "<<totalCase<<" completed."<<endl;
    }
}
