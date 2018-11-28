#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <memory>
using namespace std;

class numtocho {
  /* Dígitos en base 10^9 */
  static const int base = 1000000000;
  int longit, signo; /* si x >= 0, signo(x) = 1 */
  vector<int> dig;

public:
  /* Constructores (0, o a partir de un int, o long long, o a partir de una cadena) */
  numtocho() : longit(0), signo(1), dig() {}
  numtocho(int num) : longit(0), dig() {
    if (num < 0) { num = -num; signo = -1; } else signo = 1;
    if (num != 0) {
      dig.push_back(num % base);
      longit = 1;
      if (num >= base) dig.push_back(num / base), longit++;
    }
  }
  numtocho(long long num) : longit(0), dig() {
    if (num < 0) { num = -num; signo = -1; } else signo = 1;
    while (num != 0) {
      dig.push_back(num % base);
      num /= base;
      longit++;
    }
  }
  numtocho(const char *cad) : longit(0), dig() {
    if (*cad == '-') { signo = -1; cad++; } else signo = 1;
    while (*cad == '0' && *(cad + 1)) cad++;  // por si hay ceros iniciales
    if (*cad == '0') return;
    int l = strlen(cad), n, i, p;
    dig.resize(longit = (l + 8) / 9);
    for (p = 1, i = 0, n = l - 1; n >= 0; n--, i++) {
      dig[i / 9] += p * (cad[n] - '0');
      p *= 10;
      if (p == base) p = 1;
    }
    quitaceros();
  }

  /* Imprimir, pasar a char* o a string (son lo mismo) */
  void imprime() const {
    if (signo < 0) putchar('-');
    if (!longit) putchar('0');
    else {
      printf("%u", dig[longit - 1]);
      for (int n = longit - 2; n >= 0; n--) printf("%09u", dig[n]);
    }
  }

  char *c_str() const {
    int n, l;
    char *cad = new char[9 * longit + 3];
    if (!longit) { strcpy(cad, "0"); return cad; }

    if (signo < 0) { cad[0] = '-'; cad++; }
    sprintf(cad, "%u", dig[longit - 1]);
    l = strlen(cad);
    for (n = longit - 2; n >= 0; n--, l+= 9)
      sprintf(cad + l, "%09u", dig[n]);
    if (signo < 0) cad--;
    return cad;
  }

  string str() const { return auto_ptr<char>(c_str()).get(); }

private:
  /* Devuelve < 0, 0 o > 0 dependiendo de si |a| < |b|, |a| == |b| o |a| > |b| */
  int comparaabs(const numtocho &b) const {
    if (longit != b.longit) return longit - b.longit;
    for (int n = longit - 1; n >= 0; n--)
      if (int d = dig[n] - b.dig[n]) return d;
    return 0;
  }

  inline int dig2(int i) const { return i < longit ? dig[i] : 0; }
  inline void quitaceros() {
    while (longit && !dig[longit - 1]) longit--;
    dig.resize(longit);
  }

  /* this += abs(b) * signo(this) */
  const numtocho& sumaabs(const numtocho &b) {
    int carry = 0, n;
    dig.resize(longit = max(longit, b.longit));
    for (n = 0; n < longit; n++) {
      dig[n] += b.dig2(n) + carry;
      if (dig[n] >= base) { dig[n] -= base; carry = 1; } else carry = 0;
    }
    if (carry) { dig.push_back(carry); longit++; }
    return *this;
  }

  /* this -= abs(b) * signo(this), suponiendo que abs(this) >= abs(b) */
  const numtocho& restaabs(const numtocho &b) {
    int carry = 0, n;
    dig.resize(longit = max(longit, b.longit));
    for (n = 0; n < longit; n++) {
      dig[n] -= b.dig2(n) + carry;
      if (dig[n] < 0) { dig[n] += base; carry = 1; } else carry = 0;
    }
    quitaceros();
    return *this;
  }

public:
  numtocho& operator+=(const numtocho &b) {
    if (signo == b.signo) sumaabs(b);
    else if (comparaabs(b) >= 0) restaabs(b);
    else {
      numtocho c(b);
      c.restaabs(*this);
      c.signo = b.signo;
      *this = c;
    }
    return *this;
  }

  numtocho& operator-=(const numtocho &b) {
    signo *= -1;
    *this += b;
    signo *= -1;
    return *this;
  }

  int compara(const numtocho &b) const {
    if (signo < b.signo) return -1;
    if (signo > b.signo) return 1;
    int c = comparaabs(b);
    return signo >= 0 ? c : -c;
  }

  /* Multiplica dos números en O(n^2) */
  const numtocho operator*(const numtocho &b) const {
    numtocho c;
    long long d, y;
    c.dig.resize(c.longit = longit + b.longit);
    for (int i = 0; i < longit; i++)
      for (int j = 0; j < b.longit; j++) {
        int k = i + j;
        d = (long long)dig[i] * b.dig[j] + c.dig[k];
        while ((y = d / base)) { c.dig[k] = d % base; d = y + c.dig[++k]; }
        c.dig[k] = d;
      }
    c.quitaceros();
    c.signo = signo * b.signo;
    return c;
  }

  static void parte(const numtocho& a, numtocho& c, numtocho& b, int m) {
    b.dig.clear();
    c.dig.clear();
    copy(a.dig.begin(), a.dig.begin() + m, back_inserter(b.dig));
    copy(a.dig.begin() + m, a.dig.end(), back_inserter(c.dig));
    b.longit = b.dig.size();
    c.longit = c.dig.size();
  }

  const numtocho& shift(int m) {
    dig.resize(longit = dig.size() + m);
    copy(&dig[0], &dig[longit - m], &dig[m]);
    fill(&dig[0], &dig[m], 0);
    return *this;
  }

  // Multiplica en O(n^log 3)
  static numtocho karatsuba(const numtocho& num1, const numtocho& num2) {
    if (num1.longit < num2.longit) return karatsuba(num2, num1);
    int m = num1.longit / 2;
    if (m > num2.longit || m < 750) return num1 * num2;

    numtocho a, b, c, d;
    parte(num1, a, b, m);
    parte(num2, c, d, m);
    numtocho r = karatsuba(a, c), t = karatsuba(b, d), s = karatsuba(a + b, c + d).restaabs(r + t);
    r = r.shift(2 * m) + s.shift(m) + t;
    r.signo = num1.signo * num2.signo;
    return r;
  }

  /* Potencia en O(n^2 * ex^2), con ex >= 0
   * LA PRIORIDAD DE ^ ES RARA */
  const numtocho operator^(int ex) const {
    numtocho a(*this), r(1);
    r.signo = signo >= 0 || !(ex & 1) ? 1 : -1;
    while (ex) {
      if (ex & 1) { r *= a; ex--; }
      else { a *= a; ex >>= 1; }
    }
    return r;
  }

  /* División por un int (en O(n))
   * Devuelve el resto y deja el cociente en *this */
  const numtocho divide(int b) {
    int n; long long resto = 0;
    if (b < 0) { b = -b; signo = -signo; }
    for (n = longit - 1; n >= 0; n--) {
      resto = resto * base + dig[n];
      dig[n] = resto / b;
      resto %= b;
    }
    quitaceros();
    return resto;
  }

  /* División en O(n^2)
   * Devuelve el resto y deja el cociente en *this
   * Supone que signo y c.signo >= 0 !! */
  const numtocho divideabs(const numtocho &c) {
    numtocho b(c), div, resto;
    if (*this < c) { numtocho r(*this); *this = 0; return r; }
    if (b.longit == 1) return divide(b.dig[0]);

    /* Hace que el primer dígito de b sea >= base / 2, y alinea los números */
    int factor = base / (b.dig.back() + 1), d;
    *this *= factor;
    b *= factor;

    int i = longit - b.longit;
    copy(&dig[i], &dig[longit], back_inserter(resto.dig));
    resto.longit = b.longit;
    if (resto < b) { resto *= base; resto += dig[--i]; }
    for (;;) {
      /* Hace una estimación inicial del siguiente dígito de la división.
       * Al haber hecho el primer dígito de b >= base / 2, la estimación
       * se desvía como mucho en 4 unidades del valor real */
      if (resto < b) d = 0;
      else {
        long long x = resto.dig.back();
        if (resto.longit > b.longit) x = x * base + resto.dig[resto.longit - 2];
        d = x / (b.dig.back() + 1);
        resto -= b * numtocho(d);
        while (resto >= b) { resto -= b; d++; }
      }
      div.dig.push_back(d); div.longit++;
      if (!i) break;
      resto *= base;
      resto += dig[--i];
    }
    reverse(div.dig.begin(), div.dig.end());
    *this = div;
    return resto / (int)factor;
  }

  /* Devuelve el resto del mismo signo que el divisor, y el cociente en *this */
  const numtocho divide(const numtocho &c) {
    int s = signo * c.signo;
    signo = c.signo;
    numtocho resto = divideabs(c);
    signo = s;
    return resto;
  }

  /* sqrt(abs(x)) * signo(x) */
  const numtocho raiz() const {
    if (!longit) return 0;
    numtocho r, s;

    if (longit % 2 == 0) {
      double x = (double)dig[longit - 1] * base + dig[longit - 2];
      r = (numtocho)(int)sqrt(x) * ((numtocho)base ^ (longit / 2 - 1));
    } else {
      double x = dig[longit - 1];
      if (longit == 1) return (int)sqrt(x);
      else {
        x = x * base + dig[longit - 2];
        r = (numtocho)(int)sqrt(x) * ((numtocho)base ^ (longit / 2 - 1));
        r *= (int)sqrt(base);
      }
    }
    for (;;) {
      s = (r + *this / r) / 2;
      if (r == s) return r;
      r = s;
    }
  }

  /* Raíces n-simas (DE MOMENTO SOLO PARA NUMTOCHOS MENORES QUE EL MAYOR DOUBLE) */
  const numtocho raiz(int r) const {
    if (r == 2) return raiz();
    numtocho a = aprox(pow((double)*this, 1.0 / r)), b = a + a;
    a /= numtocho(2);

    while (a != b - numtocho(1)) { // a <= res < b
      numtocho m = (a + b) / 2, p = m^r;
      if (*this >= p) a = m;
      else b = m;
    }
    return a;
  }

  numtocho& niega() { signo = -signo; return *this; }

  /* Intercambia dos numtochos en tiempo constante */
  void swap(numtocho &b) {
    std::swap(longit, b.longit);
    std::swap(signo, b.signo);
    dig.swap(b.dig);
  }

  /* Syntactic sugaring */
  numtocho& operator/=(const numtocho &b) { divide(b); return *this; }
  numtocho& operator/=(int b)             { divide(b); return *this; }
  numtocho& operator*=(const numtocho &b) { return *this = *this * b; }
  numtocho& operator%=(const numtocho &b) { return *this = divide(b); }
  numtocho& operator%=(int b)             { return *this = divide(b); }

  bool operator==(const numtocho &b) const { return !compara(b); }
  bool operator!=(const numtocho &b) const { return compara(b); }
  bool operator<(const numtocho &b)  const { return compara(b) < 0; }
  bool operator<=(const numtocho &b) const { return compara(b) <= 0; }
  bool operator>(const numtocho &b)  const { return compara(b) > 0; }
  bool operator>=(const numtocho &b) const { return compara(b) >= 0; }

  const numtocho operator+(const numtocho &b) const { return numtocho(*this) += b; }
  const numtocho operator-(const numtocho &b) const { return numtocho(*this) -= b; }
  const numtocho operator-() const { return numtocho(*this).niega(); }   // menos unario
  const numtocho operator/(const numtocho &b) const { return numtocho(*this) /= b; }
  const numtocho operator/(int b) const { return numtocho(*this) /= b; }
  const numtocho operator%(const numtocho &b) const { return numtocho(*this).divide(b); }
  const numtocho operator%(int b) const { return numtocho(*this).divide(b); }

  numtocho& operator++() {         // postfix ++
    *this += 1;
    return *this;
  }

  const numtocho operator++(int) { // prefix ++
    numtocho ant = *this;
    ++(*this);
    return ant;
  }

  friend ostream& operator<<(ostream &out, const numtocho &b) { return out << b.str(); }
  friend istream& operator>>(istream &in, numtocho &b) {
    string s; in >> s;
    b = s.c_str();
    return in;
  }

  /* Castings */
  operator bool() const { return longit; }
  operator int() const { if (!longit) return 0; return dig[0]; }
  operator long long() const {
    long long a = (int)(*this);
    if (longit > 1) a += (long long)base * dig[1];
    return a;
  }
  operator double() const { // peta si es > 1e300
    char *c = c_str();
    double a;
    sscanf(c, "%lf", &a);
    return a;
  }

  // Devuelve una aproximación a un double, si es un número usual (no NaN, inf...)
  static const numtocho aprox(double a) {
    int ndig = (int)(log(a) / log((double)numtocho::base)) + 1;
    a /= pow((double)numtocho::base, ndig - 1);
    numtocho r;
    r.dig.resize(r.longit = ndig);
    r.dig[ndig - 1] = (int)a;
    return r;
  }

  static const numtocho gcd(numtocho a, numtocho b) {
    a.signo = b.signo = 1;
    if (a < b) a.swap(b);
    while (b) {
      a.swap(b);
      b %= a;
    }
    return a;
  }

  static const numtocho fact(int base, int skip, int n) {
    return base + skip > n ? numtocho(base) : karatsuba(fact(base, skip * 2, n), fact(base + skip, skip * 2, n));
  }
  static const numtocho fact(int n) { return fact(1, 1, n); }
};

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    int n;
    numtocho t[1001];

    scanf("%i", &n);
    for (int i = 0; i < n; ++i) cin >> t[i];
    sort(&t[0], &t[n]);

    numtocho g;
    bool some = false;
    for (int i = 1; i < n; ++i)
      if (t[i] != t[i - 1]) {
        if (some) g = numtocho::gcd(g, t[i] - t[i - 1]);
        else g = t[i] - t[i - 1];
        some = true;
      }
    numtocho rem = t[0] % g;
    if (rem > numtocho(0)) rem = g - rem;
    printf("Case #%i: ", numcase);
    cout << rem << endl;
  }
  return 0;
}
