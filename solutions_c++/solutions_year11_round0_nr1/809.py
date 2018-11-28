#include <cstdio>

const int N = 110;

int n;
int robot[N];
int pos[N];
int togo[N][2];

int main()
{
    char ch;
    int t, cas = 0;;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &t);
    while (t--){
        scanf("%d", &n);
        for (int i = 0; i < n; ++i){
            scanf(" %c %d", &ch, &pos[i]);
            robot[i] = ch == 'O' ? 0 : 1;
        }
        togo[n-1][0] = togo[n-1][1] = pos[n-1];
        for (int i = n-2; i >= 0; --i){
            togo[i][0] = togo[i+1][0];
            togo[i][1] = togo[i+1][1];
            togo[i][robot[i]] = pos[i];
        }
        int ans = 0, p[2];
        p[0] = p[1] = 1;
        for (int i = 0; i < n; ++i){
            while (p[robot[i]] != pos[i]){
                if (p[0] < togo[i][0]) ++p[0];
                if (p[0] > togo[i][0]) --p[0];
                if (p[1] < togo[i][1]) ++p[1];
                if (p[1] > togo[i][1]) --p[1];
                ++ans;
            }
            ++ans;
            if (p[0] < togo[i][0]) ++p[0];
            if (p[0] > togo[i][0]) --p[0];
            if (p[1] < togo[i][1]) ++p[1];
            if (p[1] > togo[i][1]) --p[1];
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
