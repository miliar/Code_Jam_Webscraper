/**
 * Description: Class to be used for large integer arithmetic.  The class
 *              contains operators for doing simple arithmetic (+, -, *, /, %),
 *              comparisons (<, >, <=, >=, ==, !=), bitwise operations
 *              (&, |, ^, <<, >>), prefix/postfix increments/decrements
 *              (++, --), stream operators for reading in and writing to a
 *              stream, as well as many other operations that can be performed
 *              on integers.
 * Author: Mark Gordon
 * Date: November 30th, 2008
 *
**/

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <math.h>

using namespace std;

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

  // Computes *this^e.
  bigint pow(const bigint & e) const;

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

  // Returns a sorted list of the prime factors of *this.  This uses a
  // combination of trial division, Pollard's Rho algorithm and the quadratic
  // sieve.
  vector<bigint> factor(bool verbose = false) const;

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
  return *this;
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


bigint bigint::pow(const bigint & e) const {
  bigint ret = 1;
  for(int i = e.bits(); i >= 0; i--) {
    ret *= ret;
    if(e.get_bit(i)) {
      ret *= *this;
    }
  }
  return ret;
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

// Used to expose the sqrt(double) method that is otherwise hidden from within
// the bigint class.
static double sq_root(double x) { return sqrt(x); }

// A simple helper function for computing the symetric difference between two
// sorted lists.  This is used several times in the factor method.
template<class T>
static vector<T> list_xor(const vector<T> & A, const vector<T> & B) {
  int a = 0;
  int b = 0;
  vector<T> ret;
  while(a < A.size() && b < B.size()) {
    if(A[a] == B[b]) {
      a++;
      b++;
    } else if(A[a] < B[b]) {
      ret.push_back(A[a++]);
    } else {
      ret.push_back(B[b++]);
    }
  }
  while(a < A.size()) {
    ret.push_back(A[a++]);
  }
  while(b < B.size()) {
    ret.push_back(B[b++]);
  }
  return ret;
}

vector<bigint> bigint::factor(bool verbose) const {
  static const int TRIVIAL_DIVISION = 10000;
  static const int PRIME_SIEVE = 50000000;
  static const int POLLARD_RHO_ITERATIONS = 100;
  static const int DOUBLE_LARGE_PRIME_SET_SIZE = 10000000;

  bigint n = *this;

  if(verbose) {
    cout << "Starting trial division" << endl;
  }

  // Search for small prime factors using trial division.
  vector<bigint> ret;
  int div_bound = TRIVIAL_DIVISION;
  if(n.sqrt() < div_bound) {
    div_bound = n.sqrt().to_int();
  }
  for(int i = 2; i <= div_bound; i++) {
    while(n % i == 0) {
      n /= i;
      ret.push_back(i);
    }
  }
  if(n == 1 || n <= bigint(div_bound) * div_bound) {
    if(n != 1) {
      ret.push_back(n);
    }
    return ret;
  }

  // Check if we are probably wasting our time.
  if(n.probably_prime()) {
    ret.push_back(n);
    return ret;
  }

  if(verbose) {
    cout << "Finished trial division, trying Pollard's Rho algorithm" << endl;
  }

  // Try Pollard's Rho algorithm for a little bit.
  for(int iter = 0; iter < POLLARD_RHO_ITERATIONS; iter += POLLARD_RHO_ITERATIONS / 100) {
    bigint c = random(n.bits() + 4) % n;
    bigint x = 2;
    bigint y = 2;
    bigint g = 1;
    for( ; iter < POLLARD_RHO_ITERATIONS && g == 1; iter++) {
      x *= x; x += c; x %= n;
      y *= y; y += c; y %= n;
      y *= y; y += c; y %= n;
      g = (x - y).abs().gcd(n);
    }
    if(g != 1 && g != n) {
      if(verbose) {
        cout << "Pollard's Rho algorithm found non-trivial factor: " << g << endl;
      }

      // Divide and recursively factor each half and merge the lists.
      vector<bigint> fa = g.factor(verbose);
      vector<bigint> fb = (n / g).factor(verbose);
      for(int i = 0; i < fa.size(); i++) {
        ret.push_back(fa[i]);
      }
      for(int i = 0; i < fb.size(); i++) {
        ret.push_back(fb[i]);
      }
      sort(ret.begin(), ret.end());
      return ret;
    }
  }

  // Calculate how large the factor base should be.  This formula comes from
  // the paper found at http://www.math.uiuc.edu/~landquis/quadsieve.pdf .
  int fsz = (int)::pow(exp(sq_root(n.bits() * log(2) * log(n.bits() * log(2)))),
                     sq_root(2) / 4) * 2;
  fsz = min(fsz, 500000);

  // Perform the Sieve of Eratosthenes to get a list of small primes to use
  // as the factor base.  This only needs to be done once.  If large primes are
  // required the probably_prime method will be used instead.
  static vector<int> is_prime;
  if(is_prime.empty()) {
    is_prime = vector<int>(PRIME_SIEVE, true);
    for(int i = 2; i * i < PRIME_SIEVE; i++) {
      for(int j = i * i; is_prime[i] && j < PRIME_SIEVE; j += i) {
        is_prime[j] = false;
      }
    }
  }

  bigint rt = n.sqrt() + 1;
  if(n.get_bit(0) != rt.get_bit(0)) rt++;

  // Calculate the factor base.  A factor base consists of primes p such that
  // n has a quadratic residue modulo p.
  vector<int> primes;
  vector<pair<int, int> > f_base;
  vector<double> f_log;
  for(int p = 2; primes.size() < fsz; p++) {
    if(p < PRIME_SIEVE && !is_prime[p]) {
      continue;
    }
    bigint nm = n % p;
    if(nm.legendre(p) != 1) {
      continue;
    }
    if(p >= PRIME_SIEVE && !bigint(p).probably_prime()) {
      continue;
    }
    primes.push_back(p);

    if(verbose && primes.size() % 100 == 0) {
      cout << "Found " << primes.size() << " of " << fsz << " primes - " << p << endl;
    }
  }

  int msz = min(fsz, 100);
  msz *= msz * msz;
  msz = max(primes.back() + 1, msz);

  for(int i = 0; i < primes.size(); i++) {
    if(primes[i] == 2) {
      // 2 is handled as a special case.
      continue;
    }
    vector<long long> onrtp;
    double p_log = log(primes[i]);
    int power = 0;
    for(long long p = primes[i]; p <= 2000000000; p *= primes[i], power++) {
      long long nm = n % p;
      vector<long long> nrtp;
      if(p == primes[i]) {
        nrtp.push_back(bigint(nm).mod_square_root(p).to_int());
        nrtp.push_back((p - nrtp[0]) % p);
      } else {
        for(int j = 0; j < onrtp.size(); j++) {
          for(long long v = onrtp[j]; v < p; v += p / primes[i]) {
            if(v * v % p == nm) {
              nrtp.push_back(v);
              nrtp.push_back((p - v) % p);
            }
          }
        }
      }

      sort(nrtp.begin(), nrtp.end());
      nrtp.resize(unique(nrtp.begin(), nrtp.end()) - nrtp.begin());

      for(int i = 0; i < nrtp.size(); i++) {
        f_base.push_back(make_pair(p, (p + nrtp[i] - rt % p) % p));
        f_log.push_back(p_log);
      }
      onrtp.swap(nrtp);
    }
    if(verbose && i % 100 == 0) {
      cout << "Computed root on " << i + 1 << " of " << fsz << " factors - " << primes[i] << '^' << power << endl;
    }
  }

  // Tracks pairs (x, y) such that y = x^2 - n and y factors over the factor base.
  vector<pair<bigint, bigint> > field;
  vector<long long> field_large_prime;

  // mat[i].first is a list of columns that have a 1 in them for the ith row.
  // mat[i].second is a list of what linear combination of original rows is
  // represented in mat[i].first.
  vector<pair<vector<int>, vector<int> > > mat;

  // owner[i] tracks which row, if any, should be the only row to have 1 in the
  // ith column.
  vector<int> owner(fsz, -1);

  // set for tracking double large primes.
  set<pair<long long, long long> > dlp;

  vector<double> xlog(msz + 1, 0);
  const double LOG_2 = log(2.0);
  for(long long xs = 0; ; xs += msz) {
    if(verbose) {
      cout << "Sieving interval [" << xs << ", " << xs + msz << ")" << endl;
    }

    long double drt = rt.to_long_double();
    long double dn = n.to_long_double();
    long double x = drt * drt - dn;

    unsigned int lsd = rt % (1 << 30);
    unsigned int negn = n % (1 << 30);

    for(int i = 0; i < msz; i++) {
      long double y = 2 * (drt + i) - 1;
      if(i % 100 == 0) {
        xlog[i] = log(x);
      }
      xlog[i + 1] = xlog[i] + y / x;
      x += y;

      unsigned int v = (lsd + i) * (lsd + i) - negn;
      v |= 1 << 30;
      xlog[i] -= __builtin_ctz(v) * LOG_2;
    }

    for(int i = 0; i < f_base.size(); i++) {
      int p = f_base[i].first;
      int & x = f_base[i].second;
      for( ; x < msz; x += p) {
        xlog[x] -= f_log[i];
      }
      x -= msz;
    }

    for(int i = 0; i < msz; i++) {
      if(xlog[i] < log(1000000000)) {
        bigint v = rt + i;
        v *= v;
        v -= n;
        
        int div2;
        for(div2 = 0; !v.get_bit(div2); div2++);
        v = v >> div2;

        for(int j = 1; j < fsz; j++) {
          while(v % primes[j] == 0) {
            v /= primes[j];
          }
        }

        bool added = false;
        if(v <= bigint("7FFFFFFF", 16)) {
          long long iv = v.to_long_long();
          bigint trt = rt + i;
          if(iv != 1) {
            if(dlp.size() < DOUBLE_LARGE_PRIME_SET_SIZE || iv <= dlp.rbegin()->first) {
              typeof(dlp.begin()) it = dlp.lower_bound(make_pair(iv, 0));
              if(it != dlp.end() && it->first == iv) {
                // We found two factors with the same large prime!
                if(verbose) {
                  cout << "Found double prime " << iv << " (dlp size: " << dlp.size() << ")" << endl;
                }
                added = true;
                bigint ort = trt - (xs + i - it->second);
                field.push_back(make_pair(trt * ort, 
                                         (trt * trt - n) * (ort * ort - n)));
                field_large_prime.push_back(iv);
              } else {
                dlp.insert(make_pair(iv, xs + i));
                if(dlp.size() > DOUBLE_LARGE_PRIME_SET_SIZE) {
                  dlp.erase(--dlp.end());
                }
              }
            }
          } else {
            // Lucky day, v factored completely over the factor base.
            added = true;
            field.push_back(make_pair(trt, trt * trt - n));
            field_large_prime.push_back(1);
          }
        }

        if(added) {
          if(verbose) {
            cout << i << ": " << field.size() << " of " << fsz + 1 << " xlog " << xlog[i] << endl;
          }

           // Create a row for this solution.
          vector<int> v_primes;
          bigint v = field.back().second;
          for(int j = 0; j < fsz; j++) {
            int cnt = 0;
            while(v % primes[j] == 0) {
              v /= primes[j];
              cnt++;
            }
            if(cnt % 2) {
              v_primes.push_back(j);
            }
          }
          mat.push_back(make_pair(v_primes, vector<int>(1, field.size() - 1)));

          // Cancel columns that are already owned.
          for(int j = 0; j < v_primes.size(); j++) {
            int k = owner[v_primes[j]];
            if(k != -1) {
              mat.back().first = list_xor(mat.back().first, mat[k].first);
              mat.back().second = list_xor(mat.back().second, mat[k].second);
            }
          }

          for(int j = 0; j < mat.back().first.size(); j++) {
            if(owner[mat.back().first[j]] != -1) {
              cout << "Linear algebra error - owned column" << endl;
              exit(1);
            }
          }

          if(!mat.back().first.empty()) {
            // Assign a column for this row to own.
            int id = mat.back().first.back();
            if(owner[id] != -1) {
              cout << "Linear algebra error" << endl;
              exit(1);
            }

            owner[id] = mat.size() - 1;
            for(int j = 0; j + 1 < mat.size(); j++) {
              if(binary_search(mat[j].first.begin(), mat[j].first.end(), id)) {
                mat[j].first = list_xor(mat.back().first, mat[j].first);
                mat[j].second = list_xor(mat.back().second, mat[j].second);
              }
            }
          } else {
            // We have a linear dependence! Hoorahh!
            if(verbose) {
              cout << "Linear dependence detected" << endl;
            }

            // Calculate a and b such that a^2 = b^2 mod n.
            bigint a = 1;
            bigint b = 1;
            vector<int> & v = mat.back().second;
            vector<int> parity(primes.size(), false);
            for(int k = 0; k < v.size(); k++) {
              a *= field[v[k]].first; a %= n;
              b *= field_large_prime[v[k]]; b %= n;
              bigint val = field[v[k]].second;
              for(int s = 0; s < primes.size(); s++) {
                while(val % primes[s] == 0) {
                  val /= primes[s];
                  parity[s] = !parity[s];
                  if(!parity[s]) {
                    b *= primes[s]; b %= n;
                  }
                }
              }
            }
            if(a < b) {
              a.swap(b);
            }

            if(a * a % n != b * b % n) {
              cout << "Computation error: squares not congruent" << endl;
              exit(1);
            }

            // We now have (a + b)(a - b) = n.  Calculate gcd(a + b, n) and
            // gcd(a - b, n) to try to find non trivial factor.  This usually works.
            for(bigint f = a - b; f <= a + b; f += b << 1) {
              bigint factor = f.gcd(n);
              if(factor != 1 && factor != n) {
                if(verbose) {
                  cout << "Non-trivial factor calculated: " << factor << endl;
                }

                // Divide and recursively factor each half and merge the lists.
                vector<bigint> fa = factor.factor(verbose);
                vector<bigint> fb = (n / factor).factor(verbose);
                for(int i = 0; i < fa.size(); i++) {
                  ret.push_back(fa[i]);
                }
                for(int i = 0; i < fb.size(); i++) {
                  ret.push_back(fb[i]);
                }
                sort(ret.begin(), ret.end());
                return ret;
              }
            }
          }
        }
      }
    }

    rt += msz;
  }
  
  return vector<bigint>();
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    int n; cin >> n;
    vector<bigint> v;
    for(int i = 0; i < n; i++) {
      bigint x; cin >> x;
      v.push_back(x);
    }
    bigint g = 0;
    bigint mn = *min_element(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++) {
      g = g.gcd(v[i] - mn);
    }
    cout << (g - mn % g) % g << endl;
  }
}

