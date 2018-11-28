// B.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <vector>

std::ifstream in("B.in");
std::ofstream out("B.out");

int mas[105][105];
int res[105][105];
int T;
int color = 0;
int rx, ry;
int H, W;

void check(int x1, int y1)
{
    rx = x1, ry = y1;
    if (x1 > 0)
    {
        if (mas[rx][ry] > mas[x1 - 1][y1])
        {
            rx = x1 - 1;
            ry = y1;
        }
    }
    if (y1 > 0)
    {
        if (mas[rx][ry] > mas[x1][y1 - 1])
        {
            rx = x1;
            ry = y1 - 1;
        }
    }
    if (y1 < W - 1)
    {
        if (mas[rx][ry] > mas[x1][y1 + 1])
        {
            rx = x1;
            ry = y1 + 1;
        }
    }
    if (x1 < H - 1)
    {
        if (mas[rx][ry] > mas[x1 + 1][y1])
        {
            rx = x1 + 1;
            ry = y1;
        }
    }
}

void fill(int x, int y)
{
    res[x][y] = color;
    if (x > 0 && res[x - 1][y] == 0)
    {
        int x1 = x - 1;
        int y1 = y;
        check(x1, y1);
        if (rx == x && ry == y)
        {
            fill(x - 1, y);
        }
    }
    if (y > 0 && res[x][y - 1] == 0)
    {
        int x1 = x;
        int y1 = y - 1;
        check(x1, y1);
        if (rx == x && ry == y)
        {
            fill(x, y - 1);
        }
    }
    if (x < H - 1 && res[x + 1][y] == 0)
    {
        int x1 = x + 1;
        int y1 = y;
        check(x1, y1);
        if (rx == x && ry == y)
        {
            fill(x + 1, y);
        }
    }
    if (y < W - 1 && res[x][y + 1] == 0)
    {
        int x1 = x;
        int y1 = y + 1;
        check(x1, y1);
        if (rx == x && ry == y)
        {
            fill(x, y + 1);
        }
    }
}

int main()
{
    in >> T;
    for (int t = 0; t < T; t++)
    {
        color = 0;
        in >> H >> W;
        for (int h = 0; h < H; h++)
        {
            for (int w = 0; w < W; w++)
            {
                in >> mas[h][w];
            }
        }
        memset(res, 0, sizeof(res));
        int x = -1, y = -1;
        for (int h = 0; h < H; h++)
        {
            for (int w = 0; w < W; w++)
            {
                if ((mas[h][w] < mas[x][y] || x == -1) && res[h][w] == 0)
                {
                    x = h;
                    y = w;
                }
            }
        }
        while (x != -1)
        {
            color++;
            fill(x, y);
            // min
            x = -1;
            y = -1;
            for (int h = 0; h < H; h++)
            {
                for (int w = 0; w < W; w++)
                {
                    if ((mas[h][w] < mas[x][y] || x == -1) && res[h][w] == 0)
                    {
                        x = h;
                        y = w;
                    }
                }
            } 
        }
        std::vector< int > v;
        v.reserve(H * W);
        for (int h = 0; h < H; h++)
        {
            for (int w = 0; w < W; w++)
            {
                v.push_back(res[h][w]);
            }
        }
        std::vector< int > temp;
        temp.resize(27);
        for (int i = 0; i < 27; i++)
        {
            temp[i] = i;
        }
        int p = 0;
        for (int i = 0; i < v.size(); i++)
        {
            if (temp[v[i]] == p)
            {
            }
            if (temp[v[i]] == p + 1)
            {
                p++;
            }
            if (temp[v[i]] > p + 1)
            {
                p++;
                int g = temp[v[i]];
                temp[v[i]] = p;
                temp[p] = g;
            }
        }
        out << "Case #" << t + 1 << ":" << std::endl;
        for (int h = 0; h < H; h++)
        {
            for (int w = 0; w < W; w++)
            {
                out << (char)(temp[res[h][w]] + 'a' - 1) << ' ';
            }
            out << std::endl;
        }
    }
	return 0;
}

