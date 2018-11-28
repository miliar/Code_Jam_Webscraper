#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>

#define fi first
#define se second
#define mp make_pair

using namespace std;

pair<int, int> s[10010];
int N, D;

map< pair<int, int >, char > m;

char solve(int i, int height) {
    int j;
    char ans;

    if ( m.find( mp(i, height) ) != m.end() ) {
        return m[ mp(i, height) ];
    }

    if (s[i].fi + height >= D ) {
        m[ mp(i, height) ] = 'Y';
        return 'Y';
    }

    for (j=i+1; j<=N; ++j) {
        if ( s[i].fi + height >= s[j].fi ) {
            if ( solve(j, min(s[j].se, s[j].fi - s[i].fi)) == 'Y' ) {
                m[ mp(i, height) ] = 'Y';
                return 'Y';
            }
        }
        else break;
    }

    m[ mp(i, height) ] = 'N';
    return 'N';
}

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int i, j, t, T;

    scanf("%d", &T);

    for(t=1; t<=T; ++t) {
        m.clear();
        scanf("%d", &N);

        for (i=0; i<N; ++i) {
            scanf("%d %d", &s[i].fi, &s[i].se);
        }
        scanf("%d", &D);


        printf("Case #%d: ", t);
        if ( solve( 0, s[0].fi ) == 'Y' ) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }

    return 0;
}
