#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>

using namespace std;

int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

void solve_case();

int main() {
  int T; scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve_case();
  }
}

// The number of bits to use per digit in the integer representation.
static const int BASE_BITS = 30;

// The base of the representation of the integer.
static const int BASE = 1 << BASE_BITS;

class bigint {
public:
  bigint() : s(false) {} // Initializes integer to 0.
  bigint(const bigint &); // Copies the parameter.
  bigint(const string &, int radix = 10); // Initializes to the value given in the string.
  bigint(long long); // Initializes to the passed int.

  bigint & operator=(const bigint &);
  
  // a.compare(b) returns -1 if a < b, 0 if a == b, and 1 if a > b.
  int compare(const bigint &) const;

  // Basic comparision operators.
  bool operator==(const bigint & x) const { return compare(x) == 0; }
  bool operator!=(const bigint & x) const { return compare(x) != 0; }
  bool operator< (const bigint & x) const { return compare(x) < 0; }
  bool operator<=(const bigint & x) const { return compare(x) <= 0; }
  bool operator> (const bigint & x) const { return compare(x) > 0; }
  bool operator>=(const bigint & x) const { return compare(x) >= 0; }
  
  // Takes the absolute value of the integer.
  bigint abs() { bigint r = *this; r.s = false; return r; }
  // Negates the integer.
  bigint & negate() { if(!d.empty()) s = !s; return *this; }
  // Returns *this negated.
  bigint operator-() const { bigint cpy = *this; return cpy.negate(); }

  // Basic scalar arithmetic.  Note that these operators work faster than the
  // bigint equivalent and should be prefered where applicable.
  bigint & operator+=(long long);
  bigint & operator-=(long long);
  bigint & operator*=(long long);
  bigint & operator/=(long long);
  bigint & operator%=(long long x) { *this = bigint(*this % x); }

  bigint operator+(long long x) const { bigint r = *this; r += x; return r; }
  bigint operator-(long long x) const { bigint r = *this; r -= x; return r; }
  bigint operator*(long long x) const { bigint r = *this; r *= x; return r; }
  bigint operator/(long long x) const { bigint r = *this; r /= x; return r; }
  long long operator%(long long) const;

  // Basic integer arithmetic.
  bigint & operator+=(const bigint &);
  bigint & operator-=(const bigint &);
  bigint & operator*=(const bigint & x) { *this = *this * x; return *this; }
  bigint & operator/=(const bigint & x) { *this = *this / x; return *this; }
  bigint & operator%=(const bigint & x) { *this = *this % x; return *this; }

  bigint operator+(const bigint & x) const { bigint r = *this; r += x; return r; }
  bigint operator-(const bigint & x) const { bigint r = *this; r -= x; return r; }
  bigint operator*(const bigint &) const;
  bigint operator/(const bigint &) const;
  bigint operator%(const bigint &) const;

  // Basic binary arithmetic.  All binary operators ignore the sign bit.
  bigint & operator|=(const bigint &);
  bigint & operator&=(const bigint &);
  bigint & operator^=(const bigint &);

  bigint operator|(const bigint & x) const { bigint r = *this; r |= x; return r; }
  bigint operator&(const bigint & x) const { bigint r = *this; r &= x; return r; }
  bigint operator^(const bigint & x) const { bigint r = *this; r ^= x; return r; }

  bigint operator<<(int) const;
  bigint operator>>(int) const;

  // Postfix/Prefix incrementors and decrementors.
  bigint & operator++() { return *this += 1; }
	bigint operator ++(int) { bigint r = *this; *this += 1; return r; }
  bigint & operator--() { return *this -= 1; }
	bigint operator --(int) { bigint r = *this; *this -= 1; return r; }
	
  // Allows for swapping two integers in constant time.
  void swap(bigint & x) { std::swap(s, x.s); d.swap(x.d); }
  // Converts the integer into a base radix string representation.
  string to_string(int radix = 10) const;
  // Returns the length of the integer in bits.
  int bits() const { return d.empty() ? 0 : BASE_BITS * d.size() - __builtin_clz(d.back()) + 32 - BASE_BITS; }

  // Returns true if the xth bit is set.
  bool get_bit(int x) const { if(x >= d.size() * BASE_BITS) return 0; return d[x / BASE_BITS] & 1 << (x % BASE_BITS); }
  // Sets the xth bit to v.
  void set_bit(int x, bool v) { if(x >= d.size() * BASE_BITS) d.resize(x / BASE_BITS + 1); if(v) d[x / BASE_BITS] |= 1 << (x % BASE_BITS); else { d[x / BASE_BITS] &= ~(1 << (x % BASE_BITS)); purge(); } }

  // Converts the integer to an int.
  int to_int() const { int ret = 0; for(int i = (int)d.size() - 1; i >= 0; i--) ret = ret * BASE + d[i]; return ret; }
  // Converts the integer to a long long.
  long long to_long_long() const { long long ret = 0; for(int i = (int)d.size() - 1; i >= 0; i--) ret = ret * BASE + d[i]; return ret; }
  // Converts the integer to a double.
  double to_double() const { double ret = 0; for(int i = (int)d.size() - 1; i >= 0; i--) ret = ret * BASE + d[i]; return ret; }
  // Converts the integer to a long double.
  long double to_long_double() const { long double ret = 0; for(int i = (int)d.size() - 1; i >= 0; i--) ret = ret * BASE + d[i]; return ret; }

  // Computes a random number with the passed number of bits.
  static bigint random(int);
  // Computes a random probable prime number with the passed number of bits.
  static bigint random_prime(int);

  // Computes the floor of the square root of *this.
  bigint sqrt() const;

  // Computes the greatest commond divisor of *this and x.
  bigint gcd(const bigint & x) const;

  // Computes *this^e modulo mod.
  bigint mod_exp(const bigint & e, const bigint & mod) const;

  // Computes x such that *this * x = 1 modulo mod.
  bigint mod_inv(const bigint & mod) const;

  // Returns true if *this is almost certainly prime.
  bool probably_prime() const;

  // Returns 1 if there exists an x such that x^2=*this modulo prime p.
  // Returns 0 if x = 0 modulo prime p.
  // Returns -1 otherwise.
  int legendre(const bigint & p) const;

  // Returns x such that x^2=*this (mod p). The behavior of this function is not
  // defined if legendre(p) is not 1.  This uses the Shanks-Tonelli algorithm.
  bigint mod_square_root(const bigint & p) const;

private:
  // Sign bit.  s = true means the integer is negative.
  bool s;
  // A list of the digits of the integer.  Less significant digits have lower
  // indicies.
  vector<int> d;

  // Helper function to remove undesired trailing 0s.
  void purge();
};

// Stream operator for writing a big integer to a stream.
ostream & operator <<(ostream &, const bigint &);

// Stream operator for reading a big integer in from a stream.
istream & operator >>(istream &, bigint &);

bigint::bigint(const bigint & x) {
  s = x.s;
  d = x.d;
}

bigint::bigint(const string & x, int radix) {
  s = false;
  for(int i = x[0] == '-'; i < x.size(); i++) {
    *this *= radix;
    char ch = tolower(x[i]);
    if(isalpha(ch)) {
      *this += 10 + ch - 'a';
    } else {
      *this += ch - '0';
    }
  }
  s = x[0] == '-';
}

bigint::bigint(long long x) {
  s = 0;
  *this += x;
}

bigint & bigint::operator=(const bigint & x) {
  s = x.s;
  d = x.d;
}

int bigint::compare(const bigint & x) const {
  if(s != x.s) {
    return s ? -1 : 1;
  }
  if(d.size() < x.d.size()) {
    return s ? 1 : -1;
  } else if(x.d.size() < d.size()) {
    return s ? -1 : 1;
  }
  for(int i = (int)d.size() - 1; i >= 0; i--) {
    if(d[i] < x.d[i]) {
      return s ? 1 : -1;
    } else if(x.d[i] < d[i]) {
      return s ? -1 : 1;
    }
  }
  return 0;
}

void bigint::purge() {
  int sz;
  for(sz = d.size(); sz && d[sz - 1] == 0; sz--);
  d.resize(sz);
  if(d.empty()) {
    s = false;
  }
}

bigint & bigint::operator+=(long long x) {
  if(!x) {
    return *this;
  } else if(x == 0x8000000000000000LL) {
    ++x;
    --*this;
  }
  if(x < 0 != s) {
    *this -= -x;
  } else {
    if(x < 0) x = -x;
    int c = 0;
    for(int i = 0; x || c; i++) {
      if(i == d.size()) {
        d.push_back(0);
      }
      d[i] += c + (x & BASE - 1);
      x = x >> BASE_BITS;
      c = d[i] >> BASE_BITS;
      d[i] &= BASE - 1;
    }
    if(c) {
      d.push_back(c);
    }
    purge();
  }
  return *this;
}

bigint & bigint::operator-=(long long x) {
  if(!x) {
    return *this;
  } else if(x == 0x8000000000000000LL) {
    ++x;
    ++*this;
  }
  if(x < 0 != s) {
    *this += -x;
  } else {
    if(x < 0) x = -x;
    for(int i = 0; x || i < d.size() && d[i] < 0; i++) {
      if(i == d.size()) {
        d.push_back(0);
      }
      d[i] -= x & BASE - 1;
      x = x >> BASE_BITS;
      if(d[i] < 0) {
        if(i + 1 == d.size()) {
          if(!x) {
            break;
          } else {
            d.push_back(0);
          }
        }
        d[i] += BASE;
        d[i + 1]--;
      }
    }
    if(d.back() < 0) {
      bool pull = false;
      for(int i = 0; i + 1 < d.size(); i++) {
        if(pull) {
          d[i] = BASE - d[i] - 1;
        } else if(d[i]) {
          d[i] = BASE - d[i];
          pull = true;
        }
      }
      d.back() = -d.back() - pull;
      s = !s;
    }
    purge();
  }
  return *this;
}

bigint & bigint::operator*=(long long x) {
  if(x == 0 || d.empty()) {
    s = false;
    d.resize(0);
    return *this;
  } else if(x <= -2147483648LL || 2147483648LL <= x) {
    return *this *= bigint(x);
  } else if(x < 0) {
    s = !s;
    x = -x;
  }
  int c = 0;
  for(int i = 0; i < d.size() || c; i++) {
    if(i == d.size()) {
      d.push_back(0);
    }
    long long v = 1LL * x * d[i] + c;
    d[i] = v & BASE - 1;
    c = v >> BASE_BITS;
  }
  return *this;
}

bigint & bigint::operator/=(long long x) {
  if(x == 0) {
    throw "bigint::operator/=(int) - divide by 0";
  } else if(d.empty()) {
    return *this;
  } else if(x <= -2147483648LL || 2147483648LL <= x) {
    return *this /= bigint(x);
  } else if(x < 0) {
    s = !s;
    x = -x;
  }
  long long c = 0;
  for(int i = (int)d.size() - 1; i >= 0; i--) {
    long long nc = (c + d[i]) % x;
    d[i] = (c + d[i]) / x;
    c = nc << BASE_BITS;
  }
  purge();
  return *this;
}

long long bigint::operator%(long long x) const {
  if(x < 0) {
    throw "bigint::operator/%(int) - Unexpected negative modulus";
  } else if(x == 0) {
    throw "bigint::operator/%(int) - divide by 0";
  } else if(x <= -2147483648LL || 2147483648LL <= x) {
    return (*this % bigint(x)).to_long_long();
  }
  long long m = 1;
  long long res = 0;
  for(int i = 0; i < d.size(); i++) {
    res = (res + d[i] * m) % x;
    m = (m * BASE) % x;
  }
  return res;
}

bigint & bigint::operator+=(const bigint & x) {
  if(x.d.empty()) {
    return *this;
  }
  if(x.s != s) {
    const_cast<bigint &>(x).negate();
    *this -= x;
    const_cast<bigint &>(x).negate();
  } else {
    if(d.size() < x.d.size()) {
      d.resize(x.d.size());
    }
    int c = 0;
    for(int i = 0; i < d.size(); i++) {
      d[i] += c + (i < x.d.size() ? x.d[i] : 0);
      c = d[i] >> BASE_BITS;
      d[i] &= BASE - 1;
    }
    if(c) {
      d.push_back(c);
    }
  }
  return *this;
}

bigint & bigint::operator-=(const bigint & x) {
  if(x.d.empty()) {
    return *this;
  }
  if(x.s != s) {
    const_cast<bigint &>(x).negate();
    *this += x;
    const_cast<bigint &>(x).negate();
  } else {
    if(d.size() < x.d.size()) {
      d.resize(x.d.size());
    }
    for(int i = 0; i < d.size(); i++) {
      d[i] -= i < x.d.size() ? x.d[i] : 0;
      if(i + 1 < d.size() && d[i] < 0) {
        d[i] += BASE;
        d[i + 1]--;
      }
    }
    if(d.back() < 0) {
      bool pull = false;
      for(int i = 0; i + 1 < d.size(); i++) {
        if(pull) {
          d[i] = BASE - d[i] - 1;
        } else if(d[i]) {
          d[i] = BASE - d[i];
          pull = true;
        }
      }
      d.back() = -d.back() - pull;
      s = !s;
    }
    purge();
  }
  return *this;
}

bigint bigint::operator*(const bigint & x) const {
  if(d.empty() || x.d.empty()) {
    return bigint();
  }
  
  int n = d.size() + x.d.size();
  vector<long long> nd = vector<long long>(n, 0);
  for(int i = 0; i < n; i++) {
    for(int j = max(0, i - (int)x.d.size() + 1); j <= i && j < d.size(); j++) {
      nd[i] += 1LL * d[j] * x.d[i - j];
      nd[i + 1] += nd[i] >> BASE_BITS;
      nd[i] &= BASE - 1;
    }
  }

  while(nd.back() >= BASE) {
    long long nv = nd.back() >> BASE_BITS;
    nd.back() &= BASE - 1;
    nd.push_back(nv);
  }

  bigint ret;
  ret.s = s != x.s;
  ret.d = vector<int>(nd.size(), 0);
  for(int i = 0; i < nd.size(); i++) {
    ret.d[i] = nd[i];
  }
  ret.purge();

  return ret;
}

bigint bigint::operator/(const bigint & x) const {
  if(x.d.empty()) {
    throw "bigint::operator/%(bigint) - divide by 0";
  }
  bigint ret = 0;
  bigint cpy = *this;
  cpy.s = false;
  bool xs = x.s;
  const_cast<bigint &>(x).s = false;
  while(true) {
    int lo = -1;
    int hi = cpy.bits();
    while(lo < hi) {
      int mid = (lo + hi + 1) / 2;
      if((x << mid) <= cpy) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }
    if(lo == -1) {
      break;
    }
    cpy -= x << lo;
    ret += bigint(1) << lo;
  }
  const_cast<bigint &>(x).s = xs;
  if(!ret.d.empty()) {
    ret.s = s != x.s;
  }
  return ret;
}

bigint bigint::operator%(const bigint & x) const {
  if(x < 0) {
    throw "bigint::operator/%(bigint) - Unexpected negative modulus";
  } else if(x.d.empty()) {
    throw "bigint::operator/%(bigint) - divide by 0";
  }
  bigint cpy = *this;
  cpy.s = x.s;
  while(true) {
    int lo = -1;
    int hi = cpy.bits();
    while(lo < hi) {
      int mid = (lo + hi + 1) / 2;
      if((x << mid) <= cpy) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }
    if(lo == -1) {
      return cpy;
    }
    cpy -= x << lo;
  }
  return bigint();
}

bigint & bigint::operator|=(const bigint & x) {
  if(d.size() < x.d.size()) {
    d.resize(x.d.size());
  }
  for(int i = 0; i < x.d.size(); i++) {
    d[i] |= x.d[i];
  }
  return *this;
}

bigint & bigint::operator&=(const bigint & x) {
  if(x.d.size() < d.size()) {
    d.resize(x.d.size());
  }
  for(int i = 0; i < x.d.size(); i++) {
    d[i] &= x.d[i];
  }
  purge();
  return *this;
}

bigint & bigint::operator^=(const bigint & x) {
  if(d.size() < x.d.size()) {
    d.resize(x.d.size());
  }
  for(int i = 0; i < x.d.size(); i++) {
    d[i] ^= x.d[i];
  }
  purge();
  return *this;
}

bigint bigint::operator<<(int x) const {
  bigint ret;
  ret.s = s;
  ret.d = vector<int>(d.size() + (x - 1) / BASE_BITS + 1, 0);
  int y = x % BASE_BITS;
  for(int i = 0; i < d.size(); i++) {
    if(y) {
      int p1 = (d[i] & (1 << (BASE_BITS - y)) - 1) << y;
      int p2 = d[i] >> (BASE_BITS - y);
      ret.d[i + x / BASE_BITS] |= p1; 
      ret.d[i + x / BASE_BITS + 1] |= p2; 
    } else {
      ret.d[i + x / BASE_BITS] = d[i]; 
    }
  }
  ret.purge();
  return ret;
}

bigint bigint::operator>>(int x) const {
  bigint ret;
  ret.s = s;
  ret.d = vector<int>(d.size() + (x - 1) / BASE_BITS + 1, 0);
  int y = x % BASE_BITS;
  for(int i = 0; i < d.size(); i++) {
    if(y) {
      int p1 = (d[i] & (1 << y) - 1) << (BASE_BITS - y);
      int p2 = d[i] >> y;
      if(x / BASE_BITS <= i) ret.d[i - x / BASE_BITS] |= p2; 
      if(x / BASE_BITS < i) ret.d[i - x / BASE_BITS - 1] |= p1; 
    } else if(x / BASE_BITS <= i) {
      ret.d[i - x / BASE_BITS] = d[i]; 
    }
  }
  ret.purge();
  return ret;
}

string bigint::to_string(int radix) const {
  if(d.empty()) {
    return "0";
  }
  string ret;
  bigint cpy = *this;
  while(cpy.d.size()) {
    int val = cpy % radix;
    cpy /= radix;
    if(val >= 10) {
      ret += 'A' + (val - 10);
    } else {
      ret += '0' + val;
    }
  }
  if(s) {
    ret += '-';
  }
  reverse(ret.begin(), ret.end());
  return ret;
}

bigint bigint::random(int bits) {
  bigint ret;
  for(int i = 0; i < bits; i++) {
    ret.set_bit(i, 1.0 * rand() / RAND_MAX < 0.5);
  }
  return ret;
}

bigint bigint::random_prime(int bits) {
  bigint ret;
  do {
    ret = random(bits);
    ret.set_bit(bits - 1, true);
    ret.set_bit(0, true);
  } while(!ret.probably_prime());
  return ret;
}

bigint bigint::sqrt() const {
  bigint ret;
  for(int i = 1 + bits() / 2; i >= 0; i--) {
    ret.set_bit(i, true);
    if(ret * ret > *this) {
      ret.set_bit(i, false);
    }
  }
  return ret;  
}

bigint bigint::gcd(const bigint & x) const {
  bigint a = *this;
  bigint b = x;
  while(!a.d.empty()) {
    b %= a;
    a.swap(b);
  }
  return b;
}

bigint bigint::mod_exp(const bigint & e, const bigint & mod) const {
  bigint ret = 1;
  for(int i = e.bits(); i >= 0; i--) {
    ret *= ret;
    ret %= mod;
    if(e.get_bit(i)) {
      ret *= *this;
      ret %= mod;
    }
  }
  return ret;
}

bigint bigint::mod_inv(const bigint & mod) const {
  bigint a = *this;
  bigint b = mod;
  bigint A = 1, B = 0;
  while(a != 0) {
    bigint m = b / a;
    B += mod - m * A % mod;
    B %= mod;
    b %= a;
    a.swap(b); A.swap(B);
  }
  return B;
}

bool bigint::probably_prime() const {
  if(*this < 2) {
    return false; 
  } else if(*this < 100) {
    for(int i = 2; i * i <= 100 && *this > i; i++) {
      if(*this % i == 0) {
        return false;
      }
    }
    return true;
  }

  int s;
  bigint d = *this - 1;
  for(s = 0; !d.get_bit(s); s++);
  d = d >> s;

  int n = bits();
  for(int k = 0; k < 20; k++) {
    int a = rand() & 0x7FFFFFFF;
    if(*this <= a) a %= to_int();
    if(a < 2) a = 2;

    bigint x = bigint(a).mod_exp(d, *this);
    if(x == 1 || x == *this - 1) {
      continue;
    }
    for(int i = 0; i < s; i++) {
      x *= x;
      x %= *this;
      if(x == *this - 1) {
        return true;
      }
    }
    return false;
  }

  return true;
}

// Uses the simple formula for calculating legendre numbers.
int bigint::legendre(const bigint & p) const {
  bigint res = mod_exp((p - 1) / 2, p);
  if(res == 1) {
    return 1;
  } else if(res == p - 1) {
    return -1;
  } else {
    return 0;
  }
}

// Uses Shanks-Tonelli algoithm
bigint bigint::mod_square_root(const bigint & p) const {
  if(p == 2) {
    return get_bit(0) ? 1 : 0;
  } else if(p % 4 == 3) {
    return mod_exp((p + 1) / 4, p);
  }

  bigint Q = p - 1;
  int S = 0;
  while(Q % 2 == 0) {
    Q /= 2;
    S++;
  }

  bigint W;
  for(W = 2; ; W++)
    if(W.legendre(p) == -1)
      break;

  bigint R = mod_exp((Q + 1) / 2, p);
  bigint V = W.mod_exp(Q, p);
  bigint ninv = mod_inv(p);

  while(true) {
    bigint val = R * R % p;
    val *= ninv; val %= p;

    int i;
    for(i = 0; val != 1; i++) {
      val *= val; val %= p;
    }
    
    if(i == 0) {
      break;
    }

    bigint RR = V;
    for(int j = 1; j < S - i - 1; j++) {
      RR *= RR; RR %= p;
    }
    R *= RR; R %= p;
  }

  return R;
}

ostream & operator <<(ostream & out, const bigint & x) {
  out << x.to_string();
  return out;
}

istream & operator >>(istream & in, bigint & x) {
  string s;
  in >> s;
  x = bigint(s);
  return in;
}

void solve_case() {
  string S; cin >> S;
  int q = 0;
  for(int i = 0; i < S.size(); i++) {
    if(S[i] == '?') q++;
  }
  for(int i = 0; i < 1 << q; i++) {
    string T = S;
    int qp = 0;
    for(int j = 0; j < T.size(); j++) {
      if(T[j] == '?') {
        T[j] = (i & 1 << qp++) ? '1' : '0';
      }
    }
    bigint xx(T, 2);
    bigint x = xx.sqrt();
    if(x * x == xx) {
      cout << xx.to_string(2) << endl;
      return;
    }
  }
}
