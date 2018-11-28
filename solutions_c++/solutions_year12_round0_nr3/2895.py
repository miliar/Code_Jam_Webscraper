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

int A, B;
vi List[2000001];
int main() {
  int i, j, total_cases, case_num = 0;
  int mul = 1;
  for (i = 1; i <= 2000000; i++) {
    int x = i;
    if (i >= mul * 10) mul *= 10;
    while (1) {
      x = x / 10 + mul * (x % 10);
      if (x == i) break;
      if (x >= mul && x < i) List[i].pb(x);
    }
  }
  cin >> total_cases;
  while (case_num++ < total_cases) {
    cin >> A >> B;
    int res = 0;
    for (i = A; i <= B; i++) {
      fr (j, SZ(List[i])) if (List[i][j] >= A) res++; 
    }
    cout << "Case #" << case_num << ": " << res << endl;
  }
  return 0;
}
