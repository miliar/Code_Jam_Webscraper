#include <cstdio>
#include <cstring>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

typedef long long LL;

const int MAXN = 10000000;

int stat[11][MAXN];

LL convert(int n, int b)
{
    LL ret = 0, base = 1;
    while (n > 0)
    {
        ret += base * (n % b);
        base *= 10;
        n /= b;
    }
    return ret;
}

int next(int n, int b)
{
    LL m = convert(n, b);
    int ret = 0;
    while (m > 0)
    {
        ret += (m % 10) * (m % 10);
        m /= 10;
    }
    return ret;
}

inline void check(int n, int b)
{
    set <int> st;
    st.insert(n);
    while (true)
    {
        n = next(n, b);
        if (st.find(n) != st.end() || n >= MAXN)
        {
            for (set <int>::iterator it = st.begin(); it != st.end(); it++)
                stat[b][*it] = 2;
        }
        if (stat[b][n] != 0)
        {
            for (set <int>::iterator it = st.begin(); it != st.end(); it++)
                stat[b][*it] = stat[b][n];
            return;
        }
        st.insert(n);
    }
}

void Init()
{
    memset(stat, 0, sizeof(stat));
    for (int i = 3; i <= 10; i++)
    {
//printf("i: %d\n", i);
        stat[i][1] = 1;
        for (int j = 2; j < MAXN; j++)
            check(j, i);
    }
//puts("Done");
/*    for (int i = 3; i <= 10; i++)
    {
        printf("%d:", i);
        for (int j = 1; j < 200; j++)
            if (stat[i][j] == 1)
                printf(" %d", j);
        putchar('\n');
    }*/
}

int main()
{
    Init();
    int T;
    scanf("%d ", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        char str[1000];
        gets(str);
        string s = string(str);
        istringstream ist(s);
        int n;
        vector <int> v;
        while (ist >> n)
        {
            v.push_back(n);
        }
        bool fl = false;
        for (int i = 2; i < MAXN; i++)
        {
            bool flag = true;
            for (size_t j = 0; j < v.size(); j++)
                if (v[j] != 2 && stat[v[j]][i] != 1)
                {
                    flag = false;
                    break;
                }
            if (flag)
            {
                printf("Case #%d: %d\n", cas, i);
                fl = true;
                break;
            }
        }
        if (!fl)
            printf("Case #%d: 11814485\n", cas);
    }
    return 0;
}
