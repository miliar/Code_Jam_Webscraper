#include <cstdio>

const int C = 40;
const int D = 40;
const int N = 120;

char comb[26][26];
bool oppo[26][26];

int c, d, n;
char str[N];
char stack[N];
int top;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--){
        for (int i = 0; i < 26; ++i)
            for (int j = 0; j < 26; ++j)
                comb[i][j] = 0, oppo[i][j] = 0;
        scanf("%d", &c);
        while (c--){
            scanf("%s", str);
            comb[str[0]-'A'][str[1]-'A'] = comb[str[1]-'A'][str[0]-'A'] = str[2];
        }
        scanf("%d", &d);
        while (d--){
            scanf("%s", str);
            oppo[str[0]-'A'][str[1]-'A'] = oppo[str[1]-'A'][str[0]-'A'] = 1;
        }
        scanf("%d", &n);
        scanf("%s", str);
        top = 0;
        for (int i = 0; i < n; ++i){
            if (top && comb[str[i]-'A'][stack[top]-'A'] != 0) stack[top] = comb[str[i]-'A'][stack[top]-'A'];
            else{
                bool clear = 0;
                for (int k = 1; k <= top; ++k) if (oppo[stack[k]-'A'][str[i]-'A']) clear = 1;
                if (clear) top = 0;
                else stack[++top] = str[i];
            }
        }
        printf("Case #%d: [", ++cas);
        for (int i = 1; i <= top; ++i){
            if (i != 1) printf(", ");
            putchar(stack[i]);
        }
        puts("]");
    }
    return 0;
}
