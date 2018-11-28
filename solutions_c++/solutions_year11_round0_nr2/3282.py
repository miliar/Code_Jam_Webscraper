#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))
char map[26][26];
bool clr[26][26];
int c, d, n;
char str[128];
char now[128];
int cnt[26];
int m = 0;
int main() {
    int e = 0, T;
    scanf("%d",&T);
    while(T--) {
        scanf(" %d",&c);
        SET(map, 0);
        SET(clr, 0);
        FOR(i,0,c) {
            char dat[4];
            scanf("%s",dat);
            map[dat[0]-'A'][dat[1]-'A'] = dat[2];
            map[dat[1]-'A'][dat[0]-'A'] = dat[2];
        }
        scanf(" %d",&d);
        FOR(i,0,d) {
            char dat[4];
            scanf("%s",dat);
            clr[dat[0]-'A'][dat[1]-'A'] = 1;
            clr[dat[1]-'A'][dat[0]-'A'] = 1;
        }
        scanf(" %d",&n);
        scanf("%s", str);
        SET(cnt, 0);
        m = 0;
        FOR(i,0,n) {
            now[m++] = str[i];
            cnt[now[m-1]-'A']++;
            while(m>=2) {
                if(map[now[m-1]-'A'][now[m-2]-'A'] > 0) {
                    cnt[now[m-1]-'A']--;
                    cnt[now[m-2]-'A']--;
                    now[m-2] = map[now[m-1]-'A'][now[m-2]-'A'];
                    cnt[now[m-2]-'A']++;
                    m--;
                    continue;
                }
               FOR(x,0,26)
                if(cnt[x])
                    FOR(y,x,26)
                    if(cnt[y])
                        if(clr[x][y]) {
                            m = 0;
                            SET(cnt, 0);
                            goto p1;
                        }
                break;
            }
            p1:;
        }
        printf("Case #%d: ",++e);
        printf("[");
        FOR(i,0,m) {
            if(i+1<m)
                printf("%c, ",now[i]);
            if(i+1==m) printf("%c",now[i]);
        }
        printf("]\n");
    }
    return 0;
}
