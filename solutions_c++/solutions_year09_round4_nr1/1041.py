#include <iterator>
#include <vector>
#include <list>
#include <map>
#include <set>
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
const int maxn = 49;
int n;
vi a;
void init()
{
     char s[100];
     cin >> n;
     a.clear();
     a.reserve(n);
     Rep (i, n)
     {
          a.pb(-1);
          cin >> s;
          Rep (j, n)
               if (s[j] == '1')
                    a[i] = j;
     }
}
int calc()
{
     // copy(a.begin(), a.begin()+n, ostream_iterator<int>(cout, " "));
     // cout << endl;
     int ans = 0;
     Rep (i, n)
     {
          int idx;
          For (j, i, n)
          {
               if (a[j] <= i)
               {
                    idx = j;
                    break;
               }
          }
          ans += idx - i;
          int tmp = a[idx];
          for (int j=idx; j>i; j--)
               a[j] = a[j-1];
          a[i] = tmp;
     }
     // copy(a.begin(), a.begin()+n, ostream_iterator<int>(cout, " "));
     // cout << endl;
     return ans;
}
int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     Rep (i, t)
     {
          init();
          cout << "Case #" << i+1 << ": " << calc() << endl;
     }
     return 0;
}

