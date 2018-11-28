// vim:set ts=8 sw=4 et smarttab:
// Round 3 2012

#include <cstdio>
#include <cassert>
#include <algorithm>

int n;
bool board[6001][6001];
int sa, sb;
int visit_list[10000][2];
int nv;
int corner;
bool edge[6];
bool cycle;

const int dir[6][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {-1, -1}};

bool inside(int a, int b)
{
    if (a < 1 || b < 1)
    {
        return false;
    }
    if (a > 2 * n - 1 || b > 2 * n - 1)
    {
        return false;
    }
    if (a < b && b - a >= n)
    {
        return false;
    }
    if (a > b && a - b >= n)
    {
        return false;
    }
    return true;
}

bool iscorner(int a, int b)
{
    if (a == 1 && b == 1)
        return true;
    if (a == 2 * n - 1 && b == 2 * n - 1)
        return true;
    if (a == 1 && b == n)
        return true;
    if (a == n && b == 2 * n - 1)
        return true;
    if (a == n && b == 1)
        return true;
    if (a == 2 * n - 1 && b == n)
        return true;
    return false;
}

bool isedge(int a, int b)
{
    if (iscorner(a, b))
        return false;
    if (a == 1 || b == 1)
        return true;
    if (a == 2 * n - 1 || b == 2 * n - 1)
        return true;
    if (a < b && b - a == n - 1)
        return true;
    if (a > b && a - b == n - 1)
        return true;
    return false;
}

int edge_number(int a, int b)
{
    assert(isedge(a, b));
    if (a == 1)
        return 0;
    if (b == 1)
        return 1;
    if (a == 2 * n - 1)
        return 2;
    if (b == 2 * n - 1)
        return 3;
    if (a < b && b - a == n - 1)
        return 4;
    if (a > b && a - b == n - 1)
        return 5;
    assert(false);
    return -1;
}

void visit(int a, int b)
{
    visit_list[nv][0] = a;
    visit_list[nv][1] = b;
    ++nv;
    assert(inside(a, b));
    assert(board[a][b]);
    board[a][b] = false;
    if (isedge(a, b))
    {
        edge[edge_number(a, b)] = true;
    }
    if (iscorner(a, b))
    {
        ++corner;
    }
    for (int d = 0; d < 6; ++d)
    {
        int na, nb;
        na = a + dir[d][0];
        nb = b + dir[d][1];
        if (inside(na, nb) && board[na][nb])
        {
            visit(na, nb);
        }
    }
}

bool visit2(int a, int b, int lastd)
{
    visit_list[nv][0] = a;
    visit_list[nv][1] = b;
    ++nv;
    assert(!board[a][b]);
    board[a][b] = true;
    if (isedge(a, b) || iscorner(a, b))
    {
        return true;
    }
    for (int dd = 0; dd < 6; ++dd)
    {
        int d = (lastd + dd) % 6;
        int na, nb;
        na = a + dir[d][0];
        nb = b + dir[d][1];
        if (inside(na, nb) && !board[na][nb])
        {
            if (visit2(na, nb, d))
            {
                return true;
            }
        }
    }
    return false;
}

bool check_bridge(int a, int b)
{
    return corner >= 2;
}

bool check_fork(int a, int b)
{
    int count = 0;
    for (int i = 0; i < 6; ++i)
    {
        if (edge[i])
        {
            ++count;
        }
    }
    return count >= 3;
}

bool check_ring(int a, int b)
{
    /*
    if (!cycle)
    {
        return false;
    }
    */
    for (int d = 0; d < 6; ++d)
    {
        int na, nb;
        na = a + dir[d][0];
        nb = b + dir[d][1];
        if (inside(na, nb) && !board[na][nb])
        {
            nv = 0;
            bool temp = visit2(na, nb, 0);
            for (int i = 0; i < nv; ++i)
            {
                board[visit_list[i][0]][visit_list[i][1]] = false;
            }
            if (!temp)
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int m;
        scanf("%d%d", &n, &m);
        int i;
        bool bridge, fork, ring;
        std::fill(board[0], board[6001], false);
        for (i = 1; i <= m; ++i)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            board[a][b] = true;
            nv = 0;
            sa = a;
            sb = b;
            corner = 0;
            for (int j = 0; j < 6; ++j)
            {
                edge[j] = false;
            }
            cycle = false;
            visit(a, b);
            for (int j = 0; j < nv; ++j)
            {
                board[visit_list[j][0]][visit_list[j][1]] = true;
            }
            bridge = check_bridge(a, b);
            fork = check_fork(a, b);
            ring = check_ring(a, b);
            if (bridge || fork || ring)
            {
                break;
            }
        }
        bool flag = false;
        printf("Case #%d: ", tc);
        if (bridge)
        {
            if (!flag)
            {
                flag = true;
            }
            else
            {
                printf("-");
            }
            printf("bridge");
        }
        if (fork)
        {
            if (!flag)
            {
                flag = true;
            }
            else
            {
                printf("-");
            }
            printf("fork");
        }
        if (ring)
        {
            if (!flag)
            {
                flag = true;
            }
            else
            {
                printf("-");
            }
            printf("ring");
        }
        if (flag)
        {
            printf(" in move %d\n", i);
        }
        else
        {
            printf("none\n");
        }
        for (++i; i <= m; ++i)
        {
            int a, b;
            scanf("%d%d", &a, &b);
        }
    }
}
