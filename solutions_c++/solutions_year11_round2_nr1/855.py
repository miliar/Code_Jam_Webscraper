#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pi pair<int, int>
#define MP make_pair
#define X first
#define Y second

int N;
string a[110];

double wp[110], owp[110], oowp[110], rpi[110];
int pl[110];

int main()
{
    int T, i, j, k;
    cin >> T;
    for(int caso=1; caso<=T; caso++) {
        cin >> N;
        for(i=0; i<N; i++) {
            cin >> a[i];
            pl[i] = 0;
            wp[i] = 0.0;
            for(j=0; j<SZ(a[i]); j++) {
                if(a[i][j] != '.') pl[i]++;
                if(a[i][j] == '1') wp[i] += 1.0;
            }
            wp[i] /= (double)pl[i];
        }
        
        for(i=0; i<N; i++) {
            owp[i] = 0.0;
            for(j=0; j<SZ(a[i]); j++) {
                if(a[i][j] == '0') owp[i] += wp[j]*(double)pl[j]/(double)(pl[j]-1) - 1.0/(double)(pl[j]-1);
                else if(a[i][j] == '1') owp[i] += wp[j]*(double)pl[j]/(double)(pl[j]-1);
            }
            owp[i] /= (double)pl[i];
        }
        
        for(i=0; i<N; i++) {
            oowp[i] = 0.0;
            for(j=0; j<SZ(a[i]); j++) {
                if(a[i][j] != '.') oowp[i] += owp[j];
            }
            oowp[i] /= (double)pl[i];
        }
        
        printf("Case #%d:\n", caso);
        for(i=0; i<N; i++) {
            rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
            printf("%.12lf\n", rpi[i]);
        }
    }
    
    return 0;
}
