#include <iostream>
#include <vector>
#include <math.h>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <string.h>
#include <stack>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
using namespace std;

const int maxn = 105;

int n;
char mat[maxn][maxn];

int win[maxn],cnt[maxn];

double wp[maxn];
double owp[maxn];
double oowp[maxn];

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
    int tests; scanf("%d",&tests);

    for( int t = 1; t <= tests; ++t ){
        scanf("%d",&n);
        for( int i = 0; i < n; ++i ){
            scanf("%s",mat[i]);
            win[i] = cnt[i] = 0;

            for( int j = 0; j < n; ++j ){
                win[i] += mat[i][j] == '1';
                cnt[i] += mat[i][j] != '.';
            }
            wp[i] = win[i] / (double)cnt[i];
        }

        for( int i = 0; i < n; ++i ){

            double ss = 0;

            for( int j = 0; j < n; ++j ){
                if( mat[i][j] == '.' ) continue;
                int w = win[j], c = cnt[j];
                w -= mat[j][i] == '1';
                c -= mat[j][i] != '.';
                ss += w / (double)c;
            }
            owp[i] = ss/(double)cnt[i];
        }

        for( int i = 0; i < n; ++i ){
            double ss = 0;
            for( int j = 0; j < n; ++j ){
                if( mat[i][j] == '.' ) continue;
                ss += owp[j];
            }
            oowp[i] = ss / (double)cnt[i];
        }

        printf("Case #%d:\n",t);

        for( int i = 0; i < n; ++i )
            printf("%.10lf\n",0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]);
    }

    return 0;
}

