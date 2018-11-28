#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <bitset>
#include <vector>
#include <deque>
#include <utility>
#include <list>
#include <sstream>
#include <iostream>
#include <functional>
#include <fstream>
#include <numeric>
#include <algorithm>

using namespace std;

//Prepared for TopCoder and Codeforces

#define EP 1E-10
#define CLR(arr, v) memset(arr, v, sizeof(arr))
#define SQ(a)       ((a)*(a))
#define DEBUG(a)    printf("%s = %s\n", #a, toStr(a).c_str())
#define FOR(i,s,e)  for( int (i)=(s); (i) < (e) ; i++)
#define SIZE(X)     ((int)(X.size()))
#define LENGTH(X)   ((int)(X.length()))
#define two(X)      (1<<(X))
#define twoL(X)     (((int64)(1))<<(X))

typedef long long ll;
typedef unsigned long long ull;
const   double PI = acos(-1.0);
int     toInt(string s)   {int r=0; istringstream sin(s); sin>>r; return r;}
ll      toInt64(string s) {ll r=0; istringstream sin(s); sin>>r; return r;}
double  toDouble(string s){double r=0; istringstream sin(s); sin>>r; return r;}
double  dist(double x1, double y1, double x2, double y2){return sqrt(SQ(x1-x2)+SQ(y1-y2));}
bool isUpperCase(char c){return c >= 'A' && c <= 'Z';}
bool isLowerCase(char c){return c >= 'a' && c <= 'z';}
bool isLetter(char c)   {return c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z';}
bool isDigit(char c)    {return c >= '0' && c <= '9';}
char toLowerCase(char c){return (isUpperCase(c))?(c + 32) : c;}
char toUpperCase(char c){return (isLowerCase(c))?(c - 32) : c;}

template<class T> inline T strTo(string s){istringstream is(s);T v;is>>v;return v;}
template<class T> inline string toStr(const T& v){ostringstream os;os<<v;return os.str();}
template<class T> inline int cMin(T& a, const T& b){return b<a?a=b,1:0;}
template<class T> inline int cMax(T& a, const T& b){return a<b?a=b,1:0;}
template<class T> inline int cBit(T n){return n?cBit(n&(n-1))+1:0;}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline T GCD(T a, T b)
  {if(a<0)return GCD(-a,b);if(b<0)return GCD(a,-b);return (b==0)?a:GCD(b,a%b);}
template<class T> inline T LCM(T a, T b)
  {if(a<0)return LCM(-a,b);if(b<0)return LCM(a,-b);return a*(b/gcd(a,b));}



string s[4];

bool is(char c)
{
        int x, t;

        for (int i = 0; i < 4; i++)
        {
                x = t = 0;

                for (int j = 0; j < 4; j++)
                {
                        if (s[i][j] == c)
                        {
                               x++;

                        }
                        else if (s[i][j] == 'T')
                                t++;
                }
                if (x == 4 || (x == 3 && t == 1))
                        return 1;

                x = t = 0;

                for (int j = 0; j < 4; j++)
                {
                        if (s[j][i] == c)
                        {
                               x++;

                        }
                        else if (s[j][i] == 'T')
                                t++;
                }
                if (x == 4 || (x == 3 && t == 1))
                        return 1;
        }

        x = t = 0;

        for (int j = 0; j < 4; j++)
        {
                if (s[j][j] == c)
                {
                        x++;
                }
                else if (s[j][j] == 'T')
                        t++;
        }
        if (x == 4 || (x == 3 && t == 1))
                return 1;

        x = t = 0;

        for (int j = 0; j < 4; j++)
        {
                if (s[j][3 - j] == c)
                {
                        x++;
                }
                else if (s[j][3 - j] == 'T')
                        t++;
        }

        if (x == 4 || (x == 3 && t == 1))
                return 1;

        return 0;
}

bool isfu()
{
        for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; ++j)
                        if (s[i][j] == '.')
                                return 0;
        return 1;
}

int main()
{


        int t;

        ifstream cin("A-large.in");
        ofstream cout("b.txt");

        cin >> t;

        int c = 1;

        while (t--)
        {
                for (int i = 0; i < 4; i++)
                        cin >> s[i];

                cout << "Case #" << c++ << ": ";

                if (is('O'))
                {
                        cout << "O won" << endl;
                }
                else if (is('X'))
                {
                        cout << "X won" << endl;
                }
                else if (isfu())
                {
                        cout << "Draw" << endl;
                }
                else cout << "Game has not completed" << endl;
        }

        return 0;
}
