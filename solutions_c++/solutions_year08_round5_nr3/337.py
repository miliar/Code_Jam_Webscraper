#include <iostream>

using namespace std;

int N;
int M;

int cl[20];

int d[20][(1 << 10)+10];

int bits(int i)
{
    int res = 0;
    while (i)
    {
        res++;
        i &= (i-1);
    }

    return res;
}

bool valid(int m)
{
    for (int i=0; i < 10; i++)
    {
        if ((m & (3 << i)) == (3 << i))
            return false;
    }

    return true;
}

bool valid(int pm, int m)
{
    return ((m&(pm>>1)) == 0) &&
           ((m&(pm<<1)) == 0);

}

void backtrack(int i, int m)
{
    if (i != 0)
    {
        for (int pm=0; pm < 1 << M; pm++)
            if (d[i-1][pm] != -1 && valid(pm, m) && d[i-1][pm] + bits(m) == d[i][m])
            {
                cout << "Going to " << i-1 << " " << pm << " " << d[i-1][pm] << endl;
                backtrack(i-1, pm);
                break;
            }
    }

    for (int j=0; j < M; j++)
        cout << ((m&(1<<j)) ? "o" : ".");
    cout << " " << m << endl;
}

int solve()
{
    memset(d, -1, sizeof(d));

    d[0][0] = 0;

    for (int i=0; i < N; i++)
        for (int m=0; m < (1 << M); m++)
            if ((m & cl[i]) == m && valid(m))
            {
                d[i+1][m] = 0;
                for (int pm=0; pm < (1 << M); pm++)
                    if (d[i][pm] != -1 && valid(pm, m))
                        d[i+1][m] >?= d[i][pm] + bits(m);
            }

    int res = 0;
    for (int m=0; m < (1 << M); m++)
        res >?= d[N][m];

    /*for (int m=0; m < (1 << M); m++)
        if (res == d[N][m])
        {
            backtrack(N, m);
            break;
        }*/

    //cout << "Valid " << valid(1005) << ": " << d[1][1005] << endl;

    return res;
}


int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int T;
    cin >> T;

    for (int tt=1; tt<=T; tt++)
    {
        cin >> N >> M;

        for (int i=0; i < N; i++)
        {
            string s;
            cin >> s;
            cl[i] = 0;
            for (int j=0; j < M; j++)
                if (s[j] == '.')
                    cl[i] |= (1 << j);
        }

        cout << "Case #" << tt << ": " << solve() << endl;
    }
}
