#include    <iostream>
#include    <string>
using   namespace   std;

int a[1000];

int main ()
{   
    freopen ("gcj.in", "r", stdin);
    freopen ("gcj.out", "w", stdout);

    int casenum, N;


    int T, S, P, i, j, now, k, p, q, r, ans;

    cin >> casenum;
    for (N=1; N<=casenum; ++N)
    {
        ans = 0; p = 0; q = 0;
        cin >> T >> S >> P;
        for (i=1; i<=T; ++i)
        {
            cin >> now;
            r = 2; //cannot
            for (j=P; j<= now; ++j)
            {   k = now - 3*j;
                if (k >= -4 && k <= 4 && r >= 2) r = 1;
                if (k >= -2 && k <= 2 && r >= 1) r = 0;
                if (r ==0) break;
            }
            if (r == 0) ans++;
            if (r == 1 && S)
            {
                S--;
                ans++;
            }
        }
        cout << "Case #" << N << ": " << ans << endl;
    }

    return 0;
}



