#pragma warning (disable : 4786)
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

#ifdef __GNUC__
typedef long long int64;
#else //MS Visual Studio
typedef __int64 int64;
#endif

const long double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const long double PI = 2 * acos(.0);

// 1 ¡Ü L ¡Ü 1 000
int gl[1001];
int keymap[1001][10001];

int main(int argc, char * argv[])
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int N, casei = 1;
    scanf("%d", &N);

    while (N-- > 0)
    {
/*
2
3 2 6
8 2 5 2 4 9
3 9 26
1 1 1 100 100 1 1 1 1 1 1 1 1 1 1 1 1 10 11 11 11 11 1 1 1 100
*/      
        int P,K,L;
        scanf("%d%d%d", &P, &K, &L); 

        for(int i = 0; i<L; i++)
        {
            scanf("%d", &gl[i]);
        }

        sort(gl,gl+L);
        reverse(gl,gl+L);
        int j;

        for (i = 0; i<1001; i++)
            for (j = 0; j<1001; j++)
                keymap[i][j] = 0;

        int m = 0;
        bool over = false;
        for (i = 0; i<P; i++)
        {
            for (j = 0; j<K; j++)
            {
                keymap[j][i] = gl[m];
                m++;
                if (m == L)
                {
                    over = true;
                    break;
                }
            }
            if (over)
                break;
        }

        int64 res = 0;

        for (i = 0; i<P; i++)
        {
            int64 line = 0;
            for (j = 0; j<K; j++)
            {
                line += keymap[j][i];
            }
            res += line*(i+1);
        }
        
        // ...
        printf("Case #%d: %d\n", casei++ , res);
    }
    return 0;
}

