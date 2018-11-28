#include <vector>
#include <map>
#include <set>
#include <climits>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define For(i,a,b) for (int i=(a); i<(b); i++)
#define Rep(i,n) For((i),0,(n))
#define Fore(it,x) for (typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define Clear(x,with) memset((x), (with), sizeof((x)))
#define sz size()
typedef long long ll;

const int north[2] = {0, -1};
const int west[2] = {-1, 0};    
int r;
bool dat[107][107], ai[107][107];
bool flag;

void init()
{
     cin >> r;
     flag = false;
     for (int i=0; i<107; i++)
          Clear(dat[i], 0);
     for (int k=0; k<r; k++)
     {
          flag = true;
          int x1, x2, y1, y2;
          cin >> x1 >> y1 >> x2 >> y2;
          for (int i=x1; i<=x2; i++)
               for (int j=y1; j<=y2; j++)
                    dat[i][j] = true;
     }
}

int calc()
{
     int t = 0;
     while (flag)
     {
          for (int i=0; i<107; i++)
               memcpy(ai[i], dat[i], sizeof(ai[i]));
          for (int i=1; i<=100; i++)
          {
               for (int j=0; j<=100; j++)
               {
                    int wx, wy, nx, ny;
                    nx = i + north[0], ny = j + north[1];
                    wx = i + west[0], wy = j + west[1];
                    if (ai[i][j] && !ai[nx][ny] && !ai[wx][wy])
                         dat[i][j] = false;
                    if (!ai[i][j] && ai[nx][ny] && ai[wx][wy])
                         dat[i][j] = true;
               }
          }
          flag = false;
          for (int i=1; i<=100; i++)
          {
               for (int j=1; j<=100; j++)
               {
                    if (dat[i][j])
                         flag = true;
                    // if (dat[i][j])
                    //      cout << 1;
                    // else
                    //      cout << 0;
               }
               // cout << endl;
          }
          // cout << endl  << endl;
          t++;
     }
     return t;
}

int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     for (int i=1; i<=t; i++)
     {
          init();
          cout << "Case #" << i << ": " << calc() << endl;
     }
     return 0;
}
