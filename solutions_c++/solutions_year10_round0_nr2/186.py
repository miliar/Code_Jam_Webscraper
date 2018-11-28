// Compiler : MS VC++ 8.0
// input  file : d.in
// output file : d.out

#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <fstream>
#include <ctime>
#include <conio.h>
#include <list>

using namespace std;
typedef long long lint;
typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<lint> VL; typedef vector<VL> VVL;
typedef vector<double> VD; typedef vector<VD> VVD;
typedef vector<char> VC; typedef vector<VC> VVC;
typedef vector<string> VS;
#define SIZE(c) ((int)(c).size())
#define SEQ(c) (c).begin(),(c).end()
#define FOR(i,a,b) for(int _U(b),i=(a);i<_U;++i)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int _U(a),i=(b)-1;i>=_U;--i)
#define FORS(i,c) FOR(i,0,SIZE(c))
#define REPD(i,n) FORD(i,0,n)
template<class T>string tostr(T v){ostringstream o;o<<v;return o.str();}
string tostrdouble(double v) {ostringstream o;o<<fixed<<setprecision(7)<<v; return o.str();}
#define UNIQUE(c) {sort(SEQ(c)); (c).erase(unique(SEQ(c)),(c).end());}
typedef pair<int,int> PII;
#define MIN(A,B) if ((B)<(A)) (A)=(B)
#define MAX(A,B) if ((B)>(A)) (A)=(B)
const int inf = 1000100100; // (inf + inf) fits into "int" type.
const double Pi = acos(-1.);
///////////////////////////////////////////////////////////////////////////////////
template <class T>
vector<T> splitString(string s, string sep = " ") {
  vector<T> ret;
  int pos = -1, posPrev = -2;
  do {
    posPrev = pos;
    pos = (int)s.find_first_of(sep, posPrev+1);
    if (pos == -1) pos = (int)s.size();
    if (pos-posPrev > 1) {
      istringstream is(s.substr(posPrev+1,pos-posPrev-1));
      T v; is >> v; ret.push_back(v);
    }
  } while (posPrev < (int)s.size());
  return ret;
}
///////////////////////////////////////////////////////////////////////////////////
string caseNo(int i) {return "Case #" + tostr(i) + ":";}

///////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

class LongNumber
{
private:
  static const int BASE = 10000;
  static const int BASE_LEN = 4;

  friend class FastMultiplier;

  std::vector<int> m_digs;
  bool m_sign; // if (m_sign==true) then negative, else positive.

private:
  void _Normalize() {
    while (m_digs.size() > 0 && m_digs[m_digs.size()-1] == 0) m_digs.pop_back();
    if (m_digs.size() == 0) m_sign = 0; 
  }

  void _CheckNormalized() const {
    assert(m_digs.size() == 0 || m_digs[m_digs.size()-1] > 0 && "There are leading zeroes");
    assert(m_digs.size() > 0 || m_sign == 0 && "Sign presents for 0 value");
  }

  void _SetDigit(size_t i_pos, int i_value) {
    assert(i_value < BASE);
    if (m_digs.size() < i_pos+1) m_digs.resize(i_pos+1);
    m_digs[i_pos] = i_value;
  }

  int _GetDigit(size_t i_pos) const {
    if (m_digs.size() < i_pos+1) return 0;
    return m_digs[i_pos];
  }

  // add without accounting the sign (actually as if this & other are positive)
  void _AddIgnoreSign(const LongNumber& i_other) {
    _CheckNormalized();
    i_other._CheckNormalized();
    int carry = 0;
    size_t size = std::max(m_digs.size(), i_other.m_digs.size());
    for (size_t i = 0; i < size; ++i) {
      carry += _GetDigit(i) + i_other._GetDigit(i);
      _SetDigit(i, carry % BASE);
      carry /= BASE;
    }
    assert(carry < BASE);
    if (carry > 0) _SetDigit(size, carry);
    _CheckNormalized();
  }

  void _SubIgnoreSignThisAboveEqualOther(const LongNumber& i_other) {
    _CheckNormalized();
    i_other._CheckNormalized();
    assert(m_digs.size() >= i_other.m_digs.size() && "mantissa of this should be >= i_other");
    int carry = 0;
    size_t pos = 0;
    while (pos < i_other.m_digs.size() || carry > 0) {
      assert(pos < m_digs.size() && "mantissa of this should be >= i_other");
      int value = 0;
      if (pos < m_digs.size()) value += m_digs[pos];
      if (carry) --value;
      if (value < i_other._GetDigit(pos)) {
        value += BASE;
        carry = 1;
      } else
        carry = 0;

      m_digs[pos] = value - i_other._GetDigit(pos);
      assert(0 <= m_digs[pos] && m_digs[pos] < BASE);

      ++pos;
    }
    _Normalize();
  }

  // returns -1,0,1 if mantissa of this is less, equal, or larger than i_other respectively
  int _CompareMantissa(const LongNumber& i_other) const {
    _CheckNormalized();
    i_other._CheckNormalized();
    size_t size = std::max(m_digs.size(), i_other.m_digs.size());
    for (int i = (int)size-1; i >= 0; --i) 
      if (_GetDigit(i) != i_other._GetDigit(i)) {
        int ret = _GetDigit(i) < i_other._GetDigit(i) ? -1 : 1;
        return ret;
      }
      return 0;
  }

public:
  explicit LongNumber(int _init = 0) : m_sign(0) {
    long long v = _init; 
    if (v < 0) m_sign = 1, v = -v;
    while (v > 0) {m_digs.push_back(int(v % BASE)); v /= BASE;}
  }

  explicit LongNumber(const std::string& _init) : m_sign() {
    int k = (int)_init.size();
    assert(k > 0 && "Wrong _init");
    int p = 0;
    if (_init[0] == '-') m_sign = 1, ++p;
    assert(p < k && "Wrong _init");
    int dig = 0;
    do {
      assert(isdigit(_init[p]) && "Wrong _init");
      dig = dig * 10 + _init[p] - '0';
      ++p;
    } while ((k - p) % BASE_LEN != 0);
    int len = (k - p) / BASE_LEN + 1;
    m_digs.resize(len);
    int di = len-1;
    m_digs[di--] = dig;
    for (; di >= 0; --di, p += BASE_LEN) {
      int dig = 0;
      for (size_t i = 0; i < BASE_LEN; ++i) {
        assert(isdigit(_init[p+i]) && "Wrong _init");
        dig = dig*10 + _init[p+i] - '0';
      }
      m_digs[di] = dig;
    }
    assert(p == k && "Something wrong with converting string to number");
    this->_Normalize();
  }

  // returns -1,0,1 if this less, equal or above of i_other respectively.
  int Compare(const LongNumber& i_other) const {
    if (m_sign != i_other.m_sign) {
      return m_sign ? -1 : 1;
    }

    int ret = _CompareMantissa(i_other);
    if (m_sign) ret = -ret;
    return ret;
  }


  bool IsZero() const {
    _CheckNormalized();
    return m_digs.size() == 0;
  }

  bool IsNegative() const {
    _CheckNormalized();
    return m_sign;
  }

  bool IsPositive() const {
    return !IsNegative() && !IsZero();
  }

  bool operator< (const LongNumber& i_other) const {
    return Compare(i_other) < 0;
  }

  bool operator<= (const LongNumber& i_other) const {
    return Compare(i_other) <= 0;
  }

  bool operator> (const LongNumber& i_other) const {
    return Compare(i_other) > 0;
  }

  bool operator>= (const LongNumber& i_other) const {
    return Compare(i_other) >= 0;
  }

  bool operator== (const LongNumber& i_other) const {
    return Compare(i_other) == 0;
  }

  bool operator!= (const LongNumber& i_other) const {
    return Compare(i_other) != 0;
  }

  string ToStr() const {
    _CheckNormalized();
    if (IsZero()) return "0";
    ostringstream os;
    if (m_sign) os << '-';
    os << m_digs[m_digs.size()-1];
    for (int i = (int)m_digs.size()-2; i >= 0; --i) {
      string s;
      int v = m_digs[i];
      for (int j = 0; j < BASE_LEN; ++j) {s = char(v%10 + '0') + s; v /= 10;}
      os << s;
    }
    string ret = os.str();
    return ret;
  }

  LongNumber& operator+= (const LongNumber& i_other) {
    if (m_sign == i_other.m_sign) {
      this->_AddIgnoreSign(i_other);
    } else {
      int cmp = _CompareMantissa(i_other);
      if (cmp == 1) {
        this->_SubIgnoreSignThisAboveEqualOther(i_other);
      } else {
        LongNumber res = i_other;
        res._SubIgnoreSignThisAboveEqualOther(*this);
        *this = res;
      }
    }
    return *this;
  }

  LongNumber operator+ (const LongNumber& i_other) const {
    LongNumber ret = *this;
    ret += i_other;
    return ret;
  }

  LongNumber operator- () const {
    LongNumber ret = *this;
    if (!IsZero()) ret.m_sign = !ret.m_sign;
    return ret;
  }

  LongNumber& operator-= (const LongNumber& i_other) {
    *this += -i_other;
    return *this;
  }

  LongNumber operator- (const LongNumber& i_other) const {
    LongNumber ret = *this;
    ret -= i_other;
    return ret;
  }

  LongNumber& operator*= (const LongNumber& i_other) {
    // check if at least one operand is zero
    if (this->IsZero() || i_other.IsZero()) {
      *this = LongNumber();
      return *this;
    }

    size_t s1 = m_digs.size(), s2 = i_other.m_digs.size();
    LongNumber res;
    res.m_digs.reserve(s1 + s2 + 1);

    for (size_t i1 = 0; i1 < s1; ++i1) {
      int carry = 0;
      size_t i2 = 0;
      for (; i2 < s2; ++i2) {
        carry += m_digs[i1] * i_other.m_digs[i2] + res._GetDigit(i1 + i2);
        res._SetDigit(i1 + i2, carry % BASE);
        carry /= BASE;
      }
      while (carry > 0) {
        res._SetDigit(i1 + i2, carry % BASE);
        carry /= BASE;
        ++i2;
      }
    }

    res.m_sign = m_sign != i_other.m_sign;
    res._Normalize();
    *this = res;
    return *this;
  }

  LongNumber Power(long long i_exp) const {
    LongNumber ret(1);
    LongNumber a(*this);
    while (i_exp > 0) {
      if (i_exp % 2 == 1) {ret *= a; --i_exp;}
      if (i_exp > 0) {i_exp /= 2; a *= a;}      
    }
    return ret;
  }

  // div by i_short, this is used in DivModNonNegative
  void DivShortNonNegative(int i_short) {
    assert(!this->IsNegative());
    assert(i_short > 0 && i_short < BASE);

    int rem = 0;
    for (int i = (int)m_digs.size() - 1; i >= 0; --i) {
      int all = m_digs[i] + rem * BASE;
      rem = all % i_short;
      m_digs[i] = all / i_short;
    }
    _Normalize();

    // rem contains reminder here, it could be used or returned if needed.
  }

  // calculates division of long numbers.
  // returns false when *this < 0 || i_divisor <= 0.
  // returns true in other case.
  // *this == i_divisor * o_quotient + o_mod, o_mod < i_divisor.
  //
  // Algorithm: uses binary search approach, long mul on every iteration.
  bool DivModNonNegative(const LongNumber& i_divisor, LongNumber& o_quotient, LongNumber& o_mod) {
    if (this->IsNegative())
      return false;
    if (!i_divisor.IsPositive())
      return false;

    LongNumber mn(0);
    LongNumber mx(*this);

    LongNumber mul;

    bool fl_min_changed = false;

    while (mn.Compare(mx) == -1) {
      LongNumber mid = mn;
      mid += mx;
      mid += LongNumber(1);
      mid.DivShortNonNegative(2);

      mul = i_divisor;
      mul *= mid;

      if (mul > *this) {
        mx = mid + LongNumber(-1);
        fl_min_changed = true;
      } else {
        mn = mid;
        fl_min_changed = false;
      }
    }
    o_quotient = mn;

    o_mod = *this;
    o_mod -= mul;
    if (fl_min_changed)
      o_mod += i_divisor;

    return true;
  }

  // divide *this by i_other integrally
  LongNumber& operator/= (const LongNumber& i_other) {
    LongNumber o_div, o_mod;
    bool div_res = DivModNonNegative(i_other, o_div, o_mod);
    assert(div_res && "WrongResultReturned");
    *this = o_div;
    return *this;
  }

  // find modulo *this by i_other integrally
  LongNumber& operator%= (const LongNumber& i_other) {
    LongNumber o_div, o_mod;
    bool div_res = DivModNonNegative(i_other, o_div, o_mod);
    assert(div_res && "WrongResultReturned");
    *this = o_mod;
    return *this;
  }

}; // class LongNumber

////////////////////////////////////////////////////////////////////////////////////

// Karatsuba algorithm implementation
// Refer to http://en.wikipedia.org/wiki/Karatsuba_algorithm for detailed description.
class FastMultiplier 
{
private:
  typedef std::vector<int> VI;
  typedef std::list<VI> VectorPool;
  VectorPool m_vector_pool;
  VectorPool::iterator m_vector_pool_top;

  static const int BASE = LongNumber::BASE;

  static const int SHORT_NUM_LEN = 8;

private:
  VI& _GetVector() {
    VI& ret = *m_vector_pool_top;
    ++m_vector_pool_top;
    if (m_vector_pool_top == m_vector_pool.end()) {
      m_vector_pool.push_back(VI());
      m_vector_pool_top = m_vector_pool.end();
      --m_vector_pool_top;
    }
    return ret;
  }

  static void _SetDigit(VI& io_vec, size_t i_pos, int i_val) {
    if (io_vec.size() <= i_pos) io_vec.resize(i_pos + 1);
    io_vec[i_pos] = i_val;
  }

  static int _GetDigit(const VI& io_vec, size_t i_pos) {
    if (io_vec.size() <= i_pos) return 0;
    return io_vec[i_pos];
  }

  static void _Trim(VI& io_vec) {
    if (io_vec.size() == 0) return;
    size_t i = io_vec.size() - 1;
    while (i > 0 && io_vec[i] == 0) --i;
    io_vec.resize(i+1);
  }

  void _Split(VI& o_x0, VI& o_x1, size_t m, const VI& i_x) {
    size_t m1 = std::min(m, i_x.size());

    o_x0.resize(m1);
    std::copy(i_x.begin(), i_x.begin() + m1, o_x0.begin());
    _Trim(o_x0);

    o_x1.resize(i_x.size() - m1);
    std::copy(i_x.begin() + m1, i_x.end(), o_x1.begin());
    _Trim(o_x1);
  }

  void _MulSlow(VI& o_res, const VI& i_left, const VI& i_right) {
    o_res.clear();
    size_t a = i_left.size(), b = i_right.size();
    o_res.resize(a+b);

    const int * p_left = &*i_left.begin();
    const int * p_right = &*i_right.begin();
    int * op_res = &*o_res.begin();

    for (size_t i = 0; i < a; ++i) {
      long long carry = 0;
      size_t j = 0;
      for (; j < b; ++j) {
        carry += long long(p_left[i]) * p_right[j] + op_res[i+j];
        //++m_ops;
        op_res[i + j] = int(carry % BASE);
        carry /= BASE;
      }
      while (carry > 0) {carry += o_res[i+j]; o_res[i+j] = int(carry % BASE), carry /= BASE; ++j;}
    }
    _Trim(o_res);
  }

  void _Sub(VI& io_res, const VI& i_other) {
    int carry = 0;
    size_t i = 0;
    for (; i < i_other.size(); ++i) {
      io_res[i] -= i_other[i] + carry;
      if (io_res[i] < 0) io_res[i] += BASE, carry = 1; else carry = 0;
      assert(io_res[i] >= 0);
    }
    if (carry) {
      while (io_res[i] == 0) io_res[i] = 9, ++i;
      --io_res[i];
    }
    _Trim(io_res);
  }

  void _Add(VI& io_res, const VI& i_other) {
    size_t len = std::max(io_res.size(), i_other.size());
    io_res.resize(len+1);
    int carry = 0;
    for (size_t i = 0; i < len; ++i) {
      carry += _GetDigit(io_res, i) + _GetDigit(i_other, i);
      if (carry >= BASE) io_res[i] = carry - BASE, carry = 1; else io_res[i] = carry, carry = 0;
    }
    if (carry > 0) io_res[len] = carry;
    _Trim(io_res);
  }

  void _MulFast(VI& o_res, const VI& i_left, const VI& i_right) {
    if (i_left.size() <= SHORT_NUM_LEN || i_right.size() <= SHORT_NUM_LEN) {
      _MulSlow(o_res, i_left, i_right);
      return;
    }
    VectorPool::iterator mem_vector_pool_top = m_vector_pool_top;
    VI& x0 = _GetVector(), &x1 = _GetVector(), &y0 = _GetVector(), &y1 = _GetVector();

    size_t m = std::max(i_left.size(), i_right.size()) / 2;
    this->_Split(x0, x1, m, i_left);
    this->_Split(y0, y1, m, i_right);

    VI& z2 = o_res; 
    this->_MulFast(z2, x1, y1);
    VI& z0 = this->_GetVector();
    this->_MulFast(z0, x0, y0);
    VI& z1 = _GetVector();
    _Add(x1, x0);
    _Add(y1, y0);
    _MulFast(z1, x1, y1);
    _Sub(z1, z2);
    _Sub(z1, z0);

    z2.insert(z2.begin(), 2 * m, 0);
    z1.insert(z1.begin(), m, 0);

    _Add(z2, z1);
    _Add(z2, z0);

    m_vector_pool_top = mem_vector_pool_top;
  }

public:

  LongNumber Mul(const LongNumber& i_left, const LongNumber& i_right) {
    if (i_left.m_digs.size() <= SHORT_NUM_LEN || i_left.m_digs.size() <= SHORT_NUM_LEN) {
      // perform slow multiplication for short numbers
      LongNumber ret = i_left;
      ret *= i_right;
      return ret;
    }
    m_vector_pool.clear(); m_vector_pool.insert(m_vector_pool.end(), VI());
    m_vector_pool_top = m_vector_pool.begin();

    LongNumber ret;
    this->_MulFast(ret.m_digs, i_left.m_digs, i_right.m_digs);
    ret.m_sign = i_left.m_sign ^ i_right.m_sign;
    ret._Normalize();

    m_vector_pool.clear();
    return ret;
  }
}; // class FastMultiplier

////////////////////////////////////////////////////////////////////////////////////
typedef vector<LongNumber> VLN;

int n;
VS num_str;
VLN num, dif;

LongNumber gcd(LongNumber a, LongNumber b) {
  LongNumber zero(0);
  while (b != zero) {
    LongNumber tmp = a;
    a = b;

    //b = tmp % b;
    tmp %= b;
    b = tmp;
  }
  return a;
}

string solve() {
  num = VLN(n);
  REP (i,n) num[i] = LongNumber(num_str[i]);
  sort(SEQ(num));

  dif = VLN(n-1);
  REP (i,n-1) {
    dif[i] = num[i+1];
    dif[i] -= num[i];
  }

  LongNumber dst = dif[0];
  FOR (i,1,n-1) dst = gcd(dst,dif[i]);

  LongNumber rem = num[0];
  rem %= dst;

  if (rem.IsZero())
    return "0";

  LongNumber res = dst;
  res -= rem;
  string ret = res.ToStr();

  return ret;

}


void main()
{
  clock_t clock_global = clock();
  ifstream ifs("d.in");
  ofstream ofs("d.out"); ofs << setprecision(9);
  int ntests;
  ifs >> ntests;
  getline(ifs,string());
  FOR (test,1,ntests+1) {
    clock_t clock_test = clock();
    ofs << caseNo(test);
    cout << caseNo(test) << " ... ";
    //-------------------------------------------------------------
    ifs >> n;
    num_str = VS(n);
    REP (i,n) ifs >> num_str[i];
    string res = solve();
    ofs << " " << res;
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
