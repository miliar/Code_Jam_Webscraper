#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

int M, V;
int list[10000][2];
int change[5000];
int gate[10000];

int search(int which, int value)
{
    if (which >= (M-1)/2)
    {
        if (gate[which] == value)
        {
            return 0;
        }
        else
        {
            return -2;
        }
    }
    if (list[which][value] != -1) return list[which][value];
    int &changes = list[which][value];
    changes = 10000000;
    int left, right;
    if (value == 0)
    {
        if (gate[which] == 1 || change[which] == 1)
        {
            //1 & 0
            left = search(which * 2 + 1, 1);
            right = search(which * 2 + 2, 0);
            if (left >= 0 && right >= 0 && changes > left + right) changes = left + right + (1 - gate[which]);
            //0 & 1
            left = search(which * 2 + 1, 0);
            right = search(which * 2 + 2, 1);
            if (left >= 0 && right >= 0 && changes > left + right) changes = left + right + (1 - gate[which]);
        }
        //0 |& 0
        left = search(which * 2 + 1, 0);
        right = search(which * 2 + 2, 0);
        if (left >= 0 && right >= 0 && changes > left + right) changes = left + right;
    }
    else
    {
        if (gate[which] == 0 || change[which] == 1)
        {
            //1 | 0
            left = search(which * 2 + 1, 1);
            right = search(which * 2 + 2, 0);
            if (left >= 0 && right >= 0 && changes > left + right) changes = left + right + gate[which];
            //0 | 1
            left = search(which * 2 + 1, 0);
            right = search(which * 2 + 2, 1);
            if (left >= 0 && right >= 0 && changes > left + right) changes = left + right + gate[which];
        }
        //1 |& 1
        left = search(which * 2 + 1, 1);
        right = search(which * 2 + 2, 1);
        if (left >= 0 && right >= 0 && changes > left + right) changes = left + right;
    }
    return changes;
}

int main(int argc, char **argv)
{
    int NNNNN;
    cin >> NNNNN;
    for (int cccccc=1;cccccc<=NNNNN;++cccccc)
    {
        cout << "Case #" << cccccc << ": ";
        
        // CODE
        memset(list, -1, sizeof(list));
        cin >> M >> V;
        for (int i=0;i<(M-1)/2;++i)
        {
            cin >> gate[i] >> change[i];
        }
        for (int i=(M-1)/2;i<M;++i)
        {
            cin >> gate[i];
        }
        int ans = search(0, V);
        if (ans == 10000000) cout << "IMPOSSIBLE" << endl; else cout << ans << endl;
        // END OF CODE
    }
    return 0;
}