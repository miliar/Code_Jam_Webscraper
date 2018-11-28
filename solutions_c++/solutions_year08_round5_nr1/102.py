#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cassert>
using namespace std;

typedef long long lint;

const int INF = 0x3f3f3f3f;

const int N = 3010*2;
const int O = 3005;

char a[N][N];
bool b[N][N];

int main()
{
    //freopen("A.in", "r", stdin);
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; ++cs)
    {
        int L;
        scanf("%d", &L);
        string path;
        for (int i = 0; i < L; ++i)
        {
            char s[64];
            int t;
            scanf(" %s %d", s, &t);
            string str(s);
            while (t -- > 0)
            {
                path += str;
            }
        }
    
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        int x = 0, y = 0, dir = 0;
        for (int i = 0; i < path.size(); ++i)
        {
            if (path[i] == 'F')
            {
                if (dir == 0) { a[x + O][y + O] |= 1; y++;}
                else if (dir == 1) { a[x + O][y + O] |= 2; x++;}
                else if (dir == 2) { y--; a[x + O][y + O] |= 1;}
                else if (dir == 3) { x--; a[x + O][y + O] |= 2;}
            }
            else if (path[i] == 'R') dir = (dir + 1) & 3;
            else dir = (dir + 3) & 3;
        }
        assert(x == 0 && y == 0);
        int res = 0;
        for (x = -3001; x <= 3001; ++x)
        {
            int upper = 3001; while (upper >= -3001 && (a[x + O][upper + O] & 2) == 0) upper--;
            int lower = -3001; while (lower <= 3001 && (a[x + O][lower + O] & 2) == 0) lower++;
            bool outside = true;
            while (lower < upper)
            {
                if (a[x + O][lower + O] & 2) outside = ! outside;
                if (outside) 
                { 
                    b[x + O][lower + O] = true; res++;
                }
                lower++;
            }
        }

        for (y = -3001; y <= 3001; ++y)
        {
            int upper = 3001; while (upper >= -3001 && (a[upper + O][y + O] & 1) == 0) upper--;
            int lower = -3001; while (lower <= 3001 && (a[lower + O][y + O] & 1) == 0) lower++;
            bool outside = true;
            while (lower < upper)
            {
                if (a[lower + O][y + O] & 1) outside = ! outside;
                if (outside && !b[lower + O][y + O]) 
                { 
                    res++;
                }
                lower++;
            }
        }
        
        printf("Case #%d: %d\n", cs, res);
    }
    return 0;
}
