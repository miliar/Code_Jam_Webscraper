#include    <iostream>
#include    <string>
using   namespace   std;

int b[2500000];
int main ()
{   
    freopen ("gcj.in", "r", stdin);
    freopen ("gcj.out", "w", stdout);

    int casenum, N;


    int A, B, i, j, k, ans, s, p, q, r, now;

    cin >> casenum;
    for (N=1; N<=casenum; ++N)
    {
        ans = 0;
        memset (b, 0, sizeof (b));
         cin >> A >> B;
                                       for (k=A; k<=B; ++k)
        {
            s = 10;
            while (s < k)
            {
                p = k / s;
                q = k % s;
                if (q < s/10)
                {
                    s *= 10;
                    continue;
                }
                now = 1; r = p;
                while (r)
                {
                    now *=10;
                    r /=10;
                }
                now *= q;
                now += p;
                if (now != k && A <= now && now <= B && b[now] != k)
                {   ans++;
                    b[now] = k;
                }
                s *= 10;
            }
        }
        cout << "Case #" << N << ": " << ans/2 << endl;
    }

    return 0;
}



