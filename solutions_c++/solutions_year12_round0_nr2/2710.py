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
 
using namespace std;

int T, N, S, P, t;
int mx[31][2];

void myinit()
{
    mx[0][0] = mx[0][1] = 0;
    for(int i = 1;i <= 30;i++)
    {
        mx[i][0] = (i - 1) / 3 + 1;
        mx[i][1] = (i - 2) / 3 + 2;
    }
}
//#define home
//#define small
//#define large
int main() 
{
#ifdef home
    freopen("1.txt", "r", stdin);
#endif
#ifdef small
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-out-small", "w", stdout);
#endif
#ifdef large
    freopen("B-large-attepmt0.in", "r", stdin);
    freopen("B-out-large", "w", stdout);
#endif

    myinit();
    int result = 0;

    scanf("%d", &T);
    for(int _case = 1;_case <= T;_case++)
    {
        result = 0;
        scanf("%d %d %d", &N, &S, &P);
        for(int i = 0;i < N;i++)
        {
            scanf("%d", &t);
            if(mx[t][0] >= P) result++;
            else if(mx[t][1] >= P && S)
            {
                S--;
                result++;
            }
        }
        printf("Case #%d: %d\n", _case, result);
    }
    return 0;
}
