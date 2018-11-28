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
#define For(i,a,b) for (int (i)=(a); (i)<(b); (i)++)
#define Rep(i,n) For((i),0,(n))
#define Fore(it,x) for (typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define Clear(x,with) memset((x), (with), sizeof((x)))
#define sz size()
typedef long long ll;

const int maxn = 100000;
double tree[maxn];
string name[maxn];
int l[maxn], r[maxn];
set<string> dic;
int tot;
string str, tmp, ai;
int pos;
char buffer[maxn*10], temp[1000];

void init(int num)
{
     tot++;
     while (buffer[pos++] != '(');
     sscanf(buffer+pos, "%lf", &tree[num]);
     while (!(islower(buffer[pos]) || buffer[pos] == ')'))
          pos++;
     if (buffer[pos] == ')')
     {
          name[num] = "END";
          l[num] = -1, r[num] = -1;
          pos++;
          return;
     }
     sscanf(buffer+pos, "%s", temp);
     name[num] = temp;
     while (buffer[pos] != '(')
          pos++;
     l[num] = tot;
     init(tot);
     r[num] = tot;
     init(tot);
     while (buffer[pos++] != ')');
}

double calc()
{
     double ans = tree[0];
     int now = 0;
     while (l[now] != -1)
     {
          if (dic.find(name[now]) != dic.end())
               now = l[now];
          else
               now = r[now];
          ans *= tree[now];

     } 
     return ans;
}

int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     Rep (i, t)
     {
          cout << "Case #" << i+1 << ":" << endl;
          Clear(l, -1), Clear(r, -1);
          str.clear();
          pos = 0;
          tot = 0;
          int a, b;
          cin >> a; getchar();
          Rep (i, a)
          {
               getline(cin, tmp);
               str += tmp;
               str += " ";
          }
          strcpy(buffer, str.c_str());
          init(0);
          cin >> a;
          Rep (j, a)
          {
               dic.clear();
               double ans = 0;
               cin >> tmp >> b;
               ans += tree[0];
               Rep (k, b)
               {
                    cin >> ai;
                    dic.insert(ai);
               }
               cout.setf(ios::fixed);
               cout.precision(7);
               cout << calc() << endl;
          }
     }
     return 0;
}
