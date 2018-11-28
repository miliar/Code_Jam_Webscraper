/* ****************************************************
 *  Big Integer (Full ?version)
 * ****************************************************
 *  set MAXSIZE
 * ***************************************************/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>

#include <cmath>

using namespace std;

#define MAXSIZE 1000
#define DIGIT 4
#define MAX_VALUE 10000

class Bigint {
   public:
   int sign;
   int vn;
   int v[MAXSIZE];

   Bigint() :sign(0), vn(0) { }
   
   Bigint(const int a) :sign(0), vn(0) {
      int carry = 0;

      if (a < 0) {
         sign = -1;
         carry = -a;
      }
      else if (a > 0) {
         sign = 1;
         carry = a;
      }

      for ( ; carry ; vn++) {
         v[vn] = carry%MAX_VALUE;
         carry /= MAX_VALUE;
      }
   }
   
   Bigint(const Bigint &a) :sign(a.sign), vn(a.vn) {
      for (int i = 0 ; i < vn ; i++) {
         v[i] = a.v[i];
      }
   }

   void trim() {
      for ( ; vn > 0 && !v[vn - 1] ; vn--);
      if (vn == 0)
         sign = 0;
   }

   Bigint &operator =(const Bigint &a) {
      if (this == &a) return *this;

      sign = a.sign;
      for (vn = 0 ; vn < a.vn ; vn++)
         v[vn] = a.v[vn];

      return *this;
   }

   void load (const char*str) {
      int len = (int)strlen(str);
      int pre = 0;
      for ( ; str[pre] == ' ' ; pre++);
      if (str[pre] == '-') {
         sign = -1;
         pre++;
      }
      else {
         sign = 1;
      }
      vn = (len - pre - 1)/DIGIT + 1;
      if (vn >= MAXSIZE) {
         fprintf(stderr, "Bigint Overflow!\n");
         exit(1);
      }
      for (int i = 0 ; i < vn ; i++)
         v[i] = 0;
      for (int i = pre ; i < len ; i++) {
         int pos = (len - i - 1)/DIGIT;
         v[pos] = v[pos]*10 + (str[i] - '0');
      }
      trim();
   }

   void print() const {
      if (sign == 0)
         printf("0");
      else {
         if (sign < 0) printf("-");
         printf("%d", v[vn - 1]);
         for (int i = vn - 2 ; i >= 0 ; i--)
            printf("%04d", v[i]);
      }
   }

   void println() const {
      print();
      printf("\n");
   }

   static bool abscmp(const Bigint &a, const Bigint &b) {
      if (a.vn == b.vn) {
         for (int i = a.vn - 1 ; i >= 0 ; i--) {
            if (a.v[i] == b.v[i]) continue;
            return a.v[i] < b.v[i];
         }
         return false;
      }

      return a.vn < b.vn;
   }

   bool operator <(const Bigint &a) const {
      if (sign == a.sign) {
         if (sign < 0)
            return abscmp(a, *this);
         return abscmp(*this, a);
      }

      return sign < a.sign;
   }

   bool operator ==(const Bigint &a) const {
      return !(operator<(a) || a.operator<(*this));
   }

   static Bigint add(const Bigint &a, const Bigint &b) {
      Bigint c;

      c.sign = a.sign;
      int i = 0;
      int carry = 0;
      for ( ; i < b.vn ; i++) {
         int v = a.v[i] + b.v[i] + carry;
         c.v[i] = v%MAX_VALUE;
         carry = v/MAX_VALUE;
      }
      for ( ; i < a.vn ; i++) {
         int v = a.v[i] + carry;
         c.v[i] = v%MAX_VALUE;
         carry = v/MAX_VALUE;
      }
      if (carry) {
         c.v[i++] = carry;
      }
      c.vn = i;

      return c;
   }

   static Bigint sub(const Bigint &a, const Bigint &b) {
      Bigint c;

      c.sign = a.sign;
      int i = 0;
      int carry = 0;
      for ( ; i < b.vn ; i++) {
         int v = a.v[i] - b.v[i] + carry;
         c.v[i] = (v < 0) ? (v + MAX_VALUE) : (v);
         carry = (v < 0) ? -1 : 0;
      }
      for ( ; i < a.vn ; i++) {
         int v = a.v[i] + carry;
         c.v[i] = (v < 0) ? (v + MAX_VALUE) : (v);
         carry = (v < 0) ? -1 : 0;
      }
      c.vn = i;
      c.trim();

      return c;
   }
   
   const Bigint operator +(const Bigint &a) const {
      if (sign*a.sign < 0) {
         if (abscmp(*this, a))
            return sub(a, *this);
         else
            return sub(*this, a);
      }
      else {
         if (abscmp(*this, a))
            return add(a, *this);
         else
            return add(*this, a);
      }   
   }

   const Bigint operator -(const Bigint &a) const {
      if (sign*a.sign < 0) {
         if (abscmp(*this, a))
            return add(a, *this);
         else
            return add(*this, a);
      }
      else {
         if (abscmp(*this, a))
            return sub(a, *this);
         else
            return sub(*this, a);
      }
   }

   static Bigint mul(const Bigint &a, const Bigint &b) {
      Bigint c;
      c.sign = a.sign*b.sign;

      int carry;
      c.vn = a.vn + b.vn;
      if (c.vn >= MAXSIZE) {
         fprintf(stderr, "Bigint overflow!\n");
         exit(1);
      }
      for (int i = 0 ; i < c.vn ; i++)
         c.v[i] = 0;
      for (int i = 0 ; i < a.vn ; i++) {
         if (a.v[i] == 0) continue;
         carry = 0;
         for (int j = 0 ; j < b.vn ; j++) {
            int v = a.v[i]*b.v[j] + carry;
            c.v[i + j] += v%MAX_VALUE;
            carry = v/MAX_VALUE;
         }
         c.v[i + b.vn] += carry;
      }
      carry = 0;
      int i = 0;
      for (int i = 0 ; i < c.vn ; i++) {
         c.v[i] += carry;
         carry = c.v[i]/MAX_VALUE;
         c.v[i] %= MAX_VALUE;
      }
      c.trim();

      return c;
   }

   Bigint operator *(const Bigint &a) const {
      if (sign*a.sign == 0) return Bigint();

      return mul(*this, a);
   }

   static Bigint divint(const Bigint &a, const int b, bool isMod) {
      if (b >= MAX_VALUE) fprintf(stderr, "Invalid call\n");
      Bigint c;
      int b2 = (b > 0) ? b : -b;
      if (b > 0)
         c.sign = a.sign;
      else
         c.sign = -a.sign;

      c.vn = a.vn;
      int r = 0;
      for (int i = a.vn - 1 ; i >= 0 ; i--) {
         r = MAX_VALUE*r + a.v[i];
         c.v[i] = r/b2;
         r %= b2;
      }
      c.trim();
      if (c.sign < 0 && r > 0) {
         c = c - 1;
         r = b2 - r;
      }
      if (isMod)
         return Bigint(r);
      return c;
   }

   static Bigint div(const Bigint &a, const Bigint &b, bool isMod) {
      Bigint c;
      Bigint r;

      c.sign = a.sign*b.sign;
      c.vn = a.vn - b.vn + 1;
      r.sign = 1;
      r.vn = b.vn - 1;
      for (int i = 0 ; i < r.vn ; i++)
         r.v[i] = a.v[a.vn - r.vn + i];

      for (int i = a.vn - b.vn ; i >= 0 ; i--) {
         for (int j = r.vn ; j > 0 ; j--)
            r.v[j] = r.v[j - 1];
         r.v[0] = a.v[i];
         r.vn++;
         r.sign = 1;
         if (r.vn == 1 && r.v[0] == 0) {
            r.vn = 0;
            r.sign = 0;
         }


         int lq = 0;
         int rq = MAX_VALUE - 1;

         Bigint d;
         while (lq <= rq) {
            int mq = (lq + rq)/2;
            d = b*(mq*b.sign);
            if (d < r)
               lq = mq + 1;
            else if (r < d)
               rq = mq - 1;
            else {
               rq = mq;
               break;
            }
         }
         d = b*(rq*b.sign);
         c.v[i] = rq;
         r = r - d;
      }
      c.trim();
      if (c.sign < 0 && r.sign != 0) {
         c = c - 1;
         r = (b*b.sign) - r;
      }

      if (isMod)
         return r;

      return c;
   }

   Bigint operator /(const Bigint &a) const {
      if (a.sign == 0) {
         fprintf(stderr, "Divide By Zero!\n");
         exit(1);
      }
      if (abscmp(*this, a)) return Bigint();

      if (a.vn == 1)
         return divint(*this, a.sign*a.v[0], false);
      else
         return div(*this, a, false);
   }

   Bigint operator %(const Bigint &a) const {
      if (a.sign == 0) {
         fprintf(stderr, "Divide By Zero!\n");
         exit(1);
      }
      if (abscmp(*this, a)) return Bigint(*this);

      if (a.vn == 1)
         return divint(*this, a.sign*a.v[0], true);
      else
         return div(*this, a, true);
   }

   Bigint pow(const Bigint &a) {
      if (a.sign == 0) return Bigint(1);
      if (a == 1) return Bigint(*this);
      if (a == 2) return (*this)*(*this);

      Bigint p = pow(divint(a, 2, false));
      p = p*p;
      if (a.v[0]&1)
         p = p * *this;

      return p;
   }

   static Bigint fact(const int a) {
      Bigint f(a);
      for (int i = a - 1 ; i > 0 ; i--)
         f = f*i;

      return f;
   }

 
};

Bigint gcd(Bigint a, Bigint b)
{
	Bigint c = a % b;
	while (c.sign != 0)
	{
		a = b, b = c, c = a % b;
	}
	return b;
}

int main()
{
	int T;
	cin >> T;
	char str[100];

	for (int qn = 1; qn <= T; ++qn)
	{
		int n;
		cin >> n;
		vector<Bigint> a(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> str;
			a[i].load( str );
		}

		sort(a.begin(), a.end());
		a.erase(unique(a.begin(), a.end()), a.end());
		n = a.size();

		long long ret1 = 0;

		Bigint ret2 = a[1] - a[0];
		for (int i = 2; i < n; ++i)
		{
			Bigint step = a[i] - a[i - 1];
			ret2 = gcd(ret2, step);
		}
		;
		Bigint rr = (ret2 - (a[0] % ret2)) % ret2;
		cout << "Case #" << qn << ": ";
		rr.println();
	}
}
