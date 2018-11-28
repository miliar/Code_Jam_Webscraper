#include<iostream>
#include<cassert>
#include<algorithm>
using namespace std;

struct node{
  bool a;
  int s;
  int t;
  bool operator<(const node &b) const {
    if (s != b.s) return s < b.s;
    if (t != b.t) return t < b.t;
    return a < b.a;
  }
};

int convert(string s) {
  assert(s[2] == ':' && s.length() == 5);
  s.erase(2, 1);
  int ret = 0;
  for (int i = 0; i < 4; i++) {
    ret = ret * 10 + s[i] - '0';
  }
  return ret;
}

int main() {
  int cases, q, n1, n2, n, t, i;
  string s;
  node a[250];
  bool used[250];
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    cin >> t;
    cin >> n1 >> n2;
    n = n1+n2;
    for (i = 0; i < n1; i++) {
      a[i].a = true;
      cin >> s;
      a[i].s = convert(s);
      cin >> s;
      a[i].t = convert(s);
    }
    for (i = n1; i < n; i++) {
      a[i].a = false;
      cin >> s;
      a[i].s = convert(s);
      cin >> s;
      a[i].t = convert(s);
    }
    sort(a, a+n);

    int ans1, ans2, nused, tlast;
    bool last;

    ans1 = ans2 = 0;
    nused = 0;
    memset(used, 0, sizeof(used));
    while (nused < n) {
      for (i = 0; i < n; i++) if (! used[i]) break;
      used[i] = true;
      nused++;
      last = a[i].a;
      tlast = a[i].t + t;
      if (last) ans1++;
      else ans2++;
      
      for ( ; i < n; i++) {
	if ( (! used[i]) && last != a[i].a && tlast <= a[i].s) {
	  used[i] = true;
	  nused++;
	  last = a[i].a;
	  tlast = a[i].t + t;
	}
      }
    }
    printf("Case #%d: %d %d\n", q, ans1, ans2);
  }
  return 0;
}
