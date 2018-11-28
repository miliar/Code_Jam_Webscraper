#include <iostream>
#include <vector>

using namespace std;

const int mod = 10000019;

int k, n, m;

int qs, qf;

bool v[5];

struct pos
{
    int x[5];
    int y[5];
    int d;

    int dfs(int i)
    {
        if (v[i])
            return 0;

        v[i] = true;
        int res = 1;
        for (int j=0; j<k; j++)
            if (abs(x[i] - x[j]) + abs(y[i] - y[j]) == 1)
                res += dfs(j);
        return res;
    }

    bool danger()
    {
        memset(v, 0, sizeof(v));
        return dfs(0) < k;
    }

    void sort()
    {
        for (int i=0; i<k; i++)
            for (int j=i+1; j<k; j++)
                if (x[i] > x[j] || x[i] == x[j] && y[i] > y[j])
                {
                    swap(x[i], x[j]);
                    swap(y[i], y[j]);
                }
    }

    int hash()
    {
        int res = 0;
        for (int i=0; i<k; i++)
            res = (res + x[i]) * 111 % mod;
        for (int i=0; i<k; i++)
            res = (res + y[i]) * 111 % mod;
        return res;
    }

    bool operator==(const pos &other) const
    {
        for (int i=0; i<k; i++)
            if (x[i] != other.x[i] || y[i] != other.y[i])
                return false;
        return true;
    }
} q[1<<25], goal;

vector<int> hashes[mod];

int ans;

void doit()
{
    q[qf+1] = q[qf];
    q[qf].sort();
    int x = q[qf].hash();
    
    for (int i=0; i<hashes[x].size(); i++)
        if (q[hashes[x][i]] == q[qf])
        {
            q[qf] = q[qf+1];
            return;
        }

    if (q[qf] == goal)
        ans = q[qf].d;

    hashes[x].push_back(qf);
    qf++;    
}

char a[64][64];

bool ok(int i, int j)
{
    if (!(0 <= i && i < n && 0 <= j && j < m && a[i][j] != '#'))
        return false;
    for (int t=0; t<k; t++)
        if (q[qs].x[t] == i && q[qs].y[t] == j)
            return false;
    return true;
}

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        for (int i=0; i<mod; i++)
            hashes[i].clear();

        cin >> n >> m;

        for (int i=0; i<n; i++)
            cin >> a[i];

        qs = qf = 0;

        ans = -1;

        k = 0;
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if (a[i][j] == 'x' || a[i][j] == 'w')
                {
                    goal.x[k] = i;
                    goal.y[k] = j;
                    k++;
                }
        goal.sort();

        k = 0;
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if (a[i][j] == 'o' || a[i][j] == 'w')
                {
                    q[qf].x[k] = i;
                    q[qf].y[k] = j;
                    k++;
                }
        doit();

        for (; qs < qf && ans < 0; qs++)
        {
            pos cur = q[qs];
            q[qf] = cur;
            q[qf].d++;

            bool f = q[qs].danger();

            for (int i=0; i<k; i++)
                for (int dx = 1, dy = 0; dy < 2; dx--, dy++)
                    if (ok(q[qf].x[i] + dx, q[qf].y[i] + dy) && ok(q[qf].x[i] - dx, q[qf].y[i] - dy))
                    {
                        q[qf].x[i] += dx;
                        q[qf].y[i] += dy;
                        if (!f || !q[qf].danger())
                            doit();
                        q[qf].x[i] -= dx;
                        q[qf].y[i] -= dy;

                        q[qf].x[i] -= dx;
                        q[qf].y[i] -= dy;
                        if (!f || !q[qf].danger())
                            doit();
                        q[qf].x[i] += dx;
                        q[qf].y[i] += dy;
                    }
        }

        cout << "Case #" << tt << ": " << ans << endl;
    }

    return 0;
}
