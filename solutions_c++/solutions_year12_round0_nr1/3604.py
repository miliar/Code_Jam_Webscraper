#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
template <typename T> inline bool checkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template <typename T> inline bool checkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
typedef long long lint;

//char s[2][3][100];
const char trans[30] = "yhesocvxduiglbkrztnwjpfmaq";
char s[10000];

int main() {
    //REP(i, 2) {
        //REP(j, 3) {
            //gets(s[i][j]);
            //out(s[i][j]);
        //}
    //}
    //REP(j, 3) {
        //int len = strlen(s[0][j]);
        //REP(i, len) {
            //if (s[0][j][i] == ' ') continue;
            //int from = s[0][j][i] - 'a';
            //trans[from] = s[1][j][i];
            //printf("%d %c\n", from, s[1][j][i]);
        //}
    //}
    //trans[26] = '\0';
    //REP(i, 26) {
        //if (trans[i] < 'a' || trans[i] > 'z') {
            //trans[i] = '*';
        //}
    //}
    //puts(trans);
    freopen("a1.out", "w", stdout);
    int T, t = 0;
    scanf("%d", &T);
    for (scanf("%d", &T); t < T; ++t) {
        gets(s);
        printf("Case #%d: ", t + 1);
        int len = strlen(s);
        REP(i, len) {
            if (s[i] == ' ') {
                printf(" ");
                continue;
            }
            printf("%c", trans[s[i] - 'a']);
        }
        puts("");
    }
    return 0;
}

