#include <cstdio>
#include <cctype>
#include <map>
#include <algorithm>

using namespace std;

    typedef map<int, int, greater<int> > mmap;

    const int maxsize = 600;

    int m, n;
    int board[maxsize][maxsize];
    int weight[maxsize][maxsize];
    

void loadboard()
{
    scanf("%d%d\n", &m, &n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n/4; j++) {
            char c;
            scanf("%c", &c);
            if (isdigit(c))
                c = c - '0';
            else
                c = 10 + c - 'A';
            for (int k = 3; k >= 0; k--) {
                board[i][4*j+k] = c&1;
                c >>= 1;
            }
        }
        scanf("\n");
    }
}

void printboard()
{
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            printf(board[i][j] ? "." : "#");
        printf("\n");
    }
}

void printweights()
{
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            printf("%d", weight[i][j]);
        printf("\n");
    }
    printf("\n");
}

void calcweights(int startx, int endx, int starty, int endy)
{
    for (int i = endy; i >= starty; i--)
        for (int j = startx; j <= endx; j++)
            if (board[i][j] == -1)
                weight[i][j] = 0;
            else if (i < m - 1 && board[i + 1][j] != -1 && board[i][j] != board[i + 1][j])
                weight[i][j] = weight[i + 1][j] + 1;
            else
                weight[i][j] = 1;
    // printweights();
}

void cutout(int startx, int endx, int starty, int endy)
{
    for (int i = endy; i >= starty; i--)
        for (int j = startx; j <= endx; j++)
            board[i][j] = -1;
}

bool findandcut(int size)
{
    for (int i = 0; i < m; i++) {
        int good = 0;
        for (int j = 0; j < n; j++) {
            if (weight[i][j] < size)
                good = 0;
            else if (j > 0 && board[i][j] != board[i][j - 1])
                good++;
            else
                good = 1;
            if (good >= size) {
                cutout(j - size + 1, j, i, i + size - 1);
                calcweights(j - size + 1, j, 0, i + size - 1);
                return true;
            }
        }
    }
    return false;
}

mmap solve()
{
    mmap answer;
    loadboard();
    calcweights(0, n - 1, 0, m - 1);
    // printboard();
    for (int size = min(n, m); size >= 1; size--) {
        if (findandcut(size)) {
            answer[size] = 1;
            while (findandcut(size))
                answer[size]++;
        }
    }
    return answer;
}

int main()
{
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        fprintf(stderr, "%d\n", t);
        mmap answer = solve();
        printf("Case #%d: %d\n", t, answer.size());
        for (map<int, int>::iterator it = answer.begin(); it != answer.end(); it++)
            printf("%d %d\n", it->first, it->second);
    }
    return 0;
}
