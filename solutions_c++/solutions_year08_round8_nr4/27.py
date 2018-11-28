#include <iostream>
#include <vector>

typedef unsigned int num_t;

template <num_t n>
class InvTable {
public:
  InvTable() {
    table[0] = 0;
    for (num_t i = 1; i < n; i++) {
      for (num_t j = 1; j < n; j++) {
        if ((i * j) % n == 1) {
          table[i] = j;
          break;
        }
      }
    }
  }
  inline num_t operator[] (num_t v) const { return table[v]; }
private:
  num_t table[n];
};

template <num_t n>
class RemainderClass {
public:
  inline RemainderClass(): v(0) {}
  inline RemainderClass(num_t val): v(val % n) {}

  // Addition, subtraction
  inline RemainderClass operator- () const
  { return RemainderClass(n - v); }
  inline RemainderClass &operator+= (const RemainderClass &that)
  { v = (v + that.v) % n;
    return *this;
  }
  inline RemainderClass &operator-= (const RemainderClass &that)
  { v = (v + n - that.v) % n; }
  inline const RemainderClass operator+ (const RemainderClass &that) const
  { return RemainderClass(*this) += that; }
  inline const RemainderClass operator- (const RemainderClass &that) const
  { return RemainderClass(*this) -= that; }

  // Multiplication
  inline RemainderClass &operator*= (const RemainderClass &that)
  { v = (v * that.v) % n;
    return *this;
  }
  inline const RemainderClass operator* (const RemainderClass &that) const
  { return RemainderClass(*this) *= that; }

  // Division
  inline RemainderClass inv() const { return invtable[v]; }
  inline RemainderClass &operator/= (const RemainderClass &that)
  { v = (v * invtable[that.v]) % n; }
  inline const RemainderClass operator/ (const RemainderClass &that) const
  { return RemainderClass(*this) /= that; }

private:
  num_t v;
  static InvTable<n> invtable;

  template <num_t nn>
  friend std::ostream &operator<< (std::ostream &s, RemainderClass<nn> v);
};

template <num_t n>
std::ostream &operator<< (std::ostream &s, RemainderClass<n> v)
{ return s << v.v; }

typedef RemainderClass<30031> rem_t;

template <num_t n>
InvTable<n> RemainderClass<n>::invtable;

rem_t fac(num_t n)
{
  rem_t res = 1;
  for (num_t i = 2; i <= n; i++)
    res *= i;
  return res;
}

void calc()
{
  size_t n, k, p;
  std::cin >> n >> k >> p;

  std::vector<rem_t> comb(1 << p, 0);
  size_t i = k;
  comb[(1 << k) - 1] = 1;
  for (; i < n; i++) {

    //std::cerr << "Iteration" << i << std::endl;
    //for (int m = 0; m < (1 << p); m++) {
    //  std::cerr << "mask=" << m << ": " << comb[m] << std::endl;
    // }

    std::vector<rem_t> newcomb(1 << p, 0);
    for (int m = 0; m < (1 << (p - 1)); m++) {
      for (size_t bit = 0; bit < p; bit++) {
	if (m & (1 << bit))
	  newcomb[(m << 1) & ~(1 << (bit + 1)) | 1] += comb[m];
      }
      //newcomb[m << 1] += comb[m];
    }
    for (int m = (1 << (p - 1)); m < (1 << p); m++) {
      newcomb[(m << 1) & ((1 << p) - 1) | 1] += comb[m];
    }
    comb.swap(newcomb);
  }

  //std::cerr << "Final" << std::endl;
  // for (int m = 0; m < (1 << p); m++) {
  //   std::cerr << "mask=" << m << ": " << comb[m] << std::endl;
  // }

  std::cout << comb[(1 << k) - 1] << std::endl;
}

int main()
{ 
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": ";
    calc();
  }
}

