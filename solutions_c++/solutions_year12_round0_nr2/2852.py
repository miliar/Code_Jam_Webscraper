#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;

int N, S, P, T[100];
int main() {
  int i, total_cases, case_num = 0;
  cin >> total_cases;
  while (case_num++ < total_cases) {
    cin >> N >> S >> P;
    int ans = 0;
    fr (i, N) {
      cin >> T[i];
      if (max(0, (P - 1)) * 2 + P <= T[i]) ans++;
      else if (S > 0 && max(0, (P - 2)) * 2 + P <= T[i]) {
        S--;
        ans++;
      }
    }

    cout << "Case #" << case_num << ": " << ans << endl;
  }
  
  return 0;
}
