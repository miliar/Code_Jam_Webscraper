# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <ctime>
# include <cmath>
# include <iostream>
# include <algorithm>
# include <vector>
# include <string>
# include <set>
# include <map>
# include <list>
# include <queue>
using namespace std;

int main()
{
    int t, n, k;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        scanf("%d%d", &n, &k);
        printf("Case #%d: %s\n", i, (k & ((1 << n) - 1)) == ((1 << n) - 1) ? "ON" : "OFF");
    }
    return 0;
}
