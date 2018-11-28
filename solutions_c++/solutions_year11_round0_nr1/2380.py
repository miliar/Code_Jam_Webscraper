#include <cstdio>
#include <iostream>
#include <string>
#define MAXN (1 << 7)
using namespace std;

int n;
int who[MAXN], pos[MAXN];

inline int getNext(int from, int bot)
{
    for (int i=from; i < n; ++i)
        if (who[i] == bot)
            return pos[i];
    return -1;
}

inline int solve()
{
    int curPos[2], ans = 0;
    curPos[0] = curPos[1] = 1;
    for (int cur=0; cur < n; ++cur)
    {
        int curBot = who[cur];
        int nextOtherBot = getNext(cur+1, !curBot);

        while (curPos[curBot] != pos[cur])
        {
            if (pos[cur] < curPos[curBot]) curPos[curBot]--;
            else curPos[curBot]++;

            if (nextOtherBot < curPos[!curBot]) curPos[!curBot]--;
            if (nextOtherBot > curPos[!curBot]) curPos[!curBot]++;
            ans ++;
        }
        ans ++;
        if (nextOtherBot < curPos[!curBot]) curPos[!curBot]--;
        if (nextOtherBot > curPos[!curBot]) curPos[!curBot]++;
    }
    return ans;
}

inline void read()
{
    cin >> n;
    for (int i=0; i < n; ++i)
    {
        string str;
        cin >> str;
        who[i] = (str[0] == 'O');
        cin >> pos[i];
    }
}

int main()
{
    int brt, testNo = 0;
    cin >> brt;

    while (brt --)
    {
        read();
        cout << "Case #" << ++testNo << ": " << solve() << endl;
    }
    return 0;
}
