#include<stdio.h>
#include<string>

int na, nb, T;
int fa[1500], fb[1500];
char start[20], end[20];
int encode(char *s) {
    return ((s[0] - '0') * 10 + (s[1] - '0')) * 60
            + (s[3] - '0') * 10 + (s[4] - '0');
}    
inline int Min(int a, int b) {
    return a < b ? a : b;
}    
int main() {
    int case_n;
    scanf("%d", &case_n);
    int t_c;
    for (t_c = 1; t_c <= case_n; t_c++) {
        scanf("%d%d%d", &T, &na, &nb);
        memset(fa, 0, sizeof(fa));
        memset(fb, 0, sizeof(fb));
        int idx;
        for (idx = 0; idx < na; idx++) {
            scanf("%s%s", start, end);
            int s = encode(start);
            int e = encode(end);
            fa[s]--;
            fb[e + T]++;
        }    
        for (idx = 0; idx < nb; idx++) {
            scanf("%s%s", start, end);
            int s = encode(start);
            int e = encode(end);
            fb[s]--;
            fa[e + T]++;
        }
        int sa = 0;
        int sb = 0;
        int ans_a = 0, ans_b = 0;
        for (idx = 0; idx < 1440; idx++) {
            sa += fa[idx];
            ans_a = Min(ans_a, sa);
            sb += fb[idx];
            ans_b = Min(ans_b, sb);
        }
        printf("Case #%d: %d %d\n", t_c, -ans_a, -ans_b);
    }    
    return 0;   
}   
 
