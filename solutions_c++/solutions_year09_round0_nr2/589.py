#include <iostream>
#include <queue>

struct P
{
    P() : x(0), y(0) {}
    P(int a, int b) : x(a), y(b) {}
    int x, y;
};

int A[100][100], DX[100][100], DY[100][100];
int id[100][100];

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        int H, W;
        std::cin >> H >> W;
        for (int y = 0 ; y < H ; ++y)
            for (int x = 0 ; x < W ; ++x)
                std::cin >> A[y][x];

        for (int y = 0 ; y < H ; ++y)
        {
            for (int x = 0 ; x < W ; ++x)
            {
                int min = A[y][x];
                int dx = 0, dy = 0;
                if (y > 0 && A[y-1][x] < min)
                {
                    dx = 0;
                    dy = -1;
                    min = A[y-1][x];
                }
                if (x > 0 && A[y][x-1] < min)
                {
                    dx = -1;
                    dy = 0;
                    min = A[y][x-1];
                }
                if (x < W-1 && A[y][x+1] < min)
                {
                    dx = 1;
                    dy = 0;
                    min = A[y][x+1];
                }
                if (y < H-1 && A[y+1][x] < min)
                {
                    dx = 0;
                    dy = 1;
                    min = A[y+1][x];
                }
                DX[y][x] = dx;
                DY[y][x] = dy;
                id[y][x] = 0;
            }
        }

        std::queue<P> q;
        int last = 1;
        for (int y = 0 ; y < H ; ++y)
            for (int x = 0 ; x < W ; ++x)
                if (!DX[y][x] && !DY[y][x])
                {
                    q.push(P(x, y));
                    id[y][x] = last++;
                }

        while (!q.empty())
        {
            P p = q.front();
            q.pop();
            int num = id[p.y][p.x];
            if (p.x > 0 && DX[p.y][p.x-1] == 1)
            {
                q.push(P(p.x-1, p.y));
                id[p.y][p.x-1] = num;
            }
            if (p.y > 0 && DY[p.y-1][p.x] == 1)
            {
                q.push(P(p.x, p.y-1));
                id[p.y-1][p.x] = num;
            }
            if (p.x < W - 1 && DX[p.y][p.x+1] == -1)
            {
                q.push(P(p.x+1, p.y));
                id[p.y][p.x+1] = num;
            }
            if (p.y < H - 1 && DY[p.y + 1][p.x] == -1)
            {
                q.push(P(p.x, p.y + 1));
                id[p.y + 1][p.x] = num;
            }
        }

        std::vector<char> z(last + 1);

        char lastLetter = 'a';
        for (int y = 0 ; y < H ; ++y)
            for (int x = 0 ; x < W ; ++x)
                if (!z[id[y][x]])
                    z[id[y][x]] = lastLetter++;

        std::cout << "Case #" << t << ":\n";
        for (int y = 0 ; y < H ; ++y)
        {
            for (int x = 0 ; x < W ; ++x)
                std::cout << z[id[y][x]] << " ";
            std::cout << "\n";
        }
    }
	return 0;
}

