#include <iostream>
#include <vector>

using namespace std;

long long N, A, B, C, D, x0, y0, M;
int X[100000];
int Y[100000];

void generate()
{
    vector<pair<int, int> > pts(N);

    pts[0].first  = x0;
    pts[0].second = y0;

    for (int i=1; i < N; i++)
    {
        pts[i].first = (A*pts[i-1].first+B)%M;
        pts[i].second = (C*pts[i-1].second+D)%M;
    }

    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());

    N = pts.size();
    for (int i=0; i < pts.size(); i++)
    {
        X[i] = pts[i].first;
        Y[i] = pts[i].second;
    }
}

long long simple_solve()
{
    long long res = 0;

    for (int i=0; i < N; i++)
        for (int j=i+1; j < N; j++)
            for (int k=j+1; k < N; k++)
                if ((X[i] + X[j] + X[k])%3 == 0 &&
                    (Y[i] + Y[j] + Y[k])%3 == 0)
                    res ++;

    return res;
}

long long complex_solve()
{
    long long cnt[3][3];

    memset(cnt, 0, sizeof(cnt));
    for (int i=0; i < N; i++)
        cnt[X[i]%3][Y[i]%3]++;


    long long res = 0;
    for (int a1=0; a1 < 3; a1++)
        for (int b1=0; b1 < 3; b1++)
            for (int a2=0; a2 < 3; a2++)
                for (int b2=0; b2 < 3; b2++)
                {
                    int a3 = (9 - a1 - a2)%3;
                    int b3 = (9 - b1 - b2)%3;

                    long long d1 = cnt[a1][b1];
                    long long d2 = cnt[a2][b2];
                    long long d3 = cnt[a3][b3];

                    if (a1 == a2 && b1 == b2) d2--;
                    if (a1 == a3 && b1 == b3) d3--;
                    if (a2 == a3 && b2 == b3) d3--;

                    if (d1 > 0 && d2 > 0 && d3 > 0)
                        res += d1*d2*d3;
                }

    return res/6;
}

long long solve()
{
 //   long long res0 = simple_solve();
    long long res1 = complex_solve();

/*    if (res0 != res1)
    {
        cout << "FAIL: got=" << res1 << ", need=" << res0 << endl;
    }*/

    return res1;
}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;

    for (int i=1; i <= T; i++)
    {
        cin >> N >> A >> B >> C >> D >> x0 >> y0 >> M;

        generate();
        cout << "Case #" << i << ": " << solve() << endl;
    }
}
