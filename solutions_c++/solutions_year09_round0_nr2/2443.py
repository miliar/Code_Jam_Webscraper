#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

struct Node
{
    int root;
    int rank;
    char label;
};

Node nodes[10010];

int att[128][128];

int findRoot(int idx)
{
    if (nodes[idx].root == idx)
    {
        return idx;
    }
    nodes[idx].root = findRoot(nodes[idx].root);
    return nodes[idx].root;
}

void merge(int idx1, int idx2)
{
    int root1 = findRoot(idx1), root2 = findRoot(idx2);
    if (nodes[root1].rank > nodes[root2].rank)
    {
        swap(root1, root2);
    }
    nodes[root2].root = root1;
    if (nodes[root1].rank == nodes[root2].rank)
    {
        nodes[root1].rank++;
    }
}

const int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int i = 1; i <= tc; ++i)
    {
        int H, W;
        scanf("%d%d", &H, &W);
        for (int p = 0; p < H * W; ++p)
        {
            nodes[p].root = p;
            nodes[p].rank = 0;
            nodes[p].label = 0;
        }
        for (int y = 0; y < H; ++y)
        {
            for (int x = 0; x < W; ++x)
            {
                scanf("%d", &att[y][x]);
            }
        }
        for (int y = 0; y < H; ++y)
        {
            for (int x = 0; x < W; ++x)
            {
                int minHeight, minDir = -1;
                for (int d = 0; d < 4; ++d)
                {
                    int ty = y + dir[d][0], tx = x + dir[d][1];
                    if (ty <= -1 || tx <= -1 || ty >= H || tx >= W)
                    {
                        continue;
                    }
                    if (att[ty][tx] < att[y][x] && (minDir == -1 || minHeight > att[ty][tx]))
                    {
                        minDir = d;
                        minHeight = att[ty][tx];
                    }
                }
                if (minDir != -1)
                {
                    int ty = dir[minDir][0] + y, tx = dir[minDir][1] + x;
                    int idx1 = y * W + x, idx2 = ty * W + tx;
                    merge(idx1, idx2);
                }
            }
        }
        printf("Case #%d:\n", i);
        char label = 'a';
        for (int y = 0; y < H; ++y)
        {
            for (int x = 0; x < W; ++x)
            {
                int idx = y * W + x;
                int root = findRoot(idx);
                if (!nodes[root].label)
                {
                    nodes[root].label = label;
                    ++label;
                }
                if (x)
                {
                    putchar(' ');
                }
                putchar(nodes[root].label);
            }
            puts("");
        }
    }
    return 0;
}
