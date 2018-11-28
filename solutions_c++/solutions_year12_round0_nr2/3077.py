// Problem B. Dancing With the Googlers.cpp : Defines the entry point for the console application.
//

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define forab(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
// need declare it for vc, vc can not use <typeof> keyword
#define foreach(it,c) for(it = c.begin(); it != c.end(); ++it)

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define zero(a) memset(a, 0, sizeof(a))

#define pb push_back
#define mp make_pair

int t;

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

 // freopen("B-small-attempt0.in", "r", stdin);
 // freopen("B-small-attempt0.out", "w", stdout);

  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

  cin >> t;
  for (int cc = 1; cc <= t; cc++) {
    int n, s, p;
    cin >> n >> s >> p;
    vector<int> scores;
    int tmp;
    for (int i = 0; i < n; i++) {
      cin >> tmp;
      scores.push_back(tmp);
    }

    int answer = 0;
    int surprising_maybe = 0;
    sort(scores.begin(), scores.end(), greater<int>());
    if (p == 0) {
      answer = n;
    } else {
      for (int i = 0; i < n; i++) {
        if (scores[i] >= 3 * p - 2)
          answer++;
        else if (scores[i] >= 3 * p - 4 && scores[i] <= 3 * p - 3)
          surprising_maybe++;
      }
      if (p == 1) surprising_maybe = 0;
      answer += min(surprising_maybe, s);
    }
    cout << "Case #" << cc << ": " << answer << endl;
  }
  return 0;
}
