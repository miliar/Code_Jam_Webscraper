#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

const int MAXN = 128;
const int INF = 2000000000;
int p[MAXN];
char c[MAXN];
int s[MAXN][MAXN][MAXN];
int q[MAXN*MAXN*MAXN][3];

int main() {
    // freopen("A-small.in","r",stdin);
    // freopen("A-small.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, n, i, qh, qt, ca;
    char buf[4];
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        int maxp = 0;
        scanf("%d",&n);
        for (i = 0 ; i < n ; i++) {
            scanf("%s%d",buf,&p[i]);
            if (p[i] > maxp) maxp = p[i];
            c[i] = buf[0];
        }
        int ans = INF;
        memset(s, 0x7f, sizeof(s));
        s[1][1][0] = 0;
        qh = 0; qt = 1;
        q[0][0] = 1; q[0][1] = 1; q[0][2] = 0;
        for ( ; qh < qt ; ++qh) {
            int po = q[qh][0];
            int pb = q[qh][1];
            int pbut = q[qh][2];
            int step = s[po][pb][pbut];
            //printf("po:%d pb:%d pbut:%d step:%d\n",po,pb,pbut,step);
            if (pbut == n) {ans = step; break;}

            int mo, mb;
            for (mo = -1 ; mo <= 2 ; ++mo) {
                for (mb = -1 ; mb <= 2 ; ++mb) {
                    int ro, rb, rbut = pbut;
                    if (mo == 2 && mb == 2) continue;
                    if (mo == 2) {
                        ro = po;
                        if (c[pbut] == 'O' && p[pbut] == po) {
                            rbut = pbut + 1;
                        } else continue;
                    } else {
                        ro = po + mo;
                    }
                    if (mb == 2) {
                        rb = pb;
                        if (c[pbut] == 'B' && p[pbut] == pb) {
                            rbut = pbut + 1;
                        } else continue;
                    } else {
                        rb = pb + mb;
                    }
                    if (ro >= 1 && ro <= maxp &&
                        rb >= 1 && rb <= maxp &&
                        s[ro][rb][rbut] >= INF)
                    {
                        q[qt][0] = ro;
                        q[qt][1] = rb;
                        q[qt][2] = rbut;
                        s[ro][rb][rbut] = step + 1;
                        ++qt;
                    }
                }
            }
            /*
            // press o
            if (c[pbut] == 'O' && p[pbut] == po && s[po][pb][pbut+1] >= INF) {
                q[qt][0] = po;
                q[qt][1] = pb;
                q[qt][2] = pbut + 1;
                s[po][pb][pbut+1] = step + 1;
                ++qt;
            }
            // press b
            if (c[pbut] == 'B' && p[pbut] == pb && s[po][pb][pbut+1] >= INF) {
                q[qt][0] = po;
                q[qt][1] = pb;
                q[qt][2] = pbut + 1;
                s[po][pb][pbut+1] = step + 1;
                ++qt;
            }
            */
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
