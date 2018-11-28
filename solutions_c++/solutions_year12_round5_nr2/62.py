// g++ -Wall -O2

#include <vector>
#include <stack>
#include <set>
#include <cstdio>

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

using namespace std;

inline int CELL(int S, int r, int c)
{
    return r * (S * 2 + 1) + c;
}

int corneredge(int S, int cell)
{
    int r = cell / (S * 2 + 1);
    int c = cell % (S * 2 + 1);
    int flags = 0;
    int count = 0;
    if (r == 1)
    {
        flags |= 1;
        ++count;
    }
    if (c == r + S - 1)
    {
        flags |= 2;
        ++count;
    }
    if (c == S * 2 - 1)
    {
        flags |= 4;
        ++count;
    }
    if (r == S * 2 - 1)
    {
        flags |= 8;
        ++count;
    }
    if (r == c + S - 1)
    {
        flags |= 16;
        ++count;
    }
    if (c == 1)
    {
        flags |= 32;
        ++count;
    }
    if (count == 2)
        flags = -flags;
    return flags;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int S, M;
        scanf("%d%d", &S, &M);
        vector<int> moves(M);
        for (int i = 0; i < M; ++i)
        {
            int r, c;
            scanf("%d%d", &r, &c);
            moves[i] = r * (S * 2 + 1) + c;
        }
        vector<bool> board((S * 2 + 1) * (S * 2 + 1), false);
        vector<bool> negboard((S * 2 + 1) * (S * 2 + 1), false);
        for (int r = 1; r <= S; ++r)
        {
            for (int c = 1; c <= S + r - 1; ++c)
                negboard[r * (S * 2 + 1) + c] = true;
        }
        for (int r = S + 1; r <= S * 2 - 1; ++r)
        {
            for (int c = r - S + 1; c <= S * 2 - 1; ++c)
                negboard[r * (S * 2 + 1) + c] = true;
        }
        printf("Case #%d: ", testcase);
        bool found = false;
        for (int i = 0; i < M; ++i)
        {
            bool bridge = false;
            bool fork = false;
            bool ring = false;
            int move = moves[i];
            board[move] = true;
            negboard[move] = false;
            stack<int> s;
            s.push(move);
            set<int> edges;
            set<int> corners;
            vector<bool> visited((S * 2 + 1) * (S * 2 + 1), false);
            while (!s.empty())
            {
                int cell = s.top();
                s.pop();
                if (!board[cell] || visited[cell])
                    continue;
                visited[cell] = true;
                int flags = corneredge(S, cell);
                if (flags > 0)
                    edges.insert(flags);
                else if (flags < 0)
                    corners.insert(flags);
                s.push(cell + 1);
                s.push(cell + S * 2 + 2);
                s.push(cell + S * 2 + 1);
                s.push(cell - S * 2 - 1);
                s.push(cell - S * 2 - 2);
                s.push(cell - 1);
            }
            if (edges.size() >= 3)
                fork = true;
            if (corners.size() >= 2)
                bridge = true;
            for (int c = 1; c <= S; ++c)
                s.push(CELL(S, 1, c));
            for (int r = 1; r <= S; ++r)
            {
                s.push(CELL(S, r, 1));
                s.push(CELL(S, r, S + r - 1));
            }
            for (int r = S + 1; r <= S * 2 - 1; ++r)
            {
                s.push(CELL(S, r, r - S + 1));
                s.push(CELL(S, r, S * 2 - 1));
            }
            for (int c = S; c <= S * 2 - 1; ++c)
                s.push(CELL(S, S * 2 - 1, c));
            visited.assign((S * 2 + 1) * (S * 2 + 1), false);
            while (!s.empty())
            {
                int cell = s.top();
                s.pop();
                if (!negboard[cell] || visited[cell])
                    continue;
                visited[cell] = true;
                s.push(cell + 1);
                s.push(cell + S * 2 + 2);
                s.push(cell + S * 2 + 1);
                s.push(cell - S * 2 - 1);
                s.push(cell - S * 2 - 2);
                s.push(cell - 1);
            }
            for (int cell = 0; cell < (S * 2 + 1) * (S * 2 + 1); ++cell)
            {
                if (negboard[cell] && !visited[cell])
                {
                    ring = true;
                    break;
                }
            }
            if (bridge || fork || ring)
            {
                found = true;
                bool first = true;
                if (bridge)
                {
                    if (first)
                        first = false;
                    else
                        putchar('-');
                    printf("bridge");
                }
                if (fork)
                {
                    if (first)
                        first = false;
                    else
                        putchar('-');
                    printf("fork");
                }
                if (ring)
                {
                    if (first)
                        first = false;
                    else
                        putchar('-');
                    printf("ring");
                }
                printf(" in move %d\n", i + 1);
                break;
            }
        }
        if (!found)
            printf("none\n");
    }
    return 0;
}
