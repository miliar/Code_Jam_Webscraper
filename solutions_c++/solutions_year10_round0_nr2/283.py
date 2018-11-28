#include <iostream>
#include <vector>

class Int {
public:
  Int(int = 0);
  Int(unsigned int);
  Int(double);
  Int(const Int& a) : sign(a.sign), Rep(a.Rep) {};

  Int& operator=(const Int&);
  Int& operator+=(const Int&);
  Int& operator-=(const Int&);
  Int& operator*=(const Int&);
  Int& operator/=(const Int&);
  Int& operator%=(const Int&);
  Int& operator<<=(const Int&);
  Int& operator>>=(const Int&);
  Int& operator&=(const Int&);
  Int& operator|=(const Int&);
  Int& operator^=(const Int&);
  Int& operator++();
  Int& operator--();
  Int operator++(int);
  Int operator--(int);

  bool operator>(const Int&) const;

  operator bool () const {return to_bool();};
  operator int () const {return to_int();};
  operator unsigned int () const {return to_uint();};
  operator double () const {return to_double();};

  bool to_bool() const;
  unsigned int to_uint() const;
  int to_int() const;
  double to_double() const;
private:
  static const unsigned int max_use_bits = sizeof(unsigned int) * 4;
  static const unsigned int max_use = 1 << max_use_bits;

  inline unsigned int get_rep_pos(int pos) const;
  inline void set_rep_pos(int pos, int val);
  inline unsigned int get_2comp_rep_pos(int pos, bool& seen1) const;
  inline bool primitive_more_than(const Int&) const;
  inline void primitive_plus(const Int&);
  inline void primitive_minus(const Int&);
  inline void primitive_multiply(unsigned int);
  inline void primitive_shift_left();
  inline void primitive_shift_right();
  inline int primitive_divide(const Int&);

  inline void simplify();

  enum sign_type{positive = 0, negetive = 1} sign;
  std::vector<unsigned int> Rep;
};

Int operator+(const Int&, const Int&);
Int operator-(const Int&, const Int&);
Int operator*(const Int&, const Int&);
Int operator/(const Int&, const Int&);
Int operator%(const Int&, const Int&);
Int operator>>(const Int&, const Int&);
Int operator<<(const Int&, const Int&);
Int operator-(const Int&);
Int operator&(const Int&, const Int&);
Int operator|(const Int&, const Int&);
Int operator^(const Int&, const Int&);
Int operator~(const Int&);
bool operator<(const Int&, const Int&);
bool operator<=(const Int&, const Int&);
bool operator>=(const Int&, const Int&);
bool operator==(const Int&, const Int&);
bool operator!=(const Int&, const Int&);


std::ostream& operator<<(std::ostream&, const Int&);
std::istream& operator>>(std::istream&, Int&);


template<class T>
Int operator+(const Int& a, const T& b)
{
  return a + Int(b);
}

template<class T>
Int operator+(const T& a, const Int& b)
{
  return Int(a) + b;
}

template<class T>
Int operator-(const Int& a, const T& b)
{
  return a - Int(b);
}

template<class T>
Int operator-(const T& a, const Int& b)
{
  return Int(a) - b;
}

template<class T>
Int operator%(const Int& a, const T& b)
{
  return a % Int(b);
}

template<class T>
Int operator%(const T& a, const Int& b)
{
  return Int(a) % b;
}

template<class T>
Int operator/(const Int& a, const T& b)
{
  return a / Int(b);
}

template<class T>
Int operator/(const T& a, const Int& b)
{
  return Int(a) / b;
}

template<class T>
Int operator*(const T& a, const Int& b)
{
  return Int(a) * b;
}

template<class T>
Int operator*(const Int& a, const T& b)
{
  return a * Int(b);
}

template<class T>
bool operator>(const T& a, const Int& b){
  return Int(a) > b;
}

template<class T>
bool operator>(const Int& a, const T& b){
  return a > Int(b);
}

template<class T>
bool operator<(const T& a, const Int& b){
  return Int(a) < b;
}

template<class T>
bool operator<(const Int& a, const T& b){
  return a < Int(b);
}

template<class T>
bool operator>=(const T& a, const Int& b){
  return Int(a) >= b;
}

template<class T>
bool operator>=(const Int& a, const T& b){
  return a >= Int(b);
}

template<class T>
bool operator<=(const T& a, const Int& b){
  return Int(a) <= b;
}

template<class T>
bool operator<=(const Int& a, const T& b){
  return a <= Int(b);
}

template<class T>
bool operator==(const Int& a, const T& b){
  return a == Int(b);
}

template<class T>
bool operator==(const T& a, const Int& b){
  return Int(a) == b;
}

template<class T>
bool operator!=(const Int& a, const T& b){
  return a != Int(b);
}

template<class T>
bool operator!=(const T& a, const Int& b){
  return Int(a) != b;
}
