#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <limits>

using namespace std;

char w[5000][16];
char p[1024];
int main()
{
    int L, D, N;
    scanf("%d%d%d", &L, &D, &N);
    for (int i = 0; i < D; ++i)
        scanf("%s", w[i]);

    for (int i = 0; i < N; ++i)
    {
        scanf("%s", p);
        int s = strlen(p), cnt = 0;
        for (int j = 0; j < D; ++j)
        {
            bool ok = true;
            int r = 0;
            for (int k = 0; ok && r < s && k < L; ++k)
            {
                if (isalpha(p[r]))
                {
                    if (w[j][k] != p[r])
                    {
                        ok = false;
                        break;
                    }
                }
                else
                {
                    while (w[j][k] != p[r])
                        if (p[++r] == ')')
                        {
                            ok = false;
                            break;
                        }
                    while (ok && p[r] != ')')
                        ++r;
                }
                ++r;
            }
            if (ok) ++cnt;
        }
        printf("Case #%d: %d\n", i + 1, cnt);
    }
    return 0;
}