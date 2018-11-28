#include <iostream>
#include <cstring>
using namespace std;
const long r = 1100000, superBig = 2147483647;

bool stop = false;
long c, ans;
//long p[r * 100];
long t[20000][2];

long getadd(long k)
{
        for (long i = 0; i < c; i++)
            if (t[i][0] == k)
               return i;
        t[c][0] = k;
        t[c][1] = 0;
        return c++;
}

void solve(long k)
{
                if (stop)
                return;
        bool flag = false;
        RRR:
        for (long i = 0; i < c; i++)
                if (t[i][1] > 1) {
                        flag = true;
                        long x = t[i][0];
                        long l = getadd(x - 1), r = getadd(x + 1);
                        ++t[l][1];
                        ++t[r][1];
                        t[i][1] -= 2;
                        break;
                }
        if (!stop && !flag) {
                ans = ans < k ? ans : k;
                stop = true;
                } else if (flag) {
                        flag = false;
                        ++k;
                        goto RRR;
                        }  
                        
}

int main(void)
{
              freopen("c.in", "r", stdin);
              freopen("c.out", "w", stdout);
        long T;
        cin >> T;
        //memset(p, -1, sizeof(p));
        for (long loop = 1; loop <= T; loop++) {
                cin >> c;
                for (long i = 0; i < c; i++) {
                        cin >> t[i][0] >> t[i][1];
                        //p[t[i][0] + r] = i;
                }
                ans = superBig;
                stop = false;
                solve(0);
                cout << "Case #" << loop << ": " << ans << endl;
                //for (long i = 0; i < c; i++)
                    //p[t[i][0] + r] = -1;
        }
        return 0;
}
