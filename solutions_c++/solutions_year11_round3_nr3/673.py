#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

void solve()
{
    int caseNum;
    scanf("%d", &caseNum);

    for (int caseId = 1; caseId <= caseNum; caseId++)
    {
        printf("Case #%d:", caseId);

        int n, low, high;
        scanf("%d %d %d", &n, &low, &high);

        vector<int> vec(n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &vec[i]);
        }

        bool bOK = true;
        for (int k = low; k <= high; k++)
        {
            bOK = true;
            for (int i = 0; i < n; i++)
            {
                if (k % vec[i] != 0 && \
                    vec[i] % k != 0)
                {
                    bOK = false;
                    break;
                }
            }

            if (bOK)
            {
                printf(" %d\n", k);
                break;
            }
        }

        if (!bOK)
        {
            printf(" NO\n");
        }
    }
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    solve();

    return 0;
}