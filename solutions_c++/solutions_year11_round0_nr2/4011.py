#include <cstdio>
#include <cstring>

char comb[50][4];
char dest[50][4];
char v[200], p[200];

int us[200];

int main() {
    int c,d,n;
    int nt;

    scanf(" %d",&nt);
    for (int ct=1; ct<=nt; ct++) {
        scanf(" %d",&c);
        for (int i=0; i<c; i++)
            scanf(" %s", comb[i]);

        scanf(" %d",&d);
        for (int i=0; i<d; i++)
            scanf(" %s", dest[i]);

        scanf(" %d", &n);
        scanf(" %s", v);

        memset(us,0,sizeof(us));
        int qe=0;
        for (int i=0; i<n; i++) {
            bool done = false;
            if (qe) {
                for (int j=0; j<c; j++)
                    if ((comb[j][0] == v[i] && comb[j][1] == p[qe-1]) ||
                      (comb[j][0] == p[qe-1] && comb[j][1] == v[i])) {
                        us[p[qe-1]]--;
                        us[comb[j][2]]++;
                        p[qe-1] = comb[j][2];
                        done = true;
                        break;
                    }
            }
            if (done) continue;

            for (int j=0; j<d; j++)
                if ((dest[j][0] == v[i] && us[dest[j][1]])
                ||  (us[dest[j][0]] && dest[j][1] == v[i])) {
                    memset(us, 0, sizeof(us));
                    qe = 0;
                    done = true;
                    break;
                }
            if (done) continue;

            us[v[i]]++;
            p[qe++] = v[i];
        }

        printf("Case #%d: [", ct);
        for (int i=0; i<qe; i++) {
            printf("%c", p[i]);
            if (i<qe-1) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
