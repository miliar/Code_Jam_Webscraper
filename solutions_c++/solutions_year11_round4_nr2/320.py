#include<iostream>

using namespace std;

int R, C, D;
long long Map[501][501];
long long MassX[501][501];
long long MassY[501][501];
long long Mass[501][501];

void read()
{
    cin >> R >> C >> D;
    char c;
    for(int i = 1; i <= R; ++i)
        for(int j = 1; j <= C; ++j)
        {
            cin >> c;
            Map[i][j] = c - '0';
        }
}


void prepare()
{
    int i, j;
    for(i = 1; i <= R; ++i)
        for(j = 1; j <= C; ++j)
        {
            Mass[i][j] = Mass[i-1][j] + Mass[i][j - 1] - Mass[i - 1][j - 1] + Map[i][j];
            MassX[i][j] = MassX[i-1][j] + MassX[i][j - 1] - MassX[i - 1][j - 1] + Map[i][j] * i;
            MassY[i][j] = MassY[i-1][j] + MassY[i][j - 1] - MassY[i - 1][j - 1] + Map[i][j] * j;
        }
}

int solve()
{
    int ans = 0;
    int k, startx, starty, x, y;
    long long sumx, sumy, sum;
    for (k = 3; k <= R && k <= C; ++k)
    {
        for(startx = 1; startx + k <= R + 1; ++startx)
        {
            for(starty = 1; starty + k <= C + 1; ++starty)
            {
                sum = Mass[startx + k - 1][starty + k - 1] - Mass[startx - 1][starty + k - 1] - Mass[startx + k - 1][starty - 1] + Mass[startx - 1][starty - 1];
                sumx = MassX[startx + k - 1][starty + k - 1] - MassX[startx - 1][starty + k - 1] - MassX[startx + k - 1][starty - 1] + MassX[startx - 1][starty - 1];
                sumy = MassY[startx + k - 1][starty + k - 1] - MassY[startx - 1][starty + k - 1] - MassY[startx + k - 1][starty - 1] + MassY[startx - 1][starty - 1];
                sumx -= (startx + 0) * Map[startx + 0][starty + 0];
                sumx -= (startx + k - 1) * Map[startx + k - 1][starty + 0];
                sumx -= (startx + 0) * Map[startx + 0][starty + k - 1];
                sumx -= (startx + k - 1) * Map[startx + k - 1][starty + k - 1];
                sumy -= (starty + 0) * Map[startx + 0][starty + 0];
                sumy -= (starty + k - 1) * Map[startx + 0][starty + k - 1];
                sumy -= (starty + 0) * Map[startx + k - 1][starty + 0];
                sumy -= (starty + k - 1) * Map[startx + k - 1][starty + k - 1];
                sum -= Map[startx + 0][starty + 0];
                sum -= Map[startx + 0][starty + k - 1];
                sum -= Map[startx + k -1 ][starty + 0];
                sum -= Map[startx + k - 1][starty + k - 1];

                if (  (2 * startx + k - 1) * sum == 2 * sumx &&
                      (2 * starty + k - 1) * sum == 2 * sumy &&
                      k > ans)
                    ans = k;
            }
        }
    }
    return ans;
}

int main()
{
    int T;
    cin >> T;
    int num;
    for(num = 1; num <= T; ++num)
    {
        read();
        cout << "Case #" << num << ": ";
        prepare();
        int ans = solve();
        if(ans == 0)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
}
