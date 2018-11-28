#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
using namespace std;

int main()
{
//    freopen("a2.in","r",stdin);
//    freopen("a2.ou","w",stdout);
    int T;
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        printf("Case #%d: ", it);
        int n,k;
        scanf("%d %d", &n, &k);
        k++;
        k %= (1 << n);
        if (k) printf("OFF\n"); else printf("ON\n");
    };
};
