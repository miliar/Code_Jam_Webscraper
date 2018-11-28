#include <iostream>
#include <queue>

using namespace std;

char a[64][64];
int d[64][64][64][64];

int qx[1<<24];
int qy[1<<24];
int ql[1<<24];
int qr[1<<24];

struct str
{
    int i, d;
    bool operator<(const str &other) const
    {
        return d > other.d;
    }
};

priority_queue<str> q;

int qs, qf;

int ans;

int n, m;

void push(int x, int y, int l, int r, int k)
{
    if (x == n-1)
    {
        ans = min(ans, k);
        return;
    }

    if (k >= d[x][y][l][r])
        return;

    str t;
    t.i = qf;
    t.d = k;
    q.push(t);

    qx[qf] = x;
    qy[qf] = y;
    ql[qf] = l;
    qr[qf] = r;
    qf++;

    d[x][y][l][r] = k;

}

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        ans = 1<<30;

        int f;
        cin >> n >> m >> f;
        for (int i=0; i<n; i++)
            cin >> a[i];

        for (int j=0; j<m; j++)
            a[n][j] = 0;

        qs = qf = 0;

        for (int i=0; i<=n; i++)
            for (int j=0; j<m; j++)
                for (int k=0; k<m; k++)
                    for (int l=0; l<m; l++)
                        d[i][j][k][l] = 1<<30;

        int l, r, x, y;
        for (r=0; a[0][r+1] == '.'; r++);

        push(0, 0, 0, r, 0);

        for (; q.size(); q.pop())
        {
            int qs = q.top().i;
            x = qx[qs];
            y = qy[qs];
            l = ql[qs];
            r = qr[qs];

            int p = d[x][y][l][r];

            if (d[x][y][l][r] == -1)
                continue;
            d[x][y][l][r] = -1;

            for (int j=y; j>=l; j--)
                if (a[x+1][j] == '.')
                {
                    int i;
                    for (i=x; a[i+1][j] == '.'; i++);

                    if (i-x <= f)
                    {
                        int u, v;
                        for (u=j; u && a[i][u-1] == '.'; u--);
                        for (v=j; a[i][v+1] == '.'; v++);
                        push(i, j, u, v, p);
                    }

                    l = j+1;
                    break;
                }

            for (int j=y; j<=r; j++)
                if (a[x+1][j] == '.')
                {
                    int i;
                    for (i=x; a[i+1][j] == '.'; i++);
                    if (i-x <= f)
                    {
                        int u, v;
                        for (u=j; u && a[i][u-1] == '.'; u--);
                        for (v=j; a[i][v+1] == '.'; v++);
                        push(i, j, u, v, p);
                    }

                    r = j-1;
                    break;
                }

            for (int j=l; j<r; j++)
            {
                int z = j;
                if (j == l)
                    for (; z && a[x+1][z-1] == '.'; z--);

                for (int k=j; k<r; k++)
                    if (a[x+2][k] != '.')
                        push(x+1, k, z, k, p + k-j+1);
            }

            for (int j=r; j>l; j--)
            {
                int z = j;
                if (j == r)
                    for (; z && a[x+1][z+1] == '.'; z++);

                for (int k=j; k>l; k--)
                    if (a[x+2][k] != '.')
                        push(x+1, k, k, z, p + j-k+1);
            }

            if (l != r)
                for (int j=l; j<=r; j++)
                    if (a[x+2][j] == '.')
                    {
                        int i;
                        for (i=x+1; a[i+1][j] == '.'; i++);
                        if (i-x <= f)
                        {
                            int u, v;
                            for (u=j; u && a[i][u-1] == '.'; u--);
                            for (v=j; a[i][v+1] == '.'; v++);
                            push(i, j, u, v, p + 1);
                        }
                    }
        }

        cout << "Case #" << tt << ": ";
        if (ans < 1<<30)
            cout << "Yes " << ans << endl;
        else
            cout << "No" << endl;
    }
    
    
    return 0;
}
