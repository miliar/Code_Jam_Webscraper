#include <cstdio>
#include <cstdlib>

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    char pr, r, s[5];
    int  pt, p, T, n, i, cnt, ct = 1, t1, t2, pt1, pt2;
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        cnt = 0;
        t1 = t2 = 1;
        pt1 = pt2 = 0;
        for (i = 0; i < n; ++i) {
            scanf("%s %d",&s, &p); 
            r = s[0];
            if ( (r == 'O' && pr == 'O') || (i == 0 && r == 'O')) {
                pt  = abs(p - t1) + 1 ;
                cnt += pt;
                t1  = p;
                pt1 += pt;
                //printf("%d\n",pt);
            } 
            else if ( (r == 'B' && pr == 'B') || (i == 0 && r == 'B')){
                pt = abs(p - t2) + 1;
                cnt += pt;
                t2  = p;   
                pt2 += pt;
                //printf("%d\n",pt);         
            }
            else if ( (r == 'O' && pr == 'B') ) {
                pt = pt2 > abs(p - t1) ? 1 : (abs(p - t1) - pt2) + 1;
                cnt += pt;
                t1  = p;
                pt1 = pt;
                //printf("%d\n",pt);
            } 
            else if ( (r == 'B' && pr == 'O') ) {
                pt = pt1 > abs(p - t2) ? 1 : (abs(p - t2) - pt1) + 1;
                cnt += pt;
                t2  = p;
                pt2 = pt;
                //printf("%d\n",pt);
            } 
            pr = r;
        }
        printf("Case #%d: %d\n",ct++, cnt);
    }
    return 0;
}
