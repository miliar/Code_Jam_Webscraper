#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 1001;
class Num {
  public:
    Num() {
      vn=1;
      v[0] = 0;
    }
    Num(const Num &num) {
      vn = num.vn;
      for (int i=0; i<vn; ++i) {
        v[i] = num.v[i];
      }
      v[vn] = 0;
    }
    void scanf() {
      ::scanf("%s",v);
      for (vn=0; v[vn]; ++vn) {
        v[vn] -= '0';
      }
    }
    void printf() const {
      Num p(*this);
      for (int i=0; i<vn; ++i) {
        p.v[i] += '0';
      }
      ::printf("%s",p.v);
    }
    inline bool operator<(const Num& num) const {
      if (vn < num.vn) return true;
      if (vn > num.vn) return false;
      for (int i=0; i<vn; ++i) {
        if (v[i] < num.v[i]) return true;
        if (v[i] > num.v[i]) return false;
      }
      return false;
    }
    inline bool operator==(const Num& num) const {
      if (vn != num.vn) return false;
      for (int i=0; i<vn; ++i) {
        if (v[i] != num.v[i]) return false;
      }
      return true;
    }
    inline bool operator<=(const Num& num) const {
      return (operator<(num) || operator==(num));
    }
    inline void clean() {
      for (int i=vn-1; i>=0;--i) {
        if (v[i] < 0) {
          v[i] += 10;
          --v[i-1];
        }
      }
      int t = 0;
      for (; t<vn && v[t]==0; ++t) ;
      if (t == vn) {
        vn = 1;
        v[0] = 0;
      } else if (t>0) {
        for (int i=t; i<vn; ++i) {
          v[i-t] = v[i];
        }
        vn -= t;
        v[vn] = 0;
      }
    }
    inline Num operator-(const Num& num) const {
      int k=vn-num.vn;
      Num ret;
      ret.vn = vn;
      for (int i=0; i<k; ++i) ret.v[i] = v[i];
      for (int i=k; i<vn; ++i) ret.v[i] = v[i] - num.v[i-k];
      ret.clean();
      return ret;
    }

    inline Num operator%(const Num& num) const {
      Num ret;
      for (int i=0; i<vn; ++i) {
        ret.v[ret.vn] = v[i];
        ret.vn++;
        ret.clean();
        while (num<=ret) {
          Num tmp = ret - num;
          ret = tmp;
        }
      }
      return ret;
    }
    inline bool operator==(int x) const {
      if (vn > 8) return false;
      int y = 0;
      for (int i=0; i<vn; ++i) {
        y *= 10;
        y += v[i];
      }
      return (x==y);
    }
  private:
    char v[100];
    int vn;
};
Num t[N];

Num gcd(const Num &a,const Num &b) {
  if (b < a) return gcd(b,a);
  if (a == 0) return b;
  return gcd (b%a,a);
}

int main() {
  int c,n;
  Num d;
  scanf("%d",&c);
  for (int i=1; i<=c; ++i) {
    scanf("%d",&n);
    for (int j=0; j<n; ++j) {
      t[j].scanf();
    }
    d = max(t[0],t[1])-min(t[0],t[1]);
    for (int j=2; j<n; ++j) {
        d = gcd(d,max(t[j],t[j-1])-min(t[j],t[j-1]));
    }
    printf("Case #%d: ",i);
    Num ret = (d-(t[0]%d))%d;
    ret.clean();
    ret.printf();
    printf("\n");
  }
  return 0;
}
