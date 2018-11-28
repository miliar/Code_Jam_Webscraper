#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int ts[128][128];
int bs[128][128];
typedef pair<int, int> P;
typedef pair<int, P> PP;

struct Dif
{
    int x, y;
}dif[] = 
{
    -1, 0,
    1, 0,
    0, 1,
    0, -1
};

int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int H, N, M;
        cin >> H >> N >> M;

        memset(ts, 0, sizeof(ts));
        for(int i = 1; i <= N; i++)
            for(int j = 1; j <= M; j++)
                cin >> ts[i][j];
        for(int i = 1; i <= N; i++)
            for(int j = 1; j <= M; j++)
                cin >> bs[i][j];


        int dist[128][128] = {};
        priority_queue<PP, vector<PP>, greater<PP> > que;

        dist[1][1] = 1;
        que.push(PP(0, P(1, 1)));

        while(que.size())
        {
            PP p = que.top();
            que.pop();

            int x = p.second.first;
            int y = p.second.second;
            int t = p.first;
            int h = H - t;

//            cout << x << ' '<< y << ' ' << t << ' ' << h << '\n';
            if(dist[x][y] == t + 1)
            {
                for(int d = 0; d < 4; d++)
                {
                    int dx = x + dif[d].x;
                    int dy = y + dif[d].y;

                    if(bs[dx][dy] + 50 <= ts[dx][dy] && bs[x][y] + 50 <= ts[dx][dy] && bs[dx][dy] + 50 <= ts[x][y])
                    {
                        int got = (h + 50 <= ts[dx][dy])? t: (t + (h - ts[dx][dy] + 50));
                        int nt = (H - got >= bs[x][y] + 20)? got + 10: (got + 100);
                        if(got == 0)
                            nt = 0;
                        if(!dist[dx][dy] || dist[dx][dy] - 1 > nt)
                        {
                            dist[dx][dy] = nt + 1;
                            que.push(PP(nt, P(dx, dy)));
                        }
                    }
                }



            }


        }


        static int tn = 0;
        cout << "Case #" << ++tn << ": " << (dist[N][M] - 1) / 10 << '.' << (dist[N][M] - 1) % 10 << '\n';



    }
    return 0;
}
