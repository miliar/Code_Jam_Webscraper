#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstring>
#include <cmath>

typedef long long ll;

const double kPI = acos(-1.0);

class bint {
 public:
  bint() { Init(0); }
  bint(int num) { Init(num); }
  bint(const char* str) { Init(str, strlen(str)); }
  bint(const bint& b) { Init(b); }
  ~bint() { delete [] dg_; }
  void Copy(const bint& b) {
    sign_ = b.sign_, len_ = b.len_;
    if (alloc_ < len_) { alloc_ = b.alloc_; delete [] dg_; dg_ = new int[alloc_]; }
    memcpy(dg_, b.dg_, len_ * sizeof(int)); }
  void Swap(bint* b) {
    std::swap(sign_, b->sign_), std::swap(len_, b->len_);
    std::swap(alloc_, b->alloc_), std::swap(dg_, b->dg_); }
  bint& operator= (const bint& b) { Copy(b); return *this; }
  bint  operator- () const { bint t(*this); t.ChangeSign(); return t; }
  bint  operator- (const bint& b) const { bint t(*this); t -= b; return t; }
  bint& operator-= (const bint& b) { this->Sub(b); return *this; }
  bint  operator+ (const bint& b) const { bint t(*this); t += b; return t; }
  bint& operator+= (const bint& b) { this->Add(b); return *this; }
  bint  operator* (const bint& b) const {
    bint r; this->Mul(*this, b, &r); return r; }
  bint& operator*= (const bint& b) {
    bint t(*this); this->Mul(t, b, this); return *this; }
  bint  operator/ (int b) const { bint re; Div(*this,b,&re); return re; }
  bint  operator/ (const bint& b) const {
    bint re, rest; Div(*this, b, &re, &rest); return re; }
  bint& operator/= (int b) { bint tmp(*this); Div(tmp, b, this); return *this; }
  bint& operator/= (const bint& b) {
    bint tmp(*this), rest; Div(tmp, b, this, &rest); return *this; }
  int   operator% (int b) const {
    bint re; int rest; Div(*this, b, &re, &rest); return rest; }
  bint  operator% (const bint& b) const {
    bint re, rest; Div(*this, b, &re, &rest); return rest; }
  bint& operator%= (const bint& b) {
    bint tmp(*this), rest; Div(tmp, b, this, &rest); return *this; }
  bint& operator-- () { this->Sub(1); return *this; }
  bint  operator-- (int) { bint t(*this); this->Sub(1); return t; }
  bint& operator++ () { this->Add(1); return *this; }
  bint  operator++ (int) { bint t(*this); this->Add(1); return t; }
  bool  operator== (const bint& b) const {
    if (sign_ != b.sign_) return false;
    if (len_ != b.len_) return false;
    for (int i = 0; i < len_; ++i) if (dg_[i] != b.dg_[i]) return false;
    return true;}
  bool  operator!= (const bint& b) const {return !operator==(b);}
  bool  operator < (const bint& b) const {
    if (sign_ != b.sign_) return sign_ < b.sign_;
    if (sign_ > 0) return AbsLess(*this, b);
    else return AbsLess(b, *this);}
  bool  operator <= (const bint& b) const {return !(b < *this);}
  bool  operator > (const bint& b) const {return b < *this;}
  bool  operator >= (const bint& b) const {return !(*this < b);}
  int Parity() const { return dg_[0] % 2; }
  void Print() {
    if (sign_ < 0) putchar('-');
    printf(FIRST_DG_FORMAT, dg_[len_ - 1]);
    for (int i = len_ - 2; i >= 0; --i) printf(DG_FORMAT, dg_[i]); }
  static void Mul(const bint& a, int b, bint* c);
  static void Mul(const bint& a, const bint& b, bint* c);
  static void MulNaive(const bint& a, const bint& b, bint* c);
  static void MulFast(const bint& a, const bint& b, bint* c);
  static void Div(const bint& a, int b, bint* c, int* rest = NULL);
  static void Div(const bint& a, const bint& b, bint* c, bint* rest);
  static void GCD(const bint& a, const bint& b, bint* d);
 private:
  void Init(int num);
  bool Init(const char* str, int inten);
  void Init(const bint& b) {
    sign_ = b.sign_, len_ = b.len_, alloc_ = b.alloc_;
    dg_ = new int[alloc_];
    memcpy(dg_, b.dg_, len_ * sizeof(int)); }
  void Alloc(int req_len) {
    for (alloc_ = 1; alloc_ < req_len; alloc_ *= 2); dg_ = new int[alloc_]; }
  void Realloc(int req_len) {
    if (alloc_ < req_len) {
      int* tmp = dg_;
      Alloc(req_len);
      memcpy(dg_, tmp, len_ * sizeof(int));
      delete [] tmp;
    } }
  void Trim() { for (; len_ > 1 && !dg_[len_ - 1]; --len_); }
  int Sign() const { return sign_; }
  void ChangeSign() { sign_ = -sign_; CorrectSign(); }
  void CorrectSign() { if (len_ == 1 && dg_[0] == 0) sign_ = 1; }
  void AbsSub(const bint& b);
  void AbsAdd(const bint& b);
  void Sub(const bint& b);
  void Add(const bint& b);
  void Shift(int k);
  static bool AbsLess(const bint& a, const bint& b) {
    if (a.len_ != b.len_) return a.len_ < b.len_;
    int i = a.len_ - 1;
    for (; i >= 0 && a.dg_[i] == b.dg_[i]; --i);
    return i >= 0 && a.dg_[i] < b.dg_[i];
  }
  int sign_, len_, alloc_;
  int* dg_;
  static const int B;
  static const int MAX_DIGIT;
  static const int DIGIT_WIDTH;
  static const char* FIRST_DG_FORMAT;
  static const char* DG_FORMAT;
};

const int bint::B = 10000L;
const int bint::MAX_DIGIT = 9999L;
const int bint::DIGIT_WIDTH = 4;
const char* bint::FIRST_DG_FORMAT = "%d";
const char* bint::DG_FORMAT = "%04d";

inline void bint::Init(int num) {
  if (num == 0) {
    sign_ = 1, len_ = 1, alloc_ = 1, dg_ = new int[1];
    dg_[0] = 0;
  } else {
    if (num > 0) sign_ = 1;
    else sign_ = -1, num = -num;
    len_ = 0;
    for (int t = num; t > 0; t /= B, ++len_);
    Alloc(len_);
    for (int t = num, i = 0; t > 0; t /= B, ++i) dg_[i] = t % B;
  }
}

inline bool bint::Init(const char* str, int slen) {
  while (isspace(*str)) ++str, --slen;
  if (!slen) return false;
  if (*str == '-') sign_ = -1, ++str, --slen;
  else sign_ = 1;
  if (!slen) return false;
  Init(0);
  Realloc((slen + DIGIT_WIDTH - 1) / DIGIT_WIDTH);
  int i, j; char c = '\0';
  for (i = 0; i < slen; ++i) if (!isdigit(str[i])) return false;
  for (j = slen - DIGIT_WIDTH, i = 0; j >= 0; j -= DIGIT_WIDTH, ++i)
    sscanf(str + j, DG_FORMAT, dg_ + i);
  if ((j += DIGIT_WIDTH) > 0) {
    char buf[DIGIT_WIDTH + 1];
    memcpy(buf, str, j * sizeof(char));
    buf[j] = '\0';
    sscanf(buf, FIRST_DG_FORMAT, dg_ + (i++));
  }
  len_ = i;
  Trim();
}

void bint::AbsSub(const bint& b) {
  int i, carry;
  for (i = carry = 0; i < b.len_; ++i) {
    dg_[i] -= b.dg_[i] + carry;
    if (dg_[i] < 0) dg_[i] += B, carry = 1;
    else carry = 0;
  }
  if (carry) {
    for (; i < len_ && !dg_[i]; ++i) dg_[i] = MAX_DIGIT;
    --dg_[i];
  }
  Trim();
}

void bint::AbsAdd(const bint& b) {
  int i, len = std::max(len_, b.len_), carry;
  Realloc(len + 1);
  for (i = len_; i <= len; ++i) dg_[i] = 0;
  for (i = carry = 0; i < b.len_; ++i) {
    dg_[i] += b.dg_[i] + carry;
    if (dg_[i] >= B) dg_[i] -= B, carry = 1;
    else carry = 0;
  }
  if (carry) {
    for (; i < len && dg_[i] == MAX_DIGIT; ++i) dg_[i] = 0;
    ++dg_[i];
  }
  len_ = len + 1;
  Trim();
}

void bint::Sub(const bint& b) {
  if (sign_ == b.sign_) {
    if (AbsLess(*this, b)) {
      bint tmp(b);
      tmp.AbsSub(*this);
      tmp.sign_ = -sign_;
      this->Swap(&tmp);
    } else {
      AbsSub(b);
    }
  } else {
    AbsAdd(b);
  }
  CorrectSign();
}

void bint::Add(const bint& b) {
  if (sign_ == b.sign_) {
    AbsAdd(b);
  } else {
    if (AbsLess(*this, b)) {
      bint tmp(b);
      tmp.AbsSub(*this);
      tmp.sign_ = b.sign_;
      this->Swap(&tmp);
    } else {
      AbsSub(b);
    }
  }
  CorrectSign();
}

void bint::Shift(int k) {
  if (k == 0) return;
  len_ += k; Realloc(len_);
  for (int i = len_ - 1; i >= k; --i) dg_[i] = dg_[i - k];
  for (int i = 0; i < k; ++i) dg_[i] = 0;
}

void bint::Mul(const bint& a, const bint& b, bint* c) {
  MulNaive(a, b, c);
}

void bint::MulNaive(const bint& a, const bint& b, bint* c) {
  c->Realloc(a.len_ + b.len_);
  int i, j, carry; ll mul;
  for (i = a.len_ + b.len_ - 1; i >= 0; --i) c->dg_[i] = 0;
  for (i = 0; i < a.len_; ++i) {
    carry = 0;
    for (j = 0; j < b.len_; ++j) {
      mul = ll(a.dg_[i]) * b.dg_[j] + carry + c->dg_[i + j];
      c->dg_[i + j] = mul % B;
      carry = mul / B;
    }
    for (; carry; ++j) {
      c->dg_[i + j] += carry;
      if (c->dg_[i + j] < B) carry = 0;
      else c->dg_[i + j] -= B, carry = 1;
    }
  }
  c->len_ = a.len_ + b.len_;
  c->Trim();
  c->sign_ = ((a.sign_ == b.sign_) ? 1 : -1);
  c->CorrectSign();
}

void bint::Div(const bint& a, int b, bint* c, int* rest) {
  int i; ll carry, mul;
  for (i = a.len_ - 1, carry = 0; i >= 0 ; --i) {
    mul = carry * B + a.dg_[i];
    c->dg_[i] = mul / b;
    carry = mul % b;
  }
  c->len_ = a.len_;
  c->Trim();
  b = (b >= 0) ? 1 : -1;
  c->sign_ = ((a.sign_ == b) ? 1 : -1);
  c->CorrectSign();
  if (rest) *rest = a.sign_ * carry;
}

void bint::Div(const bint& a, const bint& b, bint* c, bint* rest) {
  int x, k, testnum = b.dg_[b.len_ - 1] + 1; bint tmp;
  *rest = a;
  *c = 0;
  while (AbsLess(b, *rest)) {
    k = rest->len_ - b.len_;
    if (rest->dg_[rest->len_ - 1] >= testnum) {
      x = rest->dg_[rest->len_ - 1] / testnum;
    } else if (k) {
      --k;
      x = (ll(rest->dg_[rest->len_ - 1]) * B + rest->dg_[rest->len_ - 2])
        / testnum;
    } else {
      break;
    }
    tmp = b * x;
    tmp.Shift(k);
    rest->AbsSub(tmp);
    tmp = x;
    tmp.Shift(k);
    c->AbsAdd(tmp);
  }
  if (!AbsLess(*rest, b)) rest->AbsSub(b), c->AbsAdd(1);
  c->sign_ = ((a.sign_ == b.sign_) ? 1 : -1);
  c->CorrectSign();
  rest->sign_ = a.sign_;
  rest->CorrectSign();
}

void bint::GCD(const bint& a, const bint& b, bint* d) {
  bint aa(a), bb(b);
  aa.sign_ = 1, bb.sign_ = 1;
  *d = 1;
  while (aa != 0 && b != 0) {
    while (aa.Parity() == 0 && bb.Parity() == 0)
      aa /= 2, bb /= 2, *d *= 2;
    while (aa.Parity() == 0) aa /= 2;
    while (bb.Parity() == 0) bb /= 2;
    if (AbsLess(aa, bb)) bb -= aa;
    else aa -= bb;
  }
  if (aa == 0) *d *= bb;
  else *d *= aa;
}

char buf[128];

int main() {
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    int n;
    bint a, b, t;
    scanf("%d", &n);
    scanf("%s", buf);
    a = buf;
    scanf("%s", buf);
    b = buf;
    b -= a;
    if (b < 0) b = -b;
    t = b;
    for (int i = 2; i < n; ++i) {
      scanf("%s", buf);
      b = buf;
      b -= a;
      if (b < 0) b = -b;
      bint tmp;
      bint::GCD(t, b, &tmp);
      t.Swap(&tmp);
    }
    bint re = a % t;
    if (re > 0) {
      re = t - re;
    }
    re.Print(); printf("\n");
  }
  return 0;
}
