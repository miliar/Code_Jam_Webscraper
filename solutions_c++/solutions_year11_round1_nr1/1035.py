#include "Common.h"
#include <assert.h>

Sieve::Sieve(s64 num)
	: _prime(NULL)
	, _array(NULL)
	, _imax(0)
	, _num(num)
{
	_num = num;
	u32 m = 8*(u32)(num/30+1);
	_prime = new u8 [m];
	memset(_prime, 0xFF, m);
	u32 sq = (u32)sqrt((double)num) + 1;
	for (u64 i = 7; i <= sq; i += 2) {
		if (!IsPrime(i)) continue;
		s64 j = 7 * i;
		while (j <= num) {
			s32 q = p[j%30];
			if (q >= 0) {
				_prime[j/30] &= ~((u8)(1 << q));
			}
			j += 2 * i;
		}
	}
}

s32 Sieve::p[30] = {
	-2,  0, -1, -1, -2, -1, -2,  1, -2, -2,
	-2,  2, -2,  3, -2, -2, -2,  4, -2,  5,
	-2, -2, -2,  6, -2, -2, -2, -2, -2,  7
};

bool Sieve::IsPrime(u64 num)
{
	s32 q = p[num%30];
	if (num < 30) return q != -2 && num != 1;
	if (q < 0) return false;
	return (_prime[num/30] & (1<<q)) > 0;
};

u64 * Sieve::Array(u32 & imax)
{
	size_t prmax = (size_t)(1.2 * _num / log((double)_num));
	if (_array == NULL) {
		_array = new u64 [prmax];
		imax = 0;
		for (u64 j = 2; j < _num; j ++) {
			if (IsPrime(j)) {
				_array[imax ++] = j;
				if (imax >= prmax) break;
			}
		}
		_imax = imax;
	}
	return _array;
}

u64 * Sieve::Array1(u32 & imax)
{
	size_t prmax = (size_t)(1.2 * _num / log((double)_num));
	if (_array == NULL) {
		_array = new u64 [prmax];
		imax = 0;
		for (u64 j = 2; j < _num; j ++) {
			if (j%4==1 && IsPrime(j)) {
				_array[imax ++] = j;
				if (imax >= prmax) break;
			}
		}
		_imax = imax;
	}
	return _array;
}

u32 Sieve::Array2(u32 & imax, u32 *p)
{
	u32 r=0;
	size_t prmax = (size_t)(1.2 * _num / log((double)_num));
	if (p == NULL) {
		p = new u32 [prmax];
		imax = 0;
		for (u64 j = 2; j < _num; j ++) {
			if (IsPrime(j)) {
				if (j < 2000000000) {
					p[imax ++] = (u32)j;
				} else {
					if (r!=0) r=imax;
					p[imax ++] = (u32)(j - 2000000000);
				}
				if (imax >= prmax) break;
			}
		}
		_imax = imax;
	}
	return r;
}

bool Sieve::Factorize(u64 n, vector<Exp> & v)
{
	if (_array == NULL) return false;
	u64 root = (u64)sqrt((double)n) + 1;
	for (u64 i = 0; _array[i] <= root; i ++) {
		if (n % _array[i] == 0) {
			Exp f;
			f.b = _array[i];
			f.e = 1;
			n /= _array[i];
			while (n % _array[i] == 0) {
				f.e ++;
				n /= _array[i];
			}
			v.push_back(f);
			if (n == 1) break;
			root = (u64)sqrt((double)n) + 1;
		}
		if (i + 1 == _imax) return false;
	}
	if (n != 1) {
		Exp f = { n, 1 };
		v.push_back(f);
	}
	return true;
}


bool Sieve::Factorize2(u64 n, vector<Exp> & v)
{
	if (_array == NULL) return false;
	u64 root = (u64)sqrt((double)n) + 1;
	for (u64 i = 0; _array[i] <= n; i ++) {
		if (n % _array[i] == 0) {
			Exp f;
			f.b = i;
			f.e = 1;
			n /= _array[i];
			while (n % _array[i] == 0) {
				f.e ++;
				n /= _array[i];
			}
			v.push_back(f);
			if (n == 1) break;
			root = (u64)sqrt((double)n) + 1;
		}
		if (i + 1 == _imax) return false;
	}
	if (n != 1) {
		Exp f = { n, 1 };
		v.push_back(f);
	}
	return true;
}

//Sieve::Sieve(u32 begin, u32 end)
//	: _prime(NULL)
//{
//	u32 j;
//	u32 num = end - begin + 1;
//	_prime = new bool [num];
//	memset(_prime, true, num);
//	u32 max = (u32)sqrt((double)end) + 1;
//	for (u32 i = 2; i <= max; i ++) {
//		j = (begin / i + 1) * i;
//		if (j == i) j += i;
//		while (j <= end) {
//			_prime[j - begin] = false;
//			j += i;
//		}
//	}
//}

/*
	Express prime p as a sum of squared two integers, based on Serret's algorithm.
	See p.122 of "The higher arithmetic: an introduction to the theory of numbers".
*/
bool SquareSum::Serret(u64 p, Twin &t)
{
	if (p == 2) {
		t.x = t.y = 1;
		return true;
	}
	if (p % 4 != 1) return false;
	map<u64, Twin>::iterator it = cache.find(p);
	if (it != cache.end()) {
		t = it->second;
		return true;
	}
	t.x = p;
	t.y = Residue(p, p - 1);
	if (2 * t.y >= p) t.y = p - t.y;
	vector<u64> v;
	while (t.y > 0) {
		v.push_back(t.x / t.y);
		u64 y_tmp = t.y;
		t.y = t.x - (t.x / t.y) * t.y;
		t.x = y_tmp;
	}
	t.x = v[v.size() / 2];
	t.y = 1;
	for (vector<u64>::size_type i = v.size() / 2 + 1; i < v.size(); i ++) {
		u64 x_tmp = t.x;
		t.x = v[i] * t.x + t.y;
		t.y = x_tmp;
	}
	if (2 * t.x >= p) {
		t.x = p - t.x;
	}
	t.y = Sqrt(p - t.x * t.x);
	if (t.y < t.x) {
		u64 tmp = t.x;
		t.x = t.y;
		t.y = tmp;
	}
	cache.insert(pair<u64, Twin>(p, t));
	return true;
}

bool SquareSum::Expand(u64 a, u64 b, u64 c, u64 d, vector<Twin> *u)
{
	Twin t;
	if (a * c >= b * d)
		t.x = a * c - b * d;
	else
		t.x = b * d - a * c;
	t.y = a * d + b * c;
	if (t.y < t.x) {
		u64 tmp = t.x;
		t.x = t.y;
		t.y = tmp;
	}
	//if (t.x==0 || t.y==0) return false;
	for (vector<Twin>::size_type i = 0; i < u->size(); i ++) {
		if (u->at(i).x == t.x) return false;
	}
	u->push_back(t);
	return true;
}

/* 
	Find all twins x>0 and y>0 which satisfy x^2+y^2=n (x<y).
	n is the form of exponent expression.
*/
bool SquareSum::Find(vector<Exp> &v, vector<Twin> &u)
{
	u64 n = 0;
	vector<u64> v1, v2;
	for (vector<Exp>::size_type i = 0; i < v.size(); i ++) {
		if (v[i].b == 2 || v[i].b % 4 == 1) {
			for (u64 j = 0; j < v[i].e; j ++) v1.push_back(v[i].b);
			n += v[i].e;
		} else {
			if (v[i].e % 2 != 0) return false;
			for (u64 j = 0; j < v[i].e / 2; j ++) v2.push_back(v[i].b);
		}
	}
	if (v1.empty()) return false;
	vector<Twin> w, *u1, *u0, *u_tmp;
	if (n % 2 == 1) {
		u0 = &u;	u1 = &w;
	} else {
		u0 = &w;	u1 = &u;
	}
	Twin t1;
	if (!Serret(v1[0], t1)) {
		t1.x = t1.y = v1[0];
	}
	u0->push_back(t1);
	for (vector<u64>::size_type i = 1; i < v1.size(); i ++) {
		if (Serret(v1[i], t1)) {
			for (vector<Twin>::size_type j = 0; j < u0->size(); j ++) {
				Expand(u0->at(j).x, u0->at(j).y, t1.x, t1.y, u1);
				Expand(u0->at(j).x, u0->at(j).y, t1.y, t1.x, u1);
			}
		}
		u_tmp = u0;
		u0 = u1;
		u1 = u_tmp;
		u1->clear();
	}
	for (vector<u64>::size_type i = 0; i < v2.size(); i ++) {
		for (vector<Twin>::size_type j = 0; j < u0->size(); j ++) {
			u0->at(j).x *= v2[i];
			u0->at(j).y *= v2[i];
		}
	}
	return true;
}

/*
	Get next number. Returned value 0 means the end of the enumeration.
*/
u64 NumGenerator::Next(void) {
	while (true) {
		u64 nnew = _n;
		if (_i < _imax) {
			nnew = _n * _p[_i];
		}
		if (_i < _imax && nnew <= _nmax) {
			_n = nnew;
			if (_e == 0) {
				Exp ex = { _p[_i], 1 };
				_v.push_back(ex);
				_u.push_back(_i);
			} else {
				_v.back().e ++;
			}
			_e ++;
			break;
		}
		if (_v.size() < 1) return 0;
		_e = 0;
		_n /= _p[_u.back()];
		_i = _u.back() + 1;
		if (_v.back().e == 1) {
			_v.pop_back();
			_u.pop_back();
		} else {
			_v.back().e --;
		}
	}
	return _n;
}

/*
	Return (a|n).
	(a|n) = 0  if a = 0 (mod p)
		  = +1 if x^2 = a (mod p) for some x
		  = -1 if there is no such x
*/
s64 Jacobi(s64 a, s64 n)
{
	s64 t = 1;
	while (a != 0) {
		while (a % 2 == 0) {
			a = a / 2;
			if (n % 8 == 3 || n % 8 == 5) t = -t;
		}
		s64 tmp = a;	a = n;	n = tmp;
		if (a % 4 == 3 && n % 4 == 3) t = -t;
		a = a % n;
	}
	if (n == 1) return t;
	return 0;
}

u64 ExtGcd( u64 a, u64 b, u64& x, u64& y ) {
	if ( b == 0 ) {
		x = 1; y = 0; return a;
	}
	u64 g = ExtGcd( b, a % b, y, x );
	y -= a / b * x;
	return g;
}

/*
	Find x who satisfies x*n=1 (mod p).
*/
u64 InvMod(u64 n, u64 p) {
	u64 x, y;
	return ExtGcd ( n, p, x, y ) == 1 ? ( x + p ) % p : 0;
}

/* 
	Return a^n (mod p)
*/
u64 PowMod(u64 a, u64 n, u64 p) {
	if (n == 0) return 1;
	if (n % 2 == 0) return PowMod( a * a % p, n / 2, p);
	return a * PowMod( a, n - 1, p ) % p;
}

/*
	Return sqrt n (mod p).
*/
u64 SqrtMod(u64 n, u64 p) {
	u64 w = 2, s = 0, q = p - 1, m = InvMod( n, p );
	while ( Jacobi ( w, p ) != -1 ) w++;
	while ( q % 2 == 0 ) q /= 2, s++;
	u64 v = PowMod( w, q, p );
	u64 r = PowMod( n, (q + 1) / 2, p );
	do {
		u64 i = 0, u = (u64) r * r * m % p;
		while ( u % p != 1 ) u = (u64) u * u % p, i++;
		if ( i == 0 ) return r;
		r = r * PowMod (v, 1 << (s - i - 1), p) % p;
	} while ( true );
}


//u64 Residue(u64 p, u64 n)
//{
//	u64 w = 2;
//	for (; w <= p / 2; w ++) {
//		if (Jacobi(w, p) == -1) break;
//	}
//	if (w > p / 2) return 0;
//	u64 q = p - 1;
//	u64 s = 0;
//	while (q % 2 == 0) {
//		s ++;
//		q /= 2;
//	}
//	u64 r = PowMod(n, (q+1)/2, p);
//	u64 v = PowMod(w, q, p);
//	while (true) {
//		u64 tmp = (r * r * InvMod(n, p)) % p;
//		u64 i = 0;
//		for (; i <= s - 1; i ++) {
//			if (tmp % p == 1) break;
//			tmp = (tmp * tmp) % p;
//		}
//		if (i == 0) break;
//		r = (r * PowMod( v, pow(2LL, s-i-1), p )) % p;
//	}
//	r %= p;
//	if (r > p / 2) r = p - r;
//	return r;
//}

/*
	Find x who satisfies x*x=n (mod prime p) by Shanks-Tonelli algorithm.
	http://www.codecodex.com/wiki/Shanks-Tonelli_algorithm
*/	
u64 Residue(u64 prime, u64 arg)
 {
	u64 y = 2, b, t, result;
	u64 r = 0, m, q = prime - 1;
	if (Jacobi(arg, prime) == -1) return -1;
	while(Jacobi(y, prime) != -1) y ++;
	result = prime - 1;
	while (q % 2 == 0) {
		r ++;
		q /= 2;
	}
	result >>= r;
	y = PowMod(y, result, prime);
	result >>= 1;
	b = PowMod(arg, result, prime);
	result = arg * b;
	result = result % prime;
	b = result * b;
	b = b % prime;
	while(b!=1) {   
		t = b * b;
		t = t % prime;
		for (m = 1; t!=1; m++) {
			t = t * t;
			t = t % prime;
		}
		t=0;
		t |= (1ULL << (r-m-1));
		t = PowMod(y, t, prime);
		y = t*t;
		r = m;
		result = result * t;
		result = result % prime;
		b = b * (y%prime);
		b = b %prime;
	}  
	return result;
 }


/*
	ペル方程式 x^2-D*y^2=+-1 を解く.
	If pstv is set to true, solve x^2-D*y^2=+1, else x^2-D*y^2=-1.
*/
bool Pell(u64 D, bool pstv, u64 &x, u64 &y)
{
	x = 0, y = 1;
	vector<u64> v;
	double b = sqrt((double)D);
	do {
		u64 a = (u64)((x + b) / y);
		v.push_back(a);
		u64 x_new = a*y-x;
		u64 y_new = (D-(a*y-x)*(a*y-x)) / y;
		x = x_new;
		y = y_new;
	} while (y != 1);
	x = 1, y = 0;
	for (vector<u64>::size_type i = 0; i < v.size(); i ++) {
		u64 x_tmp = x;
		x = v[i] * x + y;
		y = x_tmp;
	}
	if (pstv) {
		y = (x*x-1)%D==0 ? Sqrt((x*x-1)/D) : 0;
		if (y == 0) {
			y = Sqrt((x*x+1)/D);
			u64 x_new = x*x + D*y*y;
			u64 y_new = 2*x*y;
			x = x_new;
			y = y_new;
		}
	} else {
		y = (x*x+1)%D==0 ? Sqrt((x*x+1)/D) : 0;
		if (y == 0) return false;
	}
	return true;
}

/*
	一次合同式 a*x=b (mod n: 正整数) の解を x=r (mod m) の形で求める.
	解が存在すれば true, しなければ false を返す.
	参考: http://homepage1.nifty.com/docs/algo/c/congruence.html
*/
bool LinearCongruence(s64 a, s64 b, s64 n, s64 &m, s64 &r)
{
	assert(a != 0);
	assert(n > 0);
	s64 x = a, y = n, z = b, w = 0, s, tmp;
	while ((s = x % y) != 0) {
		r = x / y;
		x = y;
		y = s;
		tmp = w;
		w = z - r * w;
		z = tmp;
	}
	if (b % y != 0) return false;
	r = (w / y) % (n / y);
	if (r < 0) r += n / y;
	m = n / y;
	return true;
}


/*
	二次合同式 a*x^2+b*x+c=0 (mod p: 素数) の解を x=r (mod m) の形で求める.
	返り値は解の個数(0-2). 0 なら解は存在しない. 1 なら x=r1 (mod m), 2 なら x=r1,r2 (mod m) が解.
	p が素数か否かのチェックはしていません.
*/
u32 QuadraticCongruence(s64 a, s64 b, s64 c, s64 p, s64 &m, s64 &r1, s64 &r2)
{
	assert(a != 0);
	assert(p > 0);
	if (a < 0) {
		a = -a;	b = -b;	c = -c;
	}
	s64 s = b * b - 4 * a * c;
	while (s < 0) s += p;
	s64 j = Jacobi(s, p);
	u32 ret;
	if (j == -1) {
		ret = 0;
	} else if (j == 0) {
		ret = 1;
		LinearCongruence(2 * a, -b, p, m, r1);
	} else {
		ret = 2;
		s64 r = Residue(p, s);
		LinearCongruence(2 * a, -b + r, p, m, r1);
		LinearCongruence(2 * a, -b - r, p, m, r2);
	}
	return ret;
}

/*
	連立一次合同式を中国剰余定理を用いて解く.
	x=b[i] (mod a[i]) を満たす x を x=p (mod q) の形で求める.
	x=2 (mod 3), x=
*/
void ChineseRemainderTheorem(s64 *a, s64 *b, s32 n, s64 &p, s64 &q)
{
	s64 c, d, m, s;
	q=b[0], p=a[0];
	for (s32 i = 1; i < n; i ++) {
		c = a[i] - p;
		d = b[i];
		LinearCongruence(q, c, d, m, s);
		p += q * s;
		q *= m;
		//cout << p << " " << q << endl;
	}
}

void Factorize(u64 num, vector<u64> & res)
{
	u64 root = (u64)sqrt((double)num) + 1;
	for (u64 i = 2; i <= root && num != 1;) {
		if (num % i == 0) {
			num /= i;
			res.push_back(i);
			continue;
		}
		i ++;
	}
	if (num != 1) res.push_back(num);
}

/*
	素因数分解された結果から約数のリストを得る
*/
void Divisor(vector<Exp> &v, vector<u64> &u)
{
	if (v.empty()) return;
	DivisorSub(1, 0, v, u);
}

void DivisorSub(u64 n, u32 i, vector<Exp> &v, vector<u64> &u)
{
	u64 tmp = n;
	if (i == v.size() - 1) {
		FOR(j,0,v[i].e+1) {
			u.push_back(tmp);
			tmp *= v[i].b;
		}
	} else {
		FOR(j,0,v[i].e+1) {
			DivisorSub(tmp, i + 1, v, u);
			tmp *= v[i].b;
		}
	}
}

void Divisor(u64 num, vector<u64> & res)
{
	for (u64 i = 2; i <= num; i ++) {
		if (num % i == 0) {
			res.push_back(i);
		}
	}
}

u64 Pan(u32 from, u32 to, u32 seed)
{
	bool f[10];
	memset(f, 0, sizeof(bool)*10); 
	u64 ret = 0;
	u32 val = seed;
	for (u32 c = to - from + 1; c >= 1; c --) {
		u32 j = 0;
		for (u32 k = 0; k <= to - from; k ++) {
			if (f[k]) continue;
			if (j == val % c) {
				f[k] = true;
				ret = 10 * ret + k + from;
				break;
			}
			j++;
		}
		val /= c;
	}
	return ret;
}

u64 Can(u32 from, u32 to, u32 num, u32 seed)
{
	bool f[10];
	memset(f, 0, sizeof(bool)*10); 
	u64 ret = 0;
	u32 val = seed;
	for (u32 c = num; c >= 1; c --) {
		u32 j = 0;
		for (u32 k = 0; k <= to - from; k ++) {
			if (f[k]) continue;
			if (j == val % c) {
				f[k] = true;
				ret = 10 * ret + k + from;
				break;
			}
			j++;
		}
		val /= c;
	}
	return ret;
}

s64 GCD(s64 x, s64 y){
	return x ? GCD(y % x, x) : y;
}

/*
	桁数を得る
	9->1, 10->2
*/
u32 digit10(u64 x)
{
	u32 ret = 0;
	while (x > 0) {
		x /= 10;
		ret ++;
	}
	return ret;
}

s64 Pow(s64 base, s64 exp)
{
	s64 ret = 1;
	for (s64 i = 0; i < exp; i ++) ret *= base;
	return ret;
}

void PrintFactor(u64 num)
{
	u32 root = (u32)sqrt((double)num) + 1;
	printf("%d =", num);
	for (u32 i = 2; i < root; i ++) {
		if (num % i == 0) {
			printf(" %d", i);
			num /= i;
		}
	}
	printf("\n");
}

/*
	第 index 位の桁を得る
*/
u32 Digit(u64 num, u32 index)
{
	for (u32 i = 0; i < index - 1; i ++) {
		num /= 10;
	}
	return num % 10;
}

/*
	Return sqrt(n). Ex:10->3
*/
u64 Sqrt(u64 n)
{
//	return (u64)( sqrt((long double)n + DEL) );
  u64 s, t;

  if (n <= 0) return 0;

  s = 1;  t = n;
  while (s < t) {  s <<= 1;  t >>= 1;  }
  do {
    t = s;
    s = (n / s + s) >> 1;
  } while (s < t);

  return t;
}

bool IsSquare(s64 x) {
	if (x < 0) return false;
	u64 y = (u64)sqrt((double)x + DEL);
	return y*y == x;
}

//bint u64tobint(u64 n) {
//	char tmp[100];
//	_ui64toa_s(n, tmp, 100, 10);
//	bint y(tmp, 10);
//	return y;
//}
