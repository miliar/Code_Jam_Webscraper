#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

typedef long long int64;

struct tree_t
{
    int64 x, y;
} trees[100000];

int64 n_trees;

int64 n_mod[3][3];

int64 ans;

int64 stack[4];

int x_mod;
int y_mod;

void recurse(int depth)
{
    if (depth == 3) {
        if ((x_mod % 3) == 0 && (y_mod % 3) == 0)
            ans += stack[depth];
        return;
    }

    for (int x = 0; x < 3; x++)
    for (int y = 0; y < 3; y++) {
        if (n_mod[x][y] != 0) {
            stack[depth + 1] = stack[depth] * n_mod[x][y];

            n_mod[x][y]--;
            x_mod += x;
            y_mod += y;
            recurse(depth+1);
            n_mod[x][y]++;
            x_mod -= x;
            y_mod -= y;
        }
    }
}

void solve()
{
    int64 A, B, C, D, cx, cy, M;
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n_trees, &A, &B, &C, &D, &cx, &cy, &M);
    
    for (int i = 0; i < n_trees; i++) {
        trees[i].x = cx;
        trees[i].y = cy;

        cx = (A * cx + B) % M;
        cy = (C * cy + D) % M;
    }

    for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
        n_mod[i][j] = 0;

    for (int i = 0; i < n_trees; i++)
        n_mod[trees[i].x % 3][trees[i].y % 3]++;

    /*
    printf("\n");
    for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
        printf("%d %d %d\n", i, j, n_mod[i][j]);
    */
    
    x_mod = 0;
    y_mod = 0;
    stack[0] = 1;
    ans = 0;
    recurse(0);

    ans /= 6;

    /*
    int64 check_ans = 0;
    for (int i = 0; i < n_trees; i++)
    for (int j = i + 1; j < n_trees; j++)
    for (int k = j + 1; k < n_trees; k++) {
        if (((trees[i].x + trees[j].x + trees[k].x)) % 3 == 0 &&
            ((trees[i].y + trees[j].y + trees[k].y) % 3) == 0)
            check_ans++;
    }
    */

    printf("%lld", ans);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

