#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 10010;

VS s;
string ch;
int num, err_num;
int n;
int L[maxn], R[maxn], err[maxn];
int L1[maxn], R1[maxn], err1[maxn];

bool pred(const int& i, const int& j)
{
   for (int pos = 0; pos < 26; pos++) {
      for (int k = 0; k < s[i].length(); k++) {
         bool a = s[i][k] == ch[pos];
         bool b = s[j][k] == ch[pos];
         if (a && !b) return true;
         if (!a && b) return false;
      }
   }
   return false;
}

int same_signature(int i, int j, char c)
{
   for (int k = 0; k < s[i].length(); k++) {
      bool a = s[i][k] == c;
      bool b = s[j][k] == c;
      if (a != b) return 0;
   }
   return 1;
}

int have(int i, char c)
{
   for (int k = 0; k < s[i].length(); k++) {
      if (s[i][k] == c) return 1;
   }
   return 0;
}

void solve1(VI &a)
{
   int n = a.size();
   sort(a.begin(), a.end(), pred);
   int sz = 1;
   L[0] = 0; R[0] = n-1; err[0] = 0;
   for (int pos = 0; pos < 26; pos++) {
      int sz1 = 0;
      for (int piece = 0; piece < sz; piece++) {
         int last = L[piece]-1;
         for (int j = L[piece]+1; j <= R[piece]; j++) {
            if (!same_signature(a[j-1], a[j], ch[pos])) {
               L1[sz1] = last+1;
               R1[sz1] = j-1;
               err1[sz1] = err[piece];
               last = j-1;
               sz1++;
            }
         }
         L1[sz1] = last+1;
         R1[sz1] = R[piece];
         err1[sz1] = err[piece];
         if (!have(a[R[piece]], ch[pos]) && last >= L[piece])
            err1[sz1]++;
         sz1++;
      }
      sz = sz1;
      memcpy(L, L1, sizeof(L));
      memcpy(R, R1, sizeof(R));
      memcpy(err, err1, sizeof(err));
   }
   num = a[0];
   err_num = err[0];
   for (int i = 1; i < n; i++) {
      if (err[i] > err_num || (err[i] == err_num && a[i] < num)) {
         err_num = err[i];
         num = a[i];
      }
   }
}

string solve()
{
   VI by_len;
   int best_err_num = -1, best_num = 0;
   string best;
   for (int len = 1; len <= 10; len++) {
      int cnt = 0;
      for (int i = 0; i < n; i++) {
         if (s[i].length() == len) cnt++;
      }
      by_len.resize(cnt);
      cnt = 0;
      for (int i = 0; i < n; i++) {
         if (s[i].length() == len) {
            by_len[cnt] = i;
            cnt++;
         }
      }
      if (by_len.size()) {
         solve1(by_len);
         if (err_num > best_err_num || (err_num == best_err_num && num < best_num)) {
            best_err_num = err_num;
            best_num = num;
         }
      }
   }
   return s[best_num];
}

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      int i, m;
      cin >> n >> m;
      s.resize(n);
      ch.resize(m);
      for (i = 0; i < n; i++) {
         cin >> s[i];
      }
      cout << "Case #" << sc+1 << ": ";
      
      for (i = 0; i < m; i++) {
         cin >> ch;
         cout << solve() << " ";
      }
      
      cout << endl;
   }
   
   /*cout << "10000 100" << endl;
   for (int i = 0; i < 10000; i++) {
      cout << "zzzzzzzzzz" << endl;
   }
   for (int i = 0; i < 100; i++) {
      cout << "abcdefghijklmnopqrstuvwxyz" << endl;
   }*/

   fclose(stdin); fclose(stdout);
   return 0;   
}
