#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string>
#include <ctime>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <cstring>

#define pii pair <int, int>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back

const int INF = 2147483647;
const double EPS = 1E-9;
const double PI = acos(-1);

using namespace std;

char M[100][100];
double ans[100], wins[100], loss[100], WP[100], OWP[100], OOWP[100];

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, n;
    cin >> t;
    for(int q = 1; q<=t; ++q) {
        cin >> n;
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                cin >> M[i][j];

        for(int i=0; i<n; ++i) {
            ans[i] = 0; WP[i] = 0; OWP[i] = 0; OOWP[i] = 0; wins[i] = 0; loss[i] = 0;
        }

        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; ++j)
                if(M[i][j] == '1')
                    ++wins[i];
                else if(M[i][j] == '0')
                    ++loss[i];
            WP[i] = (double)wins[i]/(wins[i]+loss[i]);
        }

        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; ++j)
                if(M[i][j] != '.') {
                    if(M[i][j] == '0')
                        OWP[i] += (double)(wins[j]-1)/(wins[j]-1+loss[j]);
                    else
                        OWP[i] += (double)(wins[j])/(wins[j]-1+loss[j]);
                }
            OWP[i] /= wins[i]+loss[i];
        }

        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; ++j)
                if(M[i][j] != '.')
                    OOWP[i] += OWP[j];
            OOWP[i] /= wins[i] + loss[i];
        }

        for(int i=0; i<n; ++i)
            ans[i] = WP[i]/4 + OWP[i]/2 + OOWP[i]/4;

        cout << "Case #" << q << ":" << endl;
        for(int i=0; i<n; ++i)
            printf("%lf\n", ans[i]);
    }

    return 0;
}
