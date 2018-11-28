#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

string combine[105],oppose[105],arg;
int T,c,o,s;
int canCombine[256][256],canOppose[256][256];

int main()
{
    freopen("b.i2","r",stdin);
    freopen("b.o2","w",stdout);

    scanf("%d\n", &T);
    for (int it = 1; it <= T; it++)
    {
        scanf("%d", &c);
        for (int i = 0; i < c; i++)
          while (1)
          {
              cin >> combine[i];  if (!combine[i].empty()) break;
          }
        scanf("%d", &o);
        for (int i = 0; i < o; i++)
          while (1)
          {
            cin >> oppose[i];  if (!oppose[i].empty()) break;
          }
        scanf("%d", &s);
        cin >> arg;

        memset(canCombine,-1,sizeof(canCombine));
        for (int i = 0; i < c; i++) canCombine[combine[i][0]][combine[i][1]] = canCombine[combine[i][1]][combine[i][0]] = combine[i][2];
        memset(canOppose,false,sizeof(canOppose));
        for (int i = 0; i < o; i++) canOppose[oppose[i][0]][oppose[i][1]] = canOppose[oppose[i][1]][oppose[i][0]] = true;

        vector<int> remain;
        for (int i = 0; i < s; i++)
        {
            remain.push_back(arg[i]);
            if (remain.size() < 2) continue;
            int chA = remain[remain.size() - 2],chB = remain[remain.size() - 1];
            if (canCombine[chA][chB] >= 0)
            {
                remain.pop_back();  remain.pop_back();  remain.push_back(canCombine[chA][chB]);  continue;
            }
            chB = remain[remain.size() - 1];
            for (int j = 0; j + 1 < remain.size(); j++)
            {
                chA = remain[j];
                if (canOppose[chA][chB])
                {
                    remain.clear();  break;
                }
            }
        }

        printf("Case #%d: [", it);
        for (int i = 0; i < remain.size(); i++)
        {
            printf("%c", remain[i]);
            if (i < remain.size() - 1) printf(", ");
        }
        printf("]\n");
    }
}
