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

int T,Q;
vector< pair<int,int> > storeO,storeB;

int main()
{
    freopen("a.i2","r",stdin);
    freopen("a.o2","w",stdout);

    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        scanf("%d", &Q);
        storeO.clear();  storeB.clear();
        for (int i = 0; i < Q; i++)
        {
            char ch;
            while (1)
            {
                scanf("%c", &ch);  if (ch == 'O' || ch == 'B') break;
            }
            int x;  scanf("%d", &x);
            if (ch == 'O') storeO.push_back(make_pair(x,i)); else storeB.push_back(make_pair(x,i));
        }

        int ret = 0;
        int posO = 1,posB = 1,idO = 0,idB = 0,szO = storeO.size(),szB = storeB.size();
        int arriveO = 0,arriveB = 0;
        while (idO < szO || idB < szB)
        {
            ret++;
            if (idO < szO)
            {
                if (posO < storeO[idO].first) posO++;
                else if (posO > storeO[idO].first) posO--; else arriveO++;
            }
            if (idB < szB)
            {
                if (posB < storeB[idB].first) posB++;
                else if (posB > storeB[idB].first) posB--; else arriveB++;
            }
            if (idO < szO && (idB == szB || storeO[idO].second < storeB[idB].second))
            {
                if (arriveO && posO == storeO[idO].first) idO++,arriveO = 0;
            }
            else if (arriveB && posB == storeB[idB].first) idB++,arriveB = 0;
        }

        printf("Case #%d: %d\n", it, ret);
    }
}
