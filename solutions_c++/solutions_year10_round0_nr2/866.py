#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define for0(i,n) for (int i = 0; i < (n); ++i)
#define PB push_back
#define SS size()

///BIGINT
const int BASE = 1000; //>> and << assume base 1000.

/*struct bigint
{
  int sign;
  vector<int> a;
  
  bigint():sign(1) {}
  
  bigint(int x):sign(x<0 ? -1 : 1) {
    x = abs(x);
    do {a.PB(x % BASE);} while((x /= BASE)>0);
  }
  
  bigint(string s):sign(s[0]=='-' ? -1 : 1) {
    int pow10[] = {1, 10, 100};
    int len = sign ? s.SS : s.SS - 1;
    for (int i = 0, d = 0; i < len; ++i)
    {
      d += int(s[s.SS-i-1] - '0') * pow10[i%3];
      if (i % 3 == 2 || i == len-1) a.PB(d), d=0;
    }
  }
    
  int& operator[](int i)
    { while(i >= SS) a.PB(0); return a[i]; }
    
  int operator[](int i) const
    { return i < SS ? a[i] : 0; }
    
  bigint operator-() const
    { bigint x = *this; x.sign *= -1; return x; }
    
  int size() const { return a.SS; }
  
  void fix()
  	{ while(SS > 0 && a.back() == 0) a.pop_back(); }
};

/// I/O
ostream& operator<<(ostream& out, bigint x) {
  x.fix();
  if (x.SS == 0) return out << 0;
  out << x[x.SS-1] * x.sign;
  for (int i = x.SS-2; i >= 0; --i)
    out << setw(3) << setfill('0') << x[i]; 
  return out;  // this ^ needs <iomanip>
}

istream& operator>>(istream& in, bigint& x) {
  string s;
  in >> s;
  x = bigint(s);
  return in;
}
bigint operator-(bigint a, const bigint& b);

///EQUALS
bool operator==(bigint a, bigint b)
{
	a.fix(); b.fix();
    return a.a == b.a && a.sign == b.sign;
}

///LESS THAN
bool operator<(bigint a, bigint b)
{
  a.fix(); b.fix();
  for (int i = max(a.SS, b.SS) - 1; i >= 0; --i)
  {
    if (a[i] < b[i]) return true;
    if (b[i] < a[i]) return false;
  }
  return false;
}

///ABSOLUTE VALUE
bigint abs(const bigint& x)
{
  return x < 0 ? -x : x;
}

///ADD
bigint operator+(bigint a, const bigint& b)
{
  if (a.sign != b.sign) return a-(-b);
  for(int i=0, c=a[i]/BASE; i<b.SS || c>0; ++i)
    c = (a[i] += b[i]+c)/BASE, a[i] %= BASE;
  return a;
}

///SUBTRACT
bigint operator-(bigint a, const bigint& b)
{
  if (a.sign != b.sign) return a+(-b);
  if (abs(a) < abs(b)) return -(b-a);
  for(int i=0, c=0; i<b.SS || c>0; ++i)
  {
  	a[i] -= b[i] + c;
  	if (a[i] < 0)
  		a[i] += BASE, c = 1;
  	else
  		c = 0;
  }
  return a;
}

///MULTIPLY
bigint operator*(const bigint& a, const bigint& b)
{
  if (a==0 || b==0) return 0;
  bigint p;
  p.sign = a.sign * b.sign;
  for0 (i, a.SS)
  {
    for0 (j, b.SS)
      p[i+j] += a[i] * b[j];
    p = 0 + p; // !!!
    // MUST be 0+p to fix digit overflow!!!
  }
  return p;
}

///FAST HALF
bigint half(bigint x)
{
  for0 (i, x.SS)
  {
    if (i != 0 && x[i] % 2 == 1) 
      x[i-1] += BASE / 2;
    x[i] /= 2;
  }
  return x;
}

///DIVIDE
bigint operator/(const bigint& a, const bigint& b)
{
  if (b == 0) cerr << "bigint dbz" << endl;
  if (a.sign == -1) return -((-a)/b);
  if (b.sign == -1) return -(a/(-b));
  if (a < b) return 0;
  
  bigint q = half(a+1);
  q.sign = a.sign / b.sign;
  for (bigint u(0), v(a+1); u+1 < v; q=half(u+v))
    (a < q*b ? v : u) = q;
  return q;
}

///SQRT
bigint sqrt(const bigint& a)
{
  bigint r = half(a+1);
  r.sign = a.sign;
  for (bigint u(0), v(a+1); u+1 < v; r=half(u+v))
    (a < r*r ? v : u) = r;
  return r;
}

///MOD
bigint operator%(const bigint& a, const bigint& b) {
  //cerr << a << ' ' << b << ' ' << a/b << ' ' << (a-b*(a/b)) << endl;
  return a - b * (a / b);
}

///GCD
bigint gcd(const bigint& a, const bigint& b) {
  return b == 0 ? a : gcd(b, a % b);
}

///LCM
bigint lcm(const bigint& a, const bigint& b) {
  return a * b / gcd(a, b);
}
*/


#define bigint long long

vector<bigint> t;

long long gcd(const long long& a, const long long& b) {
  //cerr << a << ' ' << b << endl;
  return b == 0 ? a : gcd(b, a % b);
}


int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; ++c)
	{
		int n;
		cin >> n;
		t.clear();
		for (int i = 0; i < n; ++i)
		{
			bigint b;
			cin >> b;
			t.push_back(b);
		}
		sort(all(t));
		//cout << "here" << endl;
		bigint diff = t[1] - t[0];
		//cout << t[1] << ' ' << t[0] << ' ' << diff << endl;
		for0 (i, n)
			for0 (j, n)
				if (t[i] < t[j])
					diff = gcd(diff, t[j] - t[i]);
	//cout << diff << endl;
		bigint add = 0;
	start:
		bigint g = t[0];
		//cout << "here" << endl;
		for (int i = 0; i < n && !(diff == 0); ++i)
		{
			//cout << t[i] << endl;
			if (!(t[i] % diff == 0))
			{
				bigint rem = t[i] % diff;
				bigint a = diff - rem;
				add = add + a;
				for0 (j, n) t[j] = t[j] + a;
				goto start;
			}
		}
		
		cout << "Case #" << c << ": ";
		cout << add;
		cout << endl;
	}
}