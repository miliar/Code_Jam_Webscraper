#include <iostream>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
using namespace std;

typedef long long int64; // 2 ^ 63 - 1 = 9223372036854775807.
typedef unsigned long long uint64; // 2 ^ 64 - 1 = 18446744073709551615.
#define mem(a, b) memset(a, b, sizeof(a))
#define Sqr(x) ((x) * (x))
template <class T>
inline T Max(T a, T b) { if (a < b) a = b; return a; }
template <class T>
inline T Min(T a, T b) { if (a > b) a = b; return a; }
template <class T>
inline void Swap(T & a, T & b) { T t = a; a = b; b = t; }
inline int64 mod(int64 x, int64 y) { return x - floor(1.0 * x / y) * y; }

const int maxn = 105;
const int maxm = 1 << 12;
const double EPS = 1e-10;
const double PI = acos(-1.0);
const int INT_INF = INT_MAX / 2;
const int64 INT64_INF = 1LL << 61;

const int direction[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

struct node
{
    int x, y;
};

int n, m;
int row, column;
int h[maxn][maxn];
node Stack[maxn * maxn];
int top;
int ans[maxn][maxn];

inline void Push(int x, int y) { Stack[top].x = x, Stack[top++].y = y; }
inline node Top(void) { return Stack[top - 1]; }
inline void Pop(void) { top--; }

void Debug(void)
{
    int i, j;
}

void Init(void)
{
    int i, j;
    mem(ans, 0); m = 1;
}


void DFS(int sx, int sy)
{
    int i, j;
    int d, min_h;
    int x, y, xx, yy, tx, ty;
    int num;
    node tn;
    Push(sx, sy);
    while (top > 0)
    {
        tn = Top();
        x = tn.x, y = tn.y;
        min_h = INT_INF;
        for (d = 0; d < 4; d++)
        {
            xx = x + direction[d][0], yy = y + direction[d][1];
            if (xx >= 0 && xx < row && yy >= 0 && yy < column && min_h > h[xx][yy])
            {
                min_h = h[xx][yy], tx = xx, ty = yy;
            }
        }
        if (min_h >= h[x][y])
        { // ËµÃ÷ÊÇsink.
            if (ans[x][y] == 0) num = m++;
            else num = ans[x][y];
            break;
        }
        Push(tx, ty);
    }
    while (top > 0)
    {
        tn = Top(); Pop();
        x = tn.x, y = tn.y;
        ans[x][y] = num;
    }
}

void Solve(void)
{
    int i, j;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < column; j++)
        {
            if (ans[i][j] == 0)
            {
                DFS(i, j);
            }
        }
    }
}

int main(void)
{
    freopen("Input.txt", "r", stdin);
    freopen("Output.txt", "w", stdout);
    int i, j;
    int cases;
    int case_num(0);
    scanf("%d", &cases);
    while (cases--)
    {
        scanf("%d %d", &row, &column);
        for (i = 0; i < row; i++)
        {
            for (j = 0; j < column; j++)
            {
                scanf("%d", &h[i][j]);
            }
        }
        Init();
        Solve();
        printf("Case #%d: \n", ++case_num);
        for (i = 0; i < row; i++)
        {
            for (j = 0; j < column - 1; j++)
            {
                printf("%c ", ans[i][j] + 'a' - 1);
            }
            printf("%c\n", ans[i][j] + 'a' - 1);
        }
//        Debug();
    }
    return 0;
}
