#include<cstdio>
#include<cstdlib>
#include<cstring>

#include<algorithm>
#include<bitset>
#include<deque>
#include<functional>
#include<iostream>
#include<iterator>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<utility>
#include<vector>

const int N = 1000;

int main()
{
int numTestCases;
int n, a[N], b[N], cross;

scanf("%d", &numTestCases);
for (int id = 1; id <= numTestCases; ++id)
{
    printf("Case #%d: ", id);
    scanf("%d", &n); // number of wires
    for (int i = 0; i < n; ++i)
    {
        scanf("%d%d", &a[i], &b[i]); // left, right
    }

    cross = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            if ((a[i] - a[j]) * (b[i] - b[j]) < 0) ++cross;
        }
    }
    printf("%d\n", cross);
}

return 0;
}

