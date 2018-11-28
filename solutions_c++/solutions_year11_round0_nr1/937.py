#include <cstdio>
#include <algorithm>
#include <cstdlib>

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define FOREACH(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ITER(c) __typeof((c).begin())
#define SZ(a) (int)(a).size()

#define MAXS 100

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w+", stdout);
    int n;
    scanf("%d", &n);
    REP(i, n) {
        int nb, seq[MAXS], pos1 = 1, pos2 = 1, sum = 0, k, dis;
        char seqc[MAXS], buff;
        scanf("%d", &nb);
        REP(j, nb) {
            while (buff != 'O' && buff != 'B') 
                scanf("%c", &buff);
            seqc[j] = buff;
            scanf("%d", &seq[j]);
            buff = 'a';
        }
        // REP(j, nb) printf("%c-%d\n", seqc[j], seq[j]);
        REP(j, nb) {
            if (seqc[j] == 'O') {
                dis = abs(seq[j] - pos1) + 1;
                sum += dis;
                pos1 = seq[j];
                k = j + 1;
                while(seqc[k] != 'B' && k < nb) k++;
                pos2 += (seq[k] > pos2) ? min(abs(seq[k]-pos2), dis) : -min(abs(seq[k]-pos2), dis);
                // printf("%d %c %d %d %d %d\n", j+1, seqc[j], dis, pos1, pos2, k);
            } else {
                dis = abs(seq[j] - pos2) + 1;
                sum += dis;
                pos2 = seq[j];
                k = j + 1;
                while(seqc[k] != 'O' && k < nb) k++;
                pos1 += (seq[k] > pos1) ? min(abs(seq[k]-pos1), dis) : -min(abs(seq[k]-pos1), dis);
                // printf("%d %c %d %d %d %d\n", j+1, seqc[j], dis, pos2, pos1, k);
            }
            // printf("%d %d\n", pos1, pos2);
        }
        printf("Case #%d: %d\n", i + 1, sum);
    }
    fclose(stdin);
    fclose(stdout);
}
