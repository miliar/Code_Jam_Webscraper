#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 2222;

int n, m, k;
vector <int> a[MAXN];
vector <int> r;
int u[MAXN], v[MAXN];
bool f[MAXN][MAXN];
int x[MAXN];

int add(const vector <int> &r)
{
    a[k] = r;
    memset(f[k], false, sizeof(f[k]));
    for (int i = 0; i < r.size(); i++)
        f[k][r[i]] = true;
    k++;
    return 0;
}


bool run(int c)
{
    for (int i = 0; i <= n; i++)
        x[i] = 0;

    do
    {
        for (int i = 0; i <= n; i++)
        {
            if (x[i] == c - 1)
            {
                x[i] = 0;
            }
            else
            {
                x[i]++;
                break;
            }
        }
        if (x[n]) break;

        for (int i = 0; i < c; i++)
            u[i] = -1;

        bool f = true;
        for (int i = 0; i < k && f; i++)
        {
            for (int j = 0; j < a[i].size(); j++)
                u[x[a[i][j]]] = i;

            for (int j = 0; j < c; j++)
                if (u[j] != i)
                {
                    f = false;
                    break;
                }
        }


        if (f) return true;
    } while (true);
    return false;
}

int main()
{
    freopen("in", "rt", stdin);
    freopen("out", "wt", stdout);

    int ctest = 0;
    scanf("%d", &ctest);
    for (int itest = 1; itest <= ctest; itest++)
    {
        scanf("%d %d", &n, &m);
        r.resize(n);
        for (int i = 0; i < n; i++)
            r[i] = i;

        k = 0;
        add(r);


        for (int i = 0; i < m; i++)
            scanf("%d", &u[i]);
        for (int i = 0; i < m; i++)
            scanf("%d", &v[i]);

        while (m--)
        {
            int x, y;
            x = u[m] - 1;
            y = v[m] - 1;

            for (int i = 0; i < k; i++)
            {
                if (f[i][x] && f[i][y])
                {
                    r = a[i];
                    k--;
                    a[i] = a[k];
                    memmove(f[i], f[k], sizeof(f[k]));
                    break;
                }
            }

            vector <int> r1, r2;
            r1.clear();
            r2.clear();

            int i = 0;
            while (r[i] != x) i = (i + 1) % r.size();


            while (r[i] != y)
            {
                r1.push_back(r[i]);
                i = (i + 1) % r.size();
            }
            r1.push_back(r[i]);

            while (r[i] != x)
            {
                r2.push_back(r[i]);
                i = (i + 1) % r.size();
            }
            r2.push_back(r[i]);

/*
            printf("%d %d\n", x, y);
            for (int i = 0; i < r.size(); i++) printf("%d ", r[i]); printf("\n");
            printf("\t"); for (int i = 0; i < r1.size(); i++) printf("%d ", r1[i]); printf("\n");
            printf("\t"); for (int i = 0; i < r2.size(); i++) printf("%d ", r2[i]); printf("\n");
            printf("\n");
//*/
            add(r1);
            add(r2);
        }

        int ans = 2;
        while (run(ans))
            ans++;

        run(ans - 1);
        
        printf("Case #%d: ", itest);
        printf("%d\n", ans - 1);
        for (int i = 0; i < n; i++)
        {
            if (i) printf(" ");
            printf("%d", x[i] + 1);
        }

        printf("\n");
    }


    return 0;
}