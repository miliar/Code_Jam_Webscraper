# include <iostream>
# include <cstring>
using namespace std;

int main()
{
    int ll, d, n, i, j, k, t, m, l;
    char words[5000][16], p[10000];
    bool v[5000], can[5000];
    scanf("%d%d%d", &ll, &d, &n);
    for (i=0; i<d; i++) {
        scanf("%s", words[i]);
    }
    for (t=1; t<=n; t++) {
        scanf("%s", p);
        m=strlen(p);
        memset(v, 0, sizeof v);
        k=0;
        for (i=0; i<ll; i++) {
            memset(can, 0, sizeof can);
            if (p[k]=='(') {
                for (j=k+1; p[j]!=')'; j++) {
                    for (l=0; l<d; l++) {
                        if (!v[l]) {
                            can[l]=can[l]||(p[j]==words[l][i]);
                        }
                    }
                }
                k=j+1;
                for (l=0; l<d; l++) {
                    v[l]=v[l]||!(can[l]);
                }
            }
            else {
                for (l=0; l<d; l++) {
                    if (!v[l]) {
                        can[l]=can[l]||(p[k]==words[l][i]);
                    }
                }
                k++;
                for (l=0; l<d; l++) {
                    v[l]=v[l]||!(can[l]);
                }
            }
        }
        int ans=0;
        for (l=0; l<d; l++) {
            if (!v[l]) {
                ans++;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
