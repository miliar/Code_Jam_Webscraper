#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

const char tran[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

char ss1[10000], ss2[10000];
char ww[26];
char ss[1000005];
void init()
{
    FILE *f1 = fopen("sample_in.txt", "r");
    FILE *f2 = fopen("sample_out.txt", "r");
    FILE *fout = fopen("tran.out", "w");
    while (fscanf(f1, "%s", ss1) != EOF && fscanf(f2, "%s", ss2) != EOF) {
        int len = strlen(ss1);
        if (len != strlen(ss2)) {
            fprintf(stderr, "not equ len!\n");
            return;
        }
        for (int i = 0; i < len; ++i) {
            if (ss1[i] < 'a' || ss1[i] > 'z' || ss2[i] < 'a' || ss2[i] > 'z') {
                fprintf(stderr, "include non-letter!\n");
                return;
            }
            if (ww[ss1[i] - 'a'] > 0 && ww[ss1[i] - 'a'] != ss2[i]) {
                fprintf(stderr, "not equ tran!\n");
                return;
            }
            ww[ss1[i] - 'a'] = ss2[i];
        }
    }
    for (int i = 0; i < 26; ++i) {
        if (ww[i] == 0) {
            fprintf(stderr, "%c no tran!\n", 'a' + i);
        }
        if (i) fprintf(fout, ", ");
        fprintf(fout, "'%c'", ww[i]);
    }
}
int main()
{
    //init();
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    fgets(ss, 1000000, stdin);
    for (int ca = 1; ca <= T; ++ca) {
        fgets(ss, 1000000, stdin);
        int len = strlen(ss);
        while (len > 0 && (ss[len - 1] == '\r' || ss[len - 1] == '\n')) len--;
        ss[len] = 0;
        for (int i = 0; i < len; ++i) {
            if (ss[i] >= 'a' && ss[i] <= 'z') ss[i] = tran[ss[i] - 'a'];
        }
        printf("Case #%d: %s\n", ca, ss);
    }
    return 0;
}
