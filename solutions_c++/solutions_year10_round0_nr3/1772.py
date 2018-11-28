#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
#define MAXN 1010
typedef long long int lint;

lint r, k, n;
lint g[MAXN];
//lint sum[MAXN];
lint flg[MAXN];
lint a[MAXN], top;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int i, j, csnum, cs, l, s, t, rm;
    lint tot;
    lint ts, ans, cnt;
    scanf ("%d", &csnum);
    for (cs = 1; cs <= csnum; cs++)
    {
        scanf ("%lld %lld %lld", &r, &k, &n);
        //sum[0] = 0;
        tot = 0;
        for (i = 0; i < n; i++)
        {
            scanf (" %I64d", &g[i]);
            //cout << "g[i] " << g[i] << endl;
            //sum[i] = sum[i-1] + g[i];
            tot += g[i];
        }

        if (k >= tot)
        {
            ans = r * tot;
            printf ("Case #%d: %I64d\n", cs, ans);
            continue;
        }

        memset(flg, -1, sizeof(flg));
        memset(a, 0, sizeof(a));

        s = 0;
        t = 0;
        top = 0;
        ans = 0;
        for (i = 0; i < r; i++)
        {
            ts = 0;
            for (; ts + g[t] <= k; t = (t+1)%n)
            {
                ts += g[t];
                //printf ("t %d ts %I64d\n", t, ts);
                //cout << "ts " << ts << endl;
            }

            //printf ("\ns %d t %d\n", s, t);
            if (flg[s] != -1)
            {
                //cnt = ts + ans - a[flg[s]];
                cnt = 0;
                for (j = flg[s]; j < i; j++)
                    cnt += a[j];
                //cout << "cnt " << cnt << endl;
                l = i - flg[s];
                //r -= flg[s];

                rm = (r - i) % (i - flg[s]);
               // cout << "flg[s] " << flg[s] << endl;
               // cout << "ans " << ans << endl;
                ans += (r - i) / l * cnt;
                //cout << " ans " << ans << endl;
                for (j = flg[s]; j < flg[s] + rm; j++)
                    ans += a[j];
              //  printf ("cnt %I64d rm %d\nans %I64d", cnt, rm,ans);
                break;
            }
            else
            {
                ans += ts;
                flg[s] = i;
                a[top++] = ts;
                s = t;
              //  cout << "ans " << ans << endl;
            }
        }
        printf ("Case #%d: %I64d\n", cs, ans);
       // cout << ans << endl;
    }
}
/*
3
9 21 9
2 10 4 2 9 2 7 6 3
2 14 8
1 10 8 10 2 5 8 10
*/
