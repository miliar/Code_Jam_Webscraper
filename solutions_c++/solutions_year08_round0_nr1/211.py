#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>

using namespace std;

#define W while
#define all(v) v.begin(), v.end()
#define sz(v) int((v).size())
#define pb push_back
#define mp make_pair
#define md 100000007
#define P pair<int, int>
#define ll long long
#define vi vector <int>
#define vs vector <string>
#define f(i, n) for(int i=0; i<(n); i++)
#define F(i, n, m) for(int i=(n); i<=(m); i++)
#define d(i, n) for(int i=(n)-1; i>=0; i--)
#define D(i, n, m) for(int i=(n); i>=(m); i--)

const int z = 1001;

int i, j, k, l, n, m, t, res;
string e[z], q[z]; 
vector< P > v;

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
     scanf("%d\n", &t);
   f(tst, t) {
      scanf("%d\n", &n);
     f(i, n) getline(cin, e[i]);
      scanf("%d\n", &m);
     f(i, m) getline(cin, q[i]);
      res=0;
        i=0;
     W (i<m) {
           k=i;
       f(u, n) {
           j=i;
          while (j<m && q[j]!=e[u]) j++;
           if (k<j) k=j;
       }
          res+=(k<m); i=k;
     }
       printf("Case #%d: %d\n", tst+1, res);
   }
       return 0;
}
