#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <queue>
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

const int z = 101;
const int inf = 1000000000;

int i, j, k, l, n, m, t, res, fa, fb, tr, ha, hb;
pair<int, int> ta[z], tb[z];
string s;
vector< P > v;  
priority_queue<int> s1, s2;

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
        s1.push(-inf);
      s2.push(-inf);
     scanf("%d\n", &t);
   f(tst, t) {
       scanf("%d\n", &tr);
       scanf("%d%d\n", &ha, &hb);
     f(i, ha) {
        getline(cin, s);
           ta[i].first=((s[0]-48)*10+s[1]-48)*60+(s[3]-48)*10+s[4]-48;
           ta[i].second=((s[6]-48)*10+s[7]-48)*60+(s[9]-48)*10+s[10]-48;
     }
     f(i, hb) {
        getline(cin, s);
           tb[i].first=((s[0]-48)*10+s[1]-48)*60+(s[3]-48)*10+s[4]-48;
           tb[i].second=((s[6]-48)*10+s[7]-48)*60+(s[9]-48)*10+s[10]-48;
     }
         tb[hb].first=inf;
         ta[ha].first=inf;
      sort(ta, ta+ha); fa=0;
      sort(tb, tb+hb); fb=0;
   while (s1.top()!=-inf) s1.pop();
   while (s2.top()!=-inf) s2.pop();
     i=0; j=0;
    while (i<ha || j<hb) {
       if (ta[i].first<tb[j].first || j==hb) {
         if (s1.top()>=-ta[i].first) s1.pop(); else fa++;
             s2.push(-ta[i].second-tr);
          i++;
       } else {
         if (s2.top()>=-tb[j].first) s2.pop(); else fb++;
             s1.push(-tb[j].second-tr);
          j++;
       }
    }
       printf("Case #%d: %d %d\n", tst+1, fa, fb);
   }         
       return 0;
} 
