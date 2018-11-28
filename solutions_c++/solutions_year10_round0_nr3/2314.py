#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
#define vsort(v) sort((v).begin(), (v).end());
#define vrsort(v) sort((v).begin(), (v).end(), greater<int>());
#define loop(n) for (int i=0;i<n;i++)
#define vforeach(i,v) for (i=0;i<(int)(v).size();i++)
#define forspan(i,s,e) for (i=s;i<e;i++)

void
solve(int num)
{
  int R, k, N;
  vi g, G, GN, GP;
  unsigned long long n, ans;
  int pos, p;
  int i, j;

  cin >> R >> k >> N;
  g.resize(N);
  GN.resize(N);
  GP.resize(N);
  forspan (i, 0, N) {
    cin >> g[i];
  }

  ans = 0;
  pos = p = 0;
  forspan (i, 0, R) {
    if (GN[pos]) {
      ans += GN[pos];
      pos = GP[pos];
      continue;
    }

    n = 0;  // temp ans
    forspan (j, 0, N) {
      if (n + g[p] > k) {
        j = N;
        break;
      }
      n += g[p];

      // next
      p++;
      if (p >= N) {
        p = 0;
      }
    }
    if (j == N) {
      ans += n;
      GN[pos] = n;  // cache
      GP[pos] = p;  // next pos
      pos = p;
    }
  }

  cout << "Case #" << num << ": ";
  cout << ans;
  cout << endl;

//  forspan (i, 0, N) {
//    cout << g[i] << " ";
//  }
//  cout << endl;
}

int
main()
{
  int N, i;

  cin >> N;
  for (i = 0; i < N; i++) {
    solve(i + 1);
  }
}

