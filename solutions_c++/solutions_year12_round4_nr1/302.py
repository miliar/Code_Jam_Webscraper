#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int N = 20000;
int d[N], l[N], s[N];

int main()
{
    int cases;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; ++T) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d%d", &d[i], &l[i]);
	l[n] = 0;
	scanf("%d", &d[n]);
        s[0] = d[0];
        for (int i = 1; i <= n; ++i) {
            s[i] = -1;
            for (int j = i; --j >= 0; )
                if (d[i]-d[j] >= 0 && d[i]-d[j] <= s[j])
                    s[i] = max(s[i], min(d[i]-d[j], l[i]));
        }
        printf("Case #%d: %s\n", T, s[n] >= 0 ? "YES" : "NO");
    }
}
