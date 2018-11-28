#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
using namespace std;
typedef long long LL;



int main()
{
    int T, C;
    scanf("%d", &T);

    for (int cs = 1; cs <= T; cs++) {
        scanf("%d", &C);

        map<int, int> mp;
        set<int> two;
        for (int i = 0; i < C; i++) {
            int P, V;
            scanf("%d %d", &P, &V);
            mp[P] = V;
            if (V >= 2)
                two.insert(P);
        }

        LL res = 0;
        while (two.size() != 0) {
            int x = *two.begin();
            int y = mp[x];
            int d = y / 2;
            if ((mp[x-1] += d) >= 2) two.insert(x-1);
            if ((mp[x+1] += d) >= 2) two.insert(x+1);
            mp[x] -= 2*d;
            two.erase(x);
            res += d;
        }

        printf("Case #%d: %lld\n", cs, res);
    }
}
