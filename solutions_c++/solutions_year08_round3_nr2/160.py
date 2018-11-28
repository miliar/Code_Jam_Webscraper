#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;

const int NOTHING = 0;
const int PLUS = 1;
const int MINUS = 2;

bool ugly(long long n)
{
  return (n / 2 * 2 == n || n / 3 * 3 == n || n / 5 * 5 == n || n / 7 * 7 == n);
}

long long eval(string t, int pn)
{
  long long n = 0;
  int f = 1;
  long long d = t[0]-'0';
  for (int i = 0; i < t.size()-1; i++) {
    if (pn % 3 == NOTHING) {
      d = d * 10 + t[i+1]-'0';
    }
    else if (pn % 3 == PLUS) {
      //cout << d << "+";
      n += d * f;
      d = t[i+1]-'0';
      f = 1;
    }
    else {
      //cout << d << "-";
      n += d * f;
      d = t[i+1]-'0';
      f = -1;
    }
    pn /= 3;
  }

  //cout << d << "=" << n + d * f << endl;

  return n + d * f;
}

int main()
{
  int N;
  cin >> N;
  for (int a = 1; a <= N; a++) {
    string t;
    cin >> t;
    int n = 1;
    for (int i = 0; i < t.size()-1; i++) {
      n *= 3;
    }

    long long ans = 0;
    for (int i = 0; i < n; i++) {
      //cout << ":" << t << "," << i << "->";
      ans += (ugly(eval(t, i)) == true);
    }

    cout << "Case #" << a << ": " << ans << endl;
  }

  return 0;
}
