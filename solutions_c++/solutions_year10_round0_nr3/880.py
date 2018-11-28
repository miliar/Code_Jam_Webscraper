#include <iostream>
#include <algorithm>
#include <vector>
#define fr(i,N) for(i = 0; i <(int)N; i++)
#define SZ(u) ((int)u.size())

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vll;

int main() {
  int t, R, K, N, T;
  int i, j;
  ll sum;
  cin >> T;

  fr (t, T) {
    cin >> R >> K >> N;
    cout << "Case #" << t+1 << ": ";

    vi List = vi(N, 0);
    vi Visit = vi(N, -1);
    vll Money = vll(N, 0);

    sum = 0;
    fr (j, N) {
      cin >> List[j];
      sum += List[j];
    }

    if (sum <= K) {
      cout << sum * R << endl;
      continue;
    }

    int now = 0;
    ll res = 0;
    bool flag = false;
    fr (j, R) {
      if (!flag && Visit[now] != -1) {
        res +=  ((R - j) / (j - Visit[now])) * (res - Money[now]);
        j += ((R - j) / (j-Visit[now])) * (j - Visit[now]);
        flag = true;
        if (j == R) continue;
      }

      Money[now] = res;
      Visit[now] = j;
      
      ll temp = 0;
      while (temp + List[now] <= K) {
        temp += List[now];
        now = (now + 1) % N;
      }

      res += temp;
    }

    cout << res << endl;
  }

  return 0;
}
