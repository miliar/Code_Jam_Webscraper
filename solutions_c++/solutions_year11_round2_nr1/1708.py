#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
char map[110][110];
double a[110], b[110], c[110], t[110], p[110][110];
int    win[110], cnt[110];


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, n, i, j, ct = 1;
    //int wi, cnt;
    double tmp;
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        for (i = 0; i < n; ++i)
            scanf("%s",map[i]);
        
        for (i = 0; i < n; ++i) {
            cnt[i] = 0;
            win[i] = 0;
            for (j = 0; j < n; ++j) {
                if (map[i][j] == '1' || map[i][j] == '0') {
                    cnt[i]++;
                    if (map[i][j] == '1') {
                        win[i]++;
                    }
                }
            }
            a[i] = (win[i] * 1.0) / cnt[i];
        }
        
        for (i = 0; i < n; ++i) {
            //cnt[i] = 0;
            //win[i] = 0;
            tmp = 0.0;
            for (j = 0; j < n; ++j) {
                if (map[i][j] == '1' || map[i][j] == '0') {
                    //cnt[i]++;
                    if (map[i][j] == '1') {
                       tmp += (win[j] * 1.0) / (cnt[j] - 1.0);  
                    }
                    else {
                       tmp += (win[j] - 1.0) / (cnt[j] - 1.0);  
                    }
                }
            }
            //printf("%.3lf %d\n", tmp, cnt[i]);
            b[i] = tmp / cnt[i];
        }
        
        for (i = 0; i < n; ++i) {
            tmp = 0.0;
            for (j = 0; j < n; ++j) {
                if (map[i][j] == '1' || map[i][j] == '0') {
                    tmp += b[j];
                }
            }
            c[i] = (tmp * 1.0) / cnt[i];
        }
        
        
        
        printf("Case #%d:\n",ct++);
        for (i = 0; i < n; ++i) {
             //printf("%.3lf %.3lf %.3lf\n",a[i],b[i],c[i]);
             printf("%.8lf\n",0.25*a[i] + 0.5*b[i] + 0.25*c[i]);
        }
    }
    return 0;
}
