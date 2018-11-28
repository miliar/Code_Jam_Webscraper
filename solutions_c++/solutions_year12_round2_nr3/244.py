#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <set>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

int T;

int n;
int s[20];
int a[2][20];
int sz[2];
bool fnd;
int sum;
int i;

void gen() {
    if (sum == 0 && (sz[0] || sz[1])) {
        fnd = 1;
        return;
    }

    if (i == n) return;

    i++;
    gen();
    if (fnd) return;
    i--;

    a[0][sz[0]++] = s[i];
    sum += s[i];
    i++;
    gen();
    if (fnd) return;
    i--;
    sz[0]--;
    sum -= s[i];

    a[1][sz[1]++] = s[i];
    sum -= s[i];
    i++;
    gen();
    if (fnd) return;
    i--;
    sz[1]--;
    sum += s[i];

}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    forn(t, T) {
        scanf("%d", &n);
        forn(j, n) scanf("%d", &s[j]);
        sum = fnd = i = sz[0] = sz[1] = 0;
        gen();

        printf("Case #%d:\n", t + 1);

        if (!fnd) printf("Impossible\n");
        else {
            forn(q, 2){
                forn(j, sz[q]) printf("%d ", a[q][j]);
                printf("\n");
            }
        }
    }
    return 0;
}
