#include <iostream>
#include <string>
#include <cassert>
using namespace std;

char a[10];
char b[10];
int S;

// incrementa di uno la stringa decimale
void next(char *x) {
  int i;
  for (i=S-1;x[i]=='9';--i);
  assert(i>=0);
  x[i]++;
  for(i++;i<S;++i)
    x[i]='0';
}

void cycle_left(char *x) {
  char l=x[0];
  int i;
  for (i=0;i<S-1;++i)
    x[i]=x[i+1];
  x[i]=l;
}

void copy(char *y, const char *x) {
  const char *e=y+S;
  for (;y<e;++y,++x)
    *y = *x;
}

int cmp(const char *x, const char *y) {
  const char *e = x+S;
  for(;x<e;++x,++y) {
    if (*x < *y)
      return -1;
    if (*x > *y)
      return 1;
  }
  return 0;
}

int count(const char *x) {
  static char y[10];
  y[S]=0;
  copy(y,x);
  cycle_left(y);
  int r = 0;
  int eq = 0;
  for (int i=1;i<S;++i,cycle_left(y)) {
    int c = cmp(y,x);
    if (c==1) {
      c = cmp(y,b);
      if (c<=0)
	r++;
    } else if (c==0)
      eq++;
  }
  if (eq>0) {
    if (r % (eq+1) != 0) {
      cerr << "a="<<a<<", b="<<b<<" S="<<S<<endl;
      cerr << "x="<<x<<" r="<<r<<" eq="<<eq<<endl;
    }
    assert(r % (eq+1) == 0);
    r /= eq+1;
  }
  return r;
}

int solve() {
  int r = 0;
  char x[10];
  x[S]=0;
  for (copy(x,a); cmp(x,b) == -1; next(x)) {
    // cerr<<"x="<<x<<endl;
    r += count(x);
  }
  return r;
}

int main() {
  int T;
  cin >> T;
  for (int X=1; X<= T; X++) {
    string sa,sb;
    cin >> sa >> sb;
    S=sa.size();
    assert(S == sb.size());
    a[S]=0; b[S]=0;
    copy(a,sa.c_str());
    copy(b,sb.c_str());
    cout << "Case #" << X << ": " << solve() << endl;
  }
  return 0;
}
