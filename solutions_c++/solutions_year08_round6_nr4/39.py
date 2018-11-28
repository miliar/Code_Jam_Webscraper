#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

typedef long long ll;

int E1[101][101];
int E2[101][101];
int N, M;
int chosen[101];
bool possible;

void back(int p) {
    /*
    cout <<"P:" <<p <<endl;
    REP(i, p) {
        cout <<chosen[i] << " ";
    }
    cout <<endl;
    */
    if (p == M) {
        //
        //  Check whether it is connected
        //

        /*
        int NE2[10][10];
        CLR(NE2, 0);
        REP(i, 
        */
        possible = true;
        /*
        REP(i, M) {
            cout <<chosen[i] << " ";
        }
        cout <<"!!" <<endl;
        */
        return;
    }
    REP(i, N) {
        bool already = false;
        bool notex = false;
        REP(j, p) {
            if (chosen[j] == i) {
                already = true;
                break;
            }
            int cc = chosen[j];
            if (E1[cc][i] && !E2[j][p]) {
                notex = true;
                break;
            }
            if (!E1[cc][i] && E2[j][p]) {
                notex = true;
                break;
            }
            if (E1[cc][i]) {
                //printf("E1: %d %d   E2: %d %d\n", cc, i, j, p);
            }
        }
        if (already || notex) continue;
        chosen[p] = i;
        back(p+1);
        if (possible) return;
    }
}

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        CLR(E1, 0);
        CLR(E2, 0);
        cin >>N;
        REP(i, N-1) {
            int a, b;
            cin >>a >>b;
            a--; b--;
            E1[a][b] = 1;
            E1[b][a] = 1;
        }
        cin >>M;
        REP(i, M-1) {
            int a, b;
            cin >>a >>b;
            a--; b--;
            E2[a][b] = 1;
            E2[b][a] = 1;
        }
        possible = false;
        back(0);
        if (!possible)
            cout <<"NO" <<endl;
        else
            cout <<"YES" <<endl;
        
    }
    return 0;

}

