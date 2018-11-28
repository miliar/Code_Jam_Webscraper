#include <vector>        
#include <map>        
#include <set>        
#include <deque>        
#include <algorithm>        
#include <utility>        
#include <sstream>        
#include <iostream>        
#include <cstdio>        
#include <cmath>        
#include <cstdlib> 
#include <string>
#include <time.h>

using namespace std;   

#define SZ(a) ((int)(a).size())   
#define pii pair<int, int>  
#define mp make_pair  
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}

struct cell
{
    int alt, label;
};
int ii[4] = {-1, 0, 0,+1};
int jj[4] = { 0,-1,+1, 0};

cell a[100][100];
int maxLabel, H, W;
int fill(int i, int j)
{
    int m[4] = {100000, 100000, 100000, 100000};

    if (i-1 >= 0) m[0] = a[i-1][j].alt;
    if (j-1 >= 0) m[1] = a[i][j-1].alt;
    if (j+1 < W) m[2] = a[i][j+1].alt;
    if (i+1 < H) m[3] = a[i+1][j].alt;
    
    int mmin = min(m[0], min(m[1], min(m[2], m[3])));
    if (mmin >= a[i][j].alt)
    {
        if (!a[i][j].label)
        {
            ++maxLabel;
            a[i][j].label = maxLabel;
        }
        return a[i][j].label;
    }
    for (int k = 0; k < 4; ++k)
        if (m[k] == mmin)
        {
            a[i][j].label = fill(i+ii[k], j+jj[k]);
            break;
        }
    return a[i][j].label;
}
int main()
{
    int testCnt;
    cin >> testCnt;
    for (int T = 0; T < testCnt; ++T)
    {
        cin >> H >> W;
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                cin >> a[i][j].alt;
                a[i][j].label = 0;
            }
        }
        maxLabel = 0;
        for (int i = 0; i < 100; ++i) labels[i] = 0;
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                if (a[i][j].label) continue;
                fill(i, j);
            }
        }
        cout << "Case #" << T+1 << ":" << endl;
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                if (j > 0) cout << " ";
                cout << char('a' + a[i][j].label - 1);
            }
            cout << endl;
        }

    }
    return 0;
}