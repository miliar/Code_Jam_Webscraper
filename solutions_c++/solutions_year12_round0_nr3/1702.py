#include <cstdlib>
#include <iostream>
#include <set>

using namespace std;

#define le 100

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out","w",stdout);
    int A, B, i, j;
    int t, ans, temp1, temp2, n, m, cnt;
    scanf ("%d", &t);
    for (int cas = 1; cas <= t; cas++)
    {
        scanf ("%d %d", &A, &B);
        printf ("Case #%d: ", cas);
        ans = 0;
        for (i = A; i <= B; i++)
        {
            cnt = 0;
            n = i;
            temp1 = 1;
            while (n)
            {
                  cnt++;
                  n /= 10;
                  temp1 *= 10;
            }
            n = i;
            temp2 = 1;
            set<int> se;
            for (j = 0; j < cnt; j++)
            {
                m = (n % temp2) * temp1 + n / temp2;
                
                if (m >= A && m <= B && m != n)
                {
                   if (j != 0 && se.find(m) == se.end())
                   {
                      se.insert(m);
                      //printf ("%d %d\n", n, m);
                      ans++;
                   }
                }
                temp1 /= 10;
                temp2 *= 10;
            }
        }
        printf ("%d\n", ans / 2);
    }
    return 0;
}
