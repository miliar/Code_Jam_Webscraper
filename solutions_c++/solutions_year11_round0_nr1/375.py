#include <cstdio>
#include <cstring>

using namespace std;

const int d[] = {-1, 0, 1};

const int maxN = 128;
const int O = 0;
const int B = 1;

struct QQ
{
    int Op;
    int Bp;
    int len;
    int step;
    int pre;
    QQ()
    {

    }
    QQ(int _Op, int _Bp, int _len, int _step, int _pre)
    {
        Op = _Op;
        Bp = _Bp;
        len = _len;
        step = _step;
        pre = _pre;
    }
};

QQ que[maxN * maxN * maxN];
bool vist[maxN][maxN][maxN];

struct PRESS
{
    int OB;
    int idx;
};

int np;
PRESS p[maxN];

bool legal(int idx)
{
    return idx >= 1 && idx <= 100;
}

void printPath(int idx)
{
    if(que[idx].pre != -1)
        printPath(que[idx].pre);
    printf("---> O:%d B:%d press:%d step:%d\n", que[idx].Op, que[idx].Bp, que[idx].len, que[idx].step);
}

int bfs()
{
    QQ in(1, 1, 0, 0, -1);

    int qh = -1, qe = 0;
    memset(vist, false, sizeof(vist));

    que[0] = in;
    vist[1][1][0] = true;

    while(qh != qe)
    {
        qh++;

        int preO = que[qh].Op;
        int preB = que[qh].Bp;
        int prelen = que[qh].len;
        int prestep = que[qh].step;

        /*printf("---> O:%d B:%d press:%d step:%d\n", preO, preB, prelen, prestep);*/

        if(prelen == np)
        {
            /*printPath(qh);*/
            return prestep;
        }

        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++)
            {
                int nO = preO + d[i];
                int nB = preB + d[j];
                if(!legal(nO) || !legal(nB)) continue;
                int nlen = prelen;
                if(vist[nO][nB][nlen]) continue;
                int nstep = prestep + 1;
                QQ tmp(nO, nB, nlen, nstep, qh);
                que[++qe] = tmp;
                vist[nO][nB][nlen] = true;
            }
        if(prelen < np && p[prelen].OB == O && p[prelen].idx == preO)
        {
            for(int j = 0; j < 3; j++)
            {
                int nO = preO;
                int nB = preB + d[j];
                if(!legal(nO) || !legal(nB)) continue;
                int nlen = prelen + 1;
                if(vist[nO][nB][nlen]) continue;
                int nstep = prestep + 1;
                QQ tmp(nO, nB, nlen, nstep, qh);
                que[++qe] = tmp;
                vist[nO][nB][nlen] = true;
            }/*
            if(prelen + 1 < np && p[prelen + 1].OB == B && p[prelen + 1].idx == preB)
            {
                int nO = preO;
                int nB = preB;
                if(!legal(nO) || !legal(nB)) continue;
                int nlen = prelen + 2;
                if(vist[nO][nB][nlen]) continue;
                int nstep = prestep + 1;
                QQ tmp(nO, nB, nlen, nstep, qh);
                que[++qe] = tmp;
                vist[nO][nB][nlen] = true;
            }*/
        }

        if(prelen < np && p[prelen].OB == B && p[prelen].idx == preB)
        {
            for(int i = 0; i < 3; i++)
            {
                int nO = preO + d[i];
                int nB = preB;
                if(!legal(nO) || !legal(nB)) continue;
                int nlen = prelen + 1;
                if(vist[nO][nB][nlen]) continue;
                int nstep = prestep + 1;
                QQ tmp(nO, nB, nlen, nstep, qh);
                que[++qe] = tmp;
                vist[nO][nB][nlen] = true;
            }/*
            if(prelen + 1 < np && p[prelen + 1].OB == O && p[prelen + 1].idx == preO)
            {
                int nO = preO;
                int nB = preB;
                if(!legal(nO) || !legal(nB)) continue;
                int nlen = prelen + 2;
                if(vist[nO][nB][nlen]) continue;
                int nstep = prestep + 1;
                QQ tmp(nO, nB, nlen, nstep, qh);
                que[++qe] = tmp;
                vist[nO][nB][nlen] = true;
            }*/
        }
    }

    return -1;
}

int main()
{
    //freopen("A2.in", "r", stdin);
    //freopen("A2.out", "w", stdout);
    int cas;
    char str[maxN];

    scanf("%d", &cas);
    for(int cc = 0; cc < cas; cc++)
    {
        scanf("%d", &np);
        for(int i = 0; i < np; i++)
        {
            int idx;
            scanf("%s %d", str, &idx);
            p[i].OB = (str[0] == 'O' ? O : B);
            p[i].idx = idx;
        }

        printf("Case #%d: %d\n", cc + 1, bfs());
    }
    return 0;
}
