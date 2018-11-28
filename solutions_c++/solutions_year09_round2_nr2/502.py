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

string str;

int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     Rep (i, t)
     {
          cin >> str;
          cout << "Case #" << i+1 << ": ";
          if (next_permutation(str.begin()+1, str.end()))
              cout << str << endl;
          else
          {
               bool flag = false;
               Fore (it, str)
               {
                    if (*it > str[0])
                    {
                         swap(*it, str[0]);
                         flag = true;
                         break;
                    }
               }
               if (flag)
               {
                    sort(str.begin()+1, str.end());
                    cout << str << endl;
               }
               else
               {
                    string::iterator it = str.begin();
                    Fore (i, str)
                    {
                         if (*i != '0' && *i < *it)
                              it = i;
                    }         
                    swap(*it, str[0]);
                    sort(str.begin()+1, str.end());
                    str.insert(1, "0");
                    cout << str << endl;
               }
          }
     }
     return 0;
}
