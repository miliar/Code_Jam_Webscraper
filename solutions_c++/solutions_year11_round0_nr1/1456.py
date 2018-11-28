// A small CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

int myabs(int x)
{
    return x > 0 ? x : -x;
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T;
    int N;
    int i;
    int cas = 1;
    int pos_O, pos_B;
    int rem_O, rem_B;
    int ans, tmp;
    char P[10];
    int R;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &N);
        pos_O = pos_B = 1;
        rem_O = rem_B = 0;
        ans = 0;
        for (i = 0; i < N; i++)
        {
            scanf("%s%d", P, &R);
            if (P[0] == 'O')
            {
                tmp = myabs(pos_O - R);
                if (rem_O >= tmp)
                {
                    ans++;
                    rem_B++;
                }
                else
                {
                    ans += tmp - rem_O + 1;
                    rem_B += tmp - rem_O + 1;
                }
                rem_O = 0;
                pos_O = R;
            }
            else
            {
                tmp = myabs(pos_B - R);
                if (rem_B >= tmp)
                {
                    ans++;
                    rem_O++;
                }
                else
                {
                    ans += tmp - rem_B + 1;
                    rem_O += tmp - rem_B + 1;
                }
                rem_B = 0;
                pos_B = R;
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
