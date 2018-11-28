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
#include <set>
 
using namespace std;

int A, B, T;
int result;
int s[100], M, toadd;
inline int cal(int a, int b)
{
    M = 1;
    int i;
    set<int> Set;
    for(i = 10;a / i > 0 ;i*=10)
        s[M++] = a % i;       

    for(int j = 1, k = 10;j < M;j++, k *= 10)
    {
        i /= 10;
        toadd = s[j] * i + a / k;
        if(toadd > a && toadd <= b) 
            Set.insert(toadd);
    }
    return Set.size();

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
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-out-small", "w", stdout);
#endif
#ifdef large
    freopen("C-large.in", "r", stdin);
    freopen("C-out-large", "w", stdout);
#endif
    scanf("%d", &T);

    for(int _case = 1;_case <= T;_case++)
    {
        result = 0;
        scanf("%d %d", &A, &B);
        for(int i = A;i <= B;i++)
            result += cal(i,B);

        printf("Case #%d: %d\n", _case, result);
    }
    return 0;
}
