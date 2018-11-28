#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <utility>
#include <complex>

using namespace std;

typedef long long LL;
typedef long double LD;

int nTests, test;

// <solution>

const int MAX_R = 510;

int r, c, d;
int w [MAX_R][MAX_R];
LL f [MAX_R][MAX_R];

int k, x, y;
pair<LL, LL> moment;

pair<LL, LL> operator + (pair<LL, LL> a, pair<LL, LL> b)
{
    return make_pair(a.first + b.first, a.second + b.second);
}

pair<LL, LL> operator - (pair<LL, LL> a, pair<LL, LL> b)
{
    return make_pair(a.first - b.first, a.second - b.second);
}

pair<LL, LL> operator * (pair<LL, LL> a, long long w)
{
    return  make_pair(a.first * w, a.second * w);
}

LL calcSum(int x1, int y1, int x2, int y2)
{
    return f[x2][y2] - f[x2][y1 - 1] - f[x1 - 1][y2] + f[x1 - 1][y1 - 1];
}

pair<LL, LL> calcMoment(int x1, int y1, int x2, int y2)
{
    int x0 = 2 * x + k, y0 = 2 * y + k;

    pair<LL, LL> ret(0, 0);
    for (int i = x1; i <= x2; i++)
        for (int j = y1; j <= y2; j++)
            ret = ret + make_pair(2 * i + 1 - x0, 2 * j + 1 - y0) * w[i][j];

    #ifdef DEBUG
    cerr << "calcMoment " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << " returns " << ret.first << ' ' << ret.second << '\n';
    #endif

    return ret;                        
}

void shiftDown()
{
    moment = moment - calcMoment(x, y, x, y + k - 1); //left column leaves us
    moment.first -= 2 * calcSum(x + 1, y, x + k - 1, y + k - 1); //all that stay with us
    x++;
    moment = moment + calcMoment(x + k - 1, y, x + k - 1, y + k - 1); //right column comes to us
}
    
void shiftRight()
{
    moment = moment - calcMoment(x, y, x + k - 1, y);

    #ifdef DEBUG
    cerr << "print " << moment.first << ' ' << moment.second << '\n';
    #endif

    moment.second -= 2 * calcSum(x, y + 1, x + k - 1, y + k - 1);
    y++;

    #ifdef DEBUG
    cerr << "print " << moment.first << ' ' << moment.second << '\n';
    #endif

    moment = moment + calcMoment(x, y + k - 1, x + k - 1, y + k - 1);

    #ifdef DEBUG
    cerr << "print " << moment.first << ' ' << moment.second << '\n';
    #endif
}

void solve()
{
    cerr << "Case " << test << '\n';

    cin >> r >> c >> d;
    for (int i = 1; i <= r; i++)
    {
        string s;
        cin >> s;

        for (int j = 1; j <= c; j++)
            w[i][j] = d + s[j - 1] - '0';
    }

    #ifdef DEBUG
    cerr << "w " << '\n';
    for (int i = 1; i <= r; i++)
    {
        for (int j = 1; j <= c; j++)
            cerr << w[i][j] << ' ';
        cerr << '\n';
    }
    #endif

    memset(f, 0, sizeof(f));
    for (int i = 1; i <= r; i++)
        for (int j = 1; j <= c; j++)
            f[i][j] = f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1] + w[i][j];

    printf("Case #%d: ", test);       
    for (k = min(r, c); k >= 3; k--)
    {
        #ifdef DEBUG
        cerr << "k = " << k << '\n'; 
        #endif

        x = 1, y = 1;
        moment = calcMoment(1, 1, k, k);
        pair<LL, LL> firstMoment = moment;

        for (; x + k - 1 <= r;)
        {
            for (; y  + k - 1 <= c;)
            {
                pair<LL, LL> allMoment = moment - calcMoment(x, y, x, y) - calcMoment(x + k - 1, y, x + k - 1, y) 
                                                - calcMoment(x, y + k - 1, x, y + k - 1) - calcMoment(x + k - 1, y + k - 1, x + k - 1, y + k - 1);                    

                #ifdef DEBUG
                cerr << "x = " << x << " y = " << y << '\n';
                cerr << "moment = " << moment.first << ' ' << moment.second << '\n';
                cerr << "allMoment = " << allMoment.first << ' ' << allMoment.second << '\n';
                #endif

                if (allMoment.first == 0 && allMoment.second == 0)
                {
                    printf("%d\n", k);
                    return;
                }

                shiftRight();
            }

            moment = firstMoment;
            y = 1;
            shiftDown();
            firstMoment = moment;
        }
    }

    printf("IMPOSSIBLE\n");
}

// </solution> 

int main()
{                
    cin >> nTests;
    for (test = 1; test <= nTests; test++)
        solve();
    return 0;
}
