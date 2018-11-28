#include <stdio.h>
#include <string.h>

#define FOR(i,n) for((i)=0;(i)<(n);(i)++)
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define _FORIT(it, b, e) for (__typeof(b) it = (b); it != (e); it++)
#define FORIT(x...) _FORIT(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define CLR(a,v) memset((a),(v),sizeof(a)) 
#define TLE while(1);
#define RTE printf("%d", 1/0);

char words[10000][20];
char padrao[20][256];
int L, D, N;
int sum;

int main() {
    
    int i, j, k, l, x = 1;
    char str[100000];
    scanf("%d %d %d", &L, &D, &N);
    FOR(i, D) scanf("%s", words[i]);
    FOR(l, N) {
        sum = 0; CLR(padrao, 0);
        scanf("%s", str);
        for (i = 0, j = 0, k = 0; str[i]; i++) {
            if (str[i]=='(') k = 1;
            if (str[i]!='(' && str[i]!=')') padrao[j][str[i]] = 1;
            if (!k) j++;
            if (str[i]==')') j++, k = 0;
        }
        FOR(i, D) {
            for (j = 0; j < L; j++) if (!padrao[j][words[i][j]]) break;
            if (j==L) sum++;
        }
        printf("Case #%d: %d\n", x++, sum);
    }
    
    return 0;
}
