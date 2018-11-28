/*
BigInt number class provided by M Phillips - 2005.

This code is provided as is with no warranties or guarantees of
any kind.

Please send an email to M Phillips (mbp2@i4free.co.nz)
  - if you use this file in a released product, or
  - if you find any bugs, or
  - if you have any suggestions
*/
#ifndef BIG_INT_H
#define BIG_INT_H

#include <iostream>
#include <limits>
#include <utility>
#include <sstream>
#include <string>
#include <climits>

// compiletime asserts (failure results in error C2118: negative subscript)
#ifndef C_ASSERT
#define C_ASSERT(e) typedef char __C_ASSERT__[(e)?1:-1]
#endif

// Store temporaries as static unless required to be re-enerant
#define MULTI_THREAD

// If using a big endian processor, define BIG_ENDIAN
//#define BIG_ENDIAN

#if defined(MULTI_THREAD)
	#define BIGINT_TEMPORARY
#else
	#define BIGINT_TEMPORARY static
#endif
#define BASE_MAX (std::numeric_limits<typename ubigint<BIGINT_TOTAL_BITS>::BIGINT_BASE>::max)()

template<int> class sbigint;

template <int BIGINT_TOTAL_BITS>
class ubigint
{
protected:
	typedef unsigned long BIGINT_BASE;  // The base type.

	enum {
		BASE_BITS = sizeof(BIGINT_BASE) * CHAR_BIT,
		HALF_BASE_BITS = (sizeof(BIGINT_BASE) * CHAR_BIT) / 2,
		HIGH_BASE_BIT = 1 << (BASE_BITS-1),
		LOW_MASK = (1<<HALF_BASE_BITS)-1,
		BIGINTSIZE = (BIGINT_TOTAL_BITS / BASE_BITS),
#ifdef BIG_ENDIAN
		LSBINDEX = BIGINTSIZE-1,
		MSBINDEX = 0,
#else
		LSBINDEX = 0,
		MSBINDEX = BIGINTSIZE-1,
#endif
	};

#ifdef BIG_ENDIAN
	#define BASE_INDEX(x) (LSBINDEX - (x))
	#define FORWARDS_LOOP(x) for (int x = BIGINTSIZE-1; x >= 0; --x)
	#define BACKWARDS_LOOP(x) for (int x = 0; x < BIGINTSIZE; ++x)
#else
	#define BASE_INDEX(x) (x)
	#define BACKWARDS_LOOP(x) for (int x = BIGINTSIZE-1; x >= 0; --x)
	#define FORWARDS_LOOP(x) for (int x = 0; x < BIGINTSIZE; ++x)
#endif

	C_ASSERT((BIGINT_TOTAL_BITS & (BASE_BITS - 1)) == 0);

	BIGINT_BASE data[BIGINTSIZE];
public:

	// Constructors and conversion operators
	ubigint() {}
	ubigint(BIGINT_BASE q) {
#ifdef BIG_ENDIAN
		for (int i = 0; i < BIGINTSIZE-1; ++i)
			data[i] = 0U;
		data[LSBINDEX] = q;
#else
		data[LSBINDEX] = q;
		for (int i = 1; i < BIGINTSIZE; ++i)
			data[i] = 0U;
#endif
	}
	template <int OTHER_BIGINT_TOTAL_BITS>
	ubigint(const ubigint<OTHER_BIGINT_TOTAL_BITS>& q)
	{ *this = q;}
	template <int OTHER_BIGINT_TOTAL_BITS>
	ubigint(const sbigint<OTHER_BIGINT_TOTAL_BITS>& q)
	{ *this = q.asUnsigned();}

	ubigint(const std::string &s)
	{
		std::stringstream st;
		st << s.c_str();
		st >> *this;
	}

	// This can be more trouble than it's worth but...
	operator BIGINT_BASE() const
	{ return data[LSBINDEX]; }

	friend void swap(ubigint &a, ubigint &b) {
		for (int i = 0; i < BIGINTSIZE; ++i)
			std::swap(a.data[i], b.data[i]);
	}

	ubigint& operator = (unsigned int a)
	{ return *this = ubigint(a); }

	template <int OTHER_BIGINT_TOTAL_BITS>
	ubigint& operator = (const sbigint<OTHER_BIGINT_TOTAL_BITS>& q)
	{ return *this = q.asUnsigned(); }

	template <int OTHER_BIGINT_TOTAL_BITS, bool LhsGreater>
	struct assign_helper {
		template <typename T2>
		void operator()(ubigint &lhs, const T2 &rhs) const {
			const BIGINT_BASE * const accessorHack = (BIGINT_BASE*)&rhs;
			int i = 0;
#ifdef BIG_ENDIAN
			for (; i < BIGINTSIZE - OTHER_BIGINT_TOTAL_BITS / BASE_BITS; ++i)
				lhs.data[BASE_INDEX(i)] = 0U;
			for (; i < BIGINTSIZE; ++i)
				lhs.data[BASE_INDEX(i)] = accessorHack[BASE_INDEX(i)];
#else
			for (; i < OTHER_BIGINT_TOTAL_BITS / BASE_BITS; ++i)
				lhs.data[BASE_INDEX(i)] = accessorHack[BASE_INDEX(i)];
			for (; i < BIGINTSIZE; ++i)
				lhs.data[BASE_INDEX(i)] = 0U;
#endif
		}
	};

	template <int OTHER_BIGINT_TOTAL_BITS>
	struct assign_helper<OTHER_BIGINT_TOTAL_BITS, false> {
		template <typename T2>
		void operator()(ubigint &lhs, const T2 &rhs) const {
			const BIGINT_BASE *accessorHack = (BIGINT_BASE*)&rhs;
#ifdef BIG_ENDIAN
			accessorHack += (OTHER_BIGINT_TOTAL_BITS-BIGINT_TOTAL_BITS) / BASE_BITS;
#endif
			for (int i = 0; i < BIGINTSIZE; ++i)
				lhs.data[BASE_INDEX(i)] = accessorHack[BASE_INDEX(i)];
		}
	};

	template <int OTHER_BIGINT_TOTAL_BITS>
	ubigint& operator=(ubigint<OTHER_BIGINT_TOTAL_BITS> const &rhs)
	{
		assign_helper<OTHER_BIGINT_TOTAL_BITS, (BIGINT_TOTAL_BITS>OTHER_BIGINT_TOTAL_BITS)>()(*this, rhs);
		return *this;
	}

	friend void minVal(ubigint &v) {
		for (int i = 0; i < BIGINTSIZE; ++i)
			v.data[i] = 0U;
	}

	friend void maxVal(ubigint &v) {
		for (int i = 0; i < BIGINTSIZE; ++i)
			v.data[i] = BASE_MAX;
	}

	BIGINT_BASE toBase() const {
		return data[LSBINDEX];
	}

	double toDouble() const {
		const double multiplier = (double(BASE_MAX) + 1.0);
		double result = 0;
		BACKWARDS_LOOP(i)
			result = result * multiplier + data[i];
		return result;
	}

	std::string toString() const
	{
		std::stringstream st;
		st << *this;
		return st.str();
	}

	operator std::string() const {
		return toString();
	}

	const sbigint<BIGINT_TOTAL_BITS>& asSigned() const
	{ return reinterpret_cast< const sbigint<BIGINT_TOTAL_BITS>& >(*this); }
	sbigint<BIGINT_TOTAL_BITS>& asSigned()
	{ return reinterpret_cast< sbigint<BIGINT_TOTAL_BITS>& >(*this); }

	// Stream operators
	friend std::ostream& operator << (std::ostream &os, ubigint a) {
		unsigned short base = 10;
		char hexChar = 'a' - 0xA;
		if (os.flags() & std::ios::hex) {
			base = 16;
			if (os.flags() & std::ios::uppercase)
				hexChar = 'A' - 0xA;
		} else if (os.flags() & std::ios::oct)
			base = 8;

		std::string s;
		do {
			unsigned short digit;
			DivMod_short(a, base, &digit);
			s.push_back(char(digit + ((digit < 0xA) ? '0' : hexChar)));
		} while (!!a);

		int width = os.width(0) - s.length();
		if (os.flags() & std::ios::showpos)
			--width;

		if (os.flags() & std::ios::right)
			for (int i = width; i > 0; --i)
				os << os.fill();

		if (os.flags() & std::ios::showpos)
			os << '+';

		if (os.flags() & std::ios::internal)
			for (int i = width; i > 0; --i)
				os << os.fill();

		for (int i = s.length(); i > 0;)
			os << s[--i];

		if (os.flags() & std::ios::left)
			for (int i = width; i > 0; --i)
				os << os.fill();
		return os;
	}
	friend std::istream& operator >> (std::istream &is, ubigint &a) {
		unsigned int base = 10, limit = ~0U / 10;
		if (is.flags() & std::ios::hex)
			base = 16, limit = ~0U / 16;
		else if (is.flags() & std::ios::oct)
			base = 8, limit = ~0U / 8;
		a = 0;
		unsigned int aa = 0, mult = 1;
		for (;;) {
			char ch;
			is >> ch;
			if (is.eof()) {
				is.clear();
				break;
			} else {
				if (ch >= '0' && ch <= '9') {
					aa *= base;
					aa += ch - '0';
				} else if (ch >= 'A' && ch <= 'F' && base > 10) {
					aa *= base;
					aa += ch - ('A' - 0xA);
				} else if (ch >= 'a' && ch <= 'f' && base > 10) {
					aa *= base;
					aa += ch - ('a' - 0xA);
				} else
					break;
				mult *= base;
				if (mult >= limit) {
					a.mulInt(mult);
					a += aa;
					mult = 1;
					aa = 0;
				}
			}
		}
		a *= mult;
		a += aa;
		return is;
	}

	// Modifying binary logical operators
	void bitClear(int b) {
		data[b/BASE_BITS] &= ~(1<<(b%BASE_BITS));
	}

	void bitSet(int b) {
		data[b/BASE_BITS] |= 1<<(b%BASE_BITS);
	}

	void bitToggle(int b) {
		data[b/BASE_BITS] ^= 1<<(b%BASE_BITS);
	}

	bool bitTest(int b) const {
		return (data[b/BASE_BITS] & (1<<(b%BASE_BITS))) != 0;
	}

	// Special version of division that's fast but only works with small divisors
	// 'a' must be positive.
	friend void DivMod_short(ubigint &a, unsigned short b, unsigned short *remainder) {
		C_ASSERT(sizeof(b) * CHAR_BIT == BASE_BITS/2);
		if (!b)
#pragma warning (disable : 4723)
			b = 1 / b;  // Force a divide by zero exception.
#pragma warning (default : 4723)
		BIGINT_BASE temp = 0;
		bool seenNonZero = false;
		BACKWARDS_LOOP(i) {
			if (seenNonZero || a.data[i] != 0) {
				BIGINT_BASE sh1 = a.data[i] >> (BASE_BITS/2);
				temp = (temp << (BASE_BITS/2)) + sh1;
				sh1 = temp / static_cast<BIGINT_BASE>(b);
				temp %= b;

				BIGINT_BASE sh2 = a.data[i] & ((1 << (BASE_BITS/2))-1);
				temp = (temp << (BASE_BITS/2)) + sh2;
				sh2 = temp / static_cast<BIGINT_BASE>(b);
				temp %= b;

				a.data[i] = (sh1 << (BASE_BITS/2)) | sh2;
				seenNonZero = true;
			}
		}
		if (remainder != NULL)
			*remainder = static_cast<unsigned short>(temp);
	}

	friend const ubigint Divide(ubigint a, ubigint b, ubigint *remainder) {
		BIGINT_TEMPORARY ubigint c;
		int shiftcnt = 0;

		c = (ubigint)0U;
		// Check for attempt to divide by zero
		if (!b) {
			shiftcnt = 1 / shiftcnt;  // Force a divide by zero exception. (shiftcnt=0)
		} else {
			// Left shift B until it is the same magnitude as A
			shiftcnt = findHighestBitSet(a) - findHighestBitSet(b);
			if (shiftcnt > 0)
				b <<= shiftcnt;

			if (b > a) {		// If B is greater than A, right shift B
				b >>= 1;
				--shiftcnt;
			}

			while (shiftcnt >= 0) {
				if (b <= a) {	// If B is not greater than A, then the bit is a 1
					a -= b;		// Subtract B from A
					c.bitSet(shiftcnt);
				}
				b >>= 1;		// Right shift B
				--shiftcnt;
			}

			if (remainder != NULL)
				*remainder = a;
		}
		return c;
	}

	// Modifying binary logical operators
	ubigint& operator &=(const ubigint& q) {
		for (int i = 0; i < BIGINTSIZE; ++i)
			data[i] &= q.data[i];
		return *this;
	}

	ubigint& operator |=(const ubigint& q) {
		for (int i = 0; i < BIGINTSIZE; ++i)
			data[i] |= q.data[i];
		return *this;
	}

	ubigint& operator ^=(const ubigint& q) {
		for (int i = 0; i < BIGINTSIZE; ++i)
			data[i] ^= q.data[i];
		return *this;
	}

	// Modifying binary mathematical operators
	ubigint& operator>>=(int shift) {
		int source = shift / BASE_BITS;
		int remaindershift = shift & (BASE_BITS-1);
		int othershift = BASE_BITS - remaindershift;

		FORWARDS_LOOP(i) {
			if (source < BIGINTSIZE) {
				data[i] = data[BASE_INDEX(source)] >> remaindershift;
				if (++source < BIGINTSIZE && othershift < BASE_BITS)
					data[i] |= data[BASE_INDEX(source)] << othershift;
			} else {
				data[i] = 0U;
			}
		}
		return *this;
	}

	ubigint& operator<<=(int shift) {
		int source = BIGINTSIZE-1 - shift / BASE_BITS;
		int remaindershift = shift & (BASE_BITS-1);
		int othershift = BASE_BITS - remaindershift;

		BACKWARDS_LOOP(i) {
			if (source >= 0) {
				data[i] = data[BASE_INDEX(source)] << remaindershift;
				if (--source >= 0 && othershift < BASE_BITS)
					data[i] |= data[BASE_INDEX(source)] >> othershift;
			} else {
				data[i] = 0U;
			}
		}
		return *this;
	}

	ubigint& operator +=(const ubigint& q) {
		BIGINT_BASE carry = 0U;

		FORWARDS_LOOP(i) {
			data[i] += q.data[i] + carry;
			if (!carry) {
				carry = (data[i] <  q.data[i]);
			} else {
				carry = (data[i] <= q.data[i]);
			}
		}
		return *this;
	}

	ubigint& operator -=(const ubigint& q) {
		BIGINT_BASE borrow = 0U, prevdigit;

		FORWARDS_LOOP(i) {
			prevdigit = data[i];
			data[i] -= q.data[i] + borrow;
			if (!borrow) {
				borrow = (prevdigit <  q.data[i]);
			} else {
				borrow = (prevdigit <= q.data[i]);
			}
		}
		return *this;
	}

#ifndef SIMPLE_MULTIPLICATION
	/* This method of multiplication is more complicated, but faster.
	 DDProduct take a two numbers 'ab' and 'cd' and splits each in half,
	 into 'a', 'b', 'c', and 'd'. It can then perform multiplications
	 natively on the processor without causing overflow. We add the pieces
	 together afterwards, taking care of the overflow manually, and the
	 result is stored into hi and lo. The result is (at worst) as big as
	 the size of the inputs combined, in multuiplication.
		  a b
		* c d
	 ========
		 bdbd (I.e. b*d high part plus b*d low part)
	   adad
	   bcbc
	 acac */
	static void DDProduct(BIGINT_BASE ab, BIGINT_BASE cd, BIGINT_BASE &hi, BIGINT_BASE &lo)
	{
		BIGINT_BASE a = ab >> HALF_BASE_BITS, b = ab & LOW_MASK,
			c = cd >> HALF_BASE_BITS, d = cd & LOW_MASK;
		BIGINT_BASE ad = a*d, bc = b*c, temp;
		// the 'hi' calculation can't overflow because the worse case is
		// 0xFFFFFFFF * 0xFFFFFFFF which equals 0xFFFFFFFE00000001
		hi = a*c + (ad >> HALF_BASE_BITS) + (bc >> HALF_BASE_BITS);
		// The 'lo' part is made up of 'bd' high and low parts plus 'ad' low
		// part, and 'bc' low parts. Those two adds could overflow into 'hi'.
		lo = b*d;
		temp = lo;
		lo += (ad << HALF_BASE_BITS);
		if (lo < temp)	// Deal with overflow into 'hi'
			++hi;
		temp = lo;
		lo += (bc << HALF_BASE_BITS);
		if (lo < temp)	// Deal with overflow into 'hi'
			++hi;
	}
	ubigint& operator *=(ubigint q) {
		BIGINT_TEMPORARY ubigint t;
		t = *this;
		*this = (ubigint)0U;
		int iMax = BIGINTSIZE, jMax = BIGINTSIZE;
		while (t.data[iMax-1] == 0) --iMax;
		while (q.data[jMax-1] == 0) --jMax;
		for (int i=0; i<iMax; ++i) {
			for (int j=0; j<jMax; ++j) {
				BIGINT_BASE hi, lo;
				DDProduct(t.data[i], q.data[j], hi, lo);
				int ij = i+j;
				BIGINT_BASE temp = data[ij];
				data[ij] += lo;
				if (data[ij] < temp) {
					while (!++data[++ij]) {}
				}
				ij = i+j+1;
				temp = data[ij];
				data[ij] += hi;
				if (data[ij] < temp) {
					while (!++data[++ij]) {}
				}
			}
		}
		return *this;
	}
	ubigint& mulInt(unsigned int rhs) {
		BIGINT_TEMPORARY ubigint t;
		t = *this;
		*this = (ubigint)0U;
		int iMax = BIGINTSIZE;
		while (t.data[iMax-1] == 0) --iMax;
		for (int i=0; i<iMax; ++i) {
			BIGINT_BASE hi, lo;
			DDProduct(t.data[i], rhs, hi, lo);
			int ii = i;
			BIGINT_BASE temp = data[ii];
			data[ii] += lo;
			if (data[ii] < temp) {
				while (!++data[++ii]) {}
			}
			ii = i+1;
			temp = data[ii];
			data[ii] += hi;
			if (data[ii] < temp) {
				while (!++data[++ii]) {}
			}
		}
		return *this;
	}
#else
	/* This method of multiplication is exactly how you do long
	 multiplication by hand except that it's base 2 instead of
	 base 10. */
	ubigint& operator *=(ubigint q) {
		BIGINT_TEMPORARY ubigint t;
		t = *this;
		*this = (ubigint)0U;
		do {
			if ((q.data[LSBINDEX] & 1U) != 0U)
				*this += t;
			q >>= 1;
			t <<= 1;
		} while (!!q);
		return *this;
	}

	ubigint& mulInt(unsigned int q) {
		BIGINT_TEMPORARY ubigint t;
		t = *this;
		*this = (ubigint)0U;
		int shift = 0;
		while (q) {
			while ((q & 1U) == 0) {
				q >>= 1;
				++shift;
			}
			t <<= shift;
			q >>= 1;
			shift = 1;
			*this += t;
		}
		return *this;
	}
#endif

	ubigint& operator /=(const ubigint& q) {
		return *this = Divide(*this, q, NULL);
	}

	ubigint& operator %=(const ubigint &q) {
		Divide(*this, q, this);
		return *this;
	}

	// Binary comparison operators
	friend bool operator ==(const ubigint& a, const ubigint& b) {
		for (int i = 0; i < BIGINTSIZE; ++i)
			if (a.data[i] != b.data[i])
				return false;
		return true;
	}

	friend inline bool operator !=(const ubigint& a, const ubigint& b) {
		return !(a == b);
	}

	friend bool operator < (const ubigint& a, const ubigint& b) {
		BACKWARDS_LOOP(i) {
			if (a.data[i] < b.data[i]) return true;
			if (a.data[i] > b.data[i]) return false;
		}
		return false;
	}

	friend bool operator > (const ubigint& a, const ubigint& b)
	{ return (b < a); }

	friend bool operator <= (const ubigint& a, const ubigint& b)
	{ return !(b < a); }

	friend bool operator >= (const ubigint& a, const ubigint& b)
	{ return !(a < b); }

	// Binary logical operators
	const ubigint operator>> (int shift) const {
		BIGINT_TEMPORARY ubigint result;
		result = *this;
		result >>= shift;
		return result;
	}

	const ubigint operator<< (int shift) const {
		BIGINT_TEMPORARY ubigint result;
		result = *this;
		result <<= shift;
		return result;
	}

	friend const ubigint operator & (const ubigint& a, const ubigint& b) {
		BIGINT_TEMPORARY ubigint result;
		for (int i = 0; i < BIGINTSIZE; ++i)
			result.data[i] = a.data[i] & b.data[i];
		return result;
	}

	friend const ubigint operator | (const ubigint& a, const ubigint& b) {
		BIGINT_TEMPORARY ubigint result;
		for (int i = 0; i < BIGINTSIZE; ++i)
			result.data[i] = a.data[i] | b.data[i];
		return result;
	}

	friend const ubigint operator ^ (const ubigint& a, const ubigint& b) {
		BIGINT_TEMPORARY ubigint result;
		for (int i = 0; i < BIGINTSIZE; ++i)
			result.data[i] = a.data[i] ^ b.data[i];
		return result;
	}

	// Binary mathematical operators
	friend const ubigint operator + (const ubigint& a, const ubigint& b) {
		BIGINT_TEMPORARY ubigint result;
		result = a;
		result += b;
		return result;
	}

	friend const ubigint operator - (const ubigint& a, const ubigint& b) {
		BIGINT_TEMPORARY ubigint result;
		result = a;
		result -= b;
		return result;
	}

	friend const ubigint operator * (const ubigint& a, const ubigint& b) {
		BIGINT_TEMPORARY ubigint result;
		result = a;
		result *= b;
		return result;
	}
	friend const ubigint operator / (const ubigint& a, const ubigint& b) {
		return Divide(a, b, NULL);
	}

	friend const ubigint operator % (const ubigint& a, const ubigint& b) {
		BIGINT_TEMPORARY ubigint result;
		Divide(a, b, &result);
		return result;
	}

	// Modifying unary operators
	ubigint& operator++ () {  // Pre Increment operator -- faster than add
		++data[LSBINDEX];
#ifdef BIG_ENDIAN
		for (int i = BIGINTSIZE-1; i > 0; --i) {
			if (!data[i])
				++data[i-1];
			else
				break;
		}
#else
		for (int i = 0; i < BIGINTSIZE-1; ++i) {
			if (!data[i])
				++data[i+1];
			else
				break;
		}
#endif
		return *this;
	}

	const ubigint operator++ (int) {  // Post Increment operator -- faster than add
		BIGINT_TEMPORARY ubigint result;
		result = *this;
		++*this;
		return result;
	}

	ubigint& operator-- () {  // Pre Decrement operator -- faster than subtract
		--data[LSBINDEX];
#ifdef BIG_ENDIAN
		for (int i = BIGINTSIZE-1; i > 0; --i) {
			if (data[i] == BASE_MAX)
				--data[i-1];
			else
				break;
		}
#else
		for (int i = 0; i < BIGINTSIZE-1; ++i) {
			if (data[i] == BASE_MAX)
				--data[i+1];
			else
				break;
		}
#endif
		return *this;
	}

	const ubigint operator-- (int) {  // Post Decrement operator -- faster than subtract
		BIGINT_TEMPORARY ubigint result;
		result = *this;
		--*this;
		return result;
	}

	// Unary operators
	bool operator ! () const {	//For comparison against zero
		bool Result = true;
		for (int i = 0; i < BIGINTSIZE; ++i)
			Result &= !data[i];
		return Result;
	}

	const ubigint operator ~ () const {
		BIGINT_TEMPORARY ubigint result;
		for (int i = 0; i < BIGINTSIZE; ++i)
			result.data[i] = ~data[i];
		return result;
	}

	const ubigint& operator + () const {  // Unary positive
		return *this;
	}

	const ubigint operator - () const {  // Negates a number
		BIGINT_TEMPORARY ubigint result;
		for (int i = 0; i < BIGINTSIZE; ++i)
			result.data[i] = ~data[i];
		++result;
		return result;
	}

	//Misc
	friend const ubigint sqrt(const ubigint& q) {		// returns the square root of q
		BIGINT_TEMPORARY ubigint x, dx;
		static const ubigint mask = ~ubigint(1);

		if (!q) {
			return q;
		} else {
			x = q >> (findHighestBitSet(q)>>1);

			do {
				/* We are really performing the fuction:
				dx = (y/x - x) / 2;
				below, but since these are unsigned numbers,
				we MUST do the subtraction last in order for
				the x += dx equation to work properly. */

				dx = (q>>1)/x - (x>>1);
				x += dx;
			} while (!!(dx & mask));

			// truncate answer
			if (x*x > q)
				--x;
			return x;
		}
	}

	friend const ubigint factorial(const ubigint &q) {
		BIGINT_TEMPORARY ubigint result;
		BIGINT_BASE f = q;
		//If the number to take the factorial of is bigger than can fit into
		//an unsigned long then the there's no way in hell the result can be
		//stored in conventional PC memory anyway - TOO BIG!
		result = 1;
		while (f > 0U) {
			result.mulInt(f--);
		}
		return result;
	}

	// This is extremely slow - Best not to use.
	friend bool isPrime(const ubigint& q) {
		BIGINT_TEMPORARY ubigint stop;
		BIGINT_TEMPORARY ubigint factor;

		if (q <= (ubigint)1U) return false;
		if (q == (ubigint)2U) return true;
		if (!(q.data[LSBINDEX] & 1U)) return false;
		stop = sqrt(q);
		for (factor = 3U; factor <= stop; factor+=2U) {
			if (!(q % factor)) {
				return false;
			}
		}
		return true;
	}

	friend const ubigint gcd(ubigint a, ubigint b) {
		BIGINT_TEMPORARY ubigint c;
		if (!a)
			return b;
		if (!b)
			return a;
		int shift = 0;
		while (!((a.data[LSBINDEX] | b.data[LSBINDEX]) & 1U)) {
			a >>= 1;
			b >>= 1;
			++shift;
		}
		while (a > (ubigint)0U) {
			if (!(a.data[LSBINDEX] & 1U))
				a >>= 1;
			else if (!(b.data[LSBINDEX] & 1U))
				b >>= 1;
			else {
				c = (abs(a.asSigned() - b.asSigned()) >> 1).asUnsigned();
				if (a < b)
					b = c;
				else
					a = c;
			}
		}
		return b << shift;
	}

	friend const ubigint lcm(ubigint a, ubigint b) {
		return (a / gcd(a, b)) * b;
	}

	friend const ubigint bitRotateRight(const ubigint &x, int shift) {
		BIGINT_TEMPORARY ubigint y;
		int source = (shift / BASE_BITS) % BIGINTSIZE;
		int remaindershift = shift & (BASE_BITS-1);

		if (remaindershift != 0) {
			int othershift = BASE_BITS - remaindershift;
			FORWARDS_LOOP(i) {
				int source1 = source;
				if (++source == BIGINTSIZE)
					source = 0;
				y.data[i] = (x.data[BASE_INDEX(source1)] >> remaindershift) |
							(x.data[BASE_INDEX(source)] << othershift);
			}
		} else {
			FORWARDS_LOOP(i) {
				y.data[i] = x.data[BASE_INDEX(source)];
				if (++source == BIGINTSIZE)
					source = 0;
			}
		}
		return y;
	}

	friend int findHighestBitSet(const ubigint &x) {
		int result = BIGINT_TOTAL_BITS-1;
		BACKWARDS_LOOP(i) {
			if (x.data[i] != 0) {
				BIGINT_BASE temp = x.data[i];
				BIGINT_BASE tempMax = BASE_MAX;
				int shift = BASE_BITS>>1;
				do {
					tempMax <<= shift;
					if ((temp & tempMax) == 0) {
						result -= shift;
						temp = temp << shift;
					}
				} while ((shift>>=1) > 0);
				break;
			}
			result -= BASE_BITS;
		}
		return result;
	}

	friend int findLowestBitSet(const ubigint &x) {
		int result = 0;
		FORWARDS_LOOP(i) {
			if (x.data[i] != 0) {
				BIGINT_BASE temp = x.data[i];
				BIGINT_BASE tempMax = BASE_MAX;
				int shift = BASE_BITS>>1;
				do {
					tempMax >>= shift;
					if ((temp & tempMax) == 0) {
						result += shift;
						temp = temp >> shift;
					}
				} while ((shift>>=1) > 0);
				break;
			}
			result += BASE_BITS;
		}
		return result;
	}

	friend bool isPow2(const ubigint& q) {
		bool found = false;
		for (int i = 0; i < BIGINTSIZE; ++i) {
			if (q.data[i] != 0) {
				if (found)
					return false;
				if ((q.data[i] & (q.data[i]-1)) != 0)
					return false;
				found = true;
			}
		}
		return true;
	}

	friend const ubigint nextPow2(const ubigint& q) {
		BIGINT_TEMPORARY ubigint result;
		result = q - (ubigint)1U;
		int shift = 1;
		do {
			result |= result >> shift;
			shift <<= 1;
		} while (shift < BIGINT_TOTAL_BITS);
		++result;
		return result;
	}

	friend BIGINT_BASE ceillog2(const ubigint& q) {
		BIGINT_TEMPORARY ubigint temp, temp2;
		BIGINT_BASE result = 0U;
		int shift = BIGINT_TOTAL_BITS>>1;

		temp = q;
		do {
			temp2 = temp >> shift;
			if (!!temp2) {
				temp = temp2;
				result |= shift;
			}
		} while ((shift>>=1) > 0);
		return result;
	}

	friend const ubigint pow(ubigint a, int b) {
		BIGINT_TEMPORARY ubigint result;
		if (b < 0)
			return (ubigint)0;
		if (a == (ubigint)1U)
			return a;
		result = (ubigint)1U;
		while (b) {
			if (b & 1)
				result *= a;
			b >>= 1;
			a *= a;
		}
		return result;
	}

	friend const ubigint modpow(ubigint base, ubigint exp, const ubigint &mod)
	{
		BIGINT_TEMPORARY ubigint result;
		result = 1;
		while (exp > 0) {
			if (!!(exp & 1))
				result = (result * base) % mod;
			exp >>= 1;
			base = (base * base) % mod;
		}
		return result;
	}

	friend bool operator < (const ubigint& q, int a)
	{ return q < sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend bool operator > (const ubigint& q, int a)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() < q; }
	friend bool operator <=(const ubigint& q, int a)
	{ return !(sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() < q); }
	friend bool operator >=(const ubigint& q, int a)
	{ return !(q < sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned()); }
	friend bool operator ==(const ubigint& q, int a)
	{ return q == sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend bool operator !=(const ubigint& q, int a)
	{ return q != sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend bool operator < (int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() < q; }
	friend bool operator > (int a, const ubigint& q)
	{ return q < sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend bool operator <=(int a, const ubigint& q)
	{ return !(q < sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned()); }
	friend bool operator >=(int a, const ubigint& q)
	{ return !(sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() < q); }
	friend bool operator ==(int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() == q; }
	friend bool operator !=(int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() != q; }

	friend const ubigint operator & (const ubigint& q, int a)
	{ return q & ubigint(a); }
	friend const ubigint operator | (const ubigint& q, int a)
	{ return q | ubigint(a); }
	friend const ubigint operator ^ (const ubigint& q, int a)
	{ return q ^ ubigint(a); }
	friend const ubigint operator & (int a, const ubigint& q)
	{ return ubigint(a) & q; }
	friend const ubigint operator | (int a, const ubigint& q)
	{ return ubigint(a) | q; }
	friend const ubigint operator ^ (int a, const ubigint& q)
	{ return ubigint(a) ^ q; }

	friend const ubigint operator + (const ubigint& q, int a)
	{ return q + sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend const ubigint operator - (const ubigint& q, int a)
	{ return q - sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend const ubigint operator * (const ubigint& q, int a)
	{ return q * sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend const ubigint operator / (const ubigint& q, int a)
	{ return q / sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend const ubigint operator % (const ubigint& q, int a)
	{ return q % sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned(); }
	friend const ubigint operator + (int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() + q; }
	friend const ubigint operator - (int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() - q; }
	friend const ubigint operator * (int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() * q; }
	friend const ubigint operator / (int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() / q; }
	friend const ubigint operator % (int a, const ubigint& q)
	{ return sbigint<BIGINT_TOTAL_BITS>(a).asUnsigned() % q; }
};

// Now we overload the unsigned functions to provide
// the necessary differences for signed numbers.

template <int BIGINT_TOTAL_BITS>
class sbigint : public ubigint<BIGINT_TOTAL_BITS>
{
	typedef typename ubigint<BIGINT_TOTAL_BITS>::BIGINT_BASE BIGINT_BASE;
	enum {
		BASE_BITS = ubigint<BIGINT_TOTAL_BITS>::BASE_BITS,
		HIGH_BASE_BIT = ubigint<BIGINT_TOTAL_BITS>::HIGH_BASE_BIT,
		BIGINTSIZE = ubigint<BIGINT_TOTAL_BITS>::BIGINTSIZE,
		LSBINDEX = ubigint<BIGINT_TOTAL_BITS>::LSBINDEX,
		MSBINDEX = ubigint<BIGINT_TOTAL_BITS>::MSBINDEX,
	};

public:

	// Constructors and conversion operators
	sbigint() {}
	sbigint(long q) {
		this->data[LSBINDEX] = q;
		if (q < 0)	//Sign extend
#ifdef BIG_ENDIAN
			for (int i = 0; i < LSBINDEX; ++i)
#else
			for (int i = 1; i < BIGINTSIZE; ++i)
#endif
				this->data[i] = BASE_MAX;
		else
#ifdef BIG_ENDIAN
			for (int i = 0; i < LSBINDEX; ++i)
#else
			for (int i = 1; i < BIGINTSIZE; ++i)
#endif
				this->data[i] = 0U;
	}
	template <int OTHER_BIGINT_TOTAL_BITS>
	sbigint(const sbigint<OTHER_BIGINT_TOTAL_BITS>& q)
	{ *this = q;}
	template <int OTHER_BIGINT_TOTAL_BITS>
	sbigint(const ubigint<OTHER_BIGINT_TOTAL_BITS>& q)
	{ *this = q.asSigned();}

	sbigint(const std::string &s)
	{
		std::stringstream st;
		st << s.c_str();
		st >> *this;
	}


	sbigint& operator = (int a)
	{ return *this = sbigint(a); }

	template <int OTHER_BIGINT_TOTAL_BITS>
	sbigint& operator = (const ubigint<OTHER_BIGINT_TOTAL_BITS>& q)
	{ return *this = q.asSigned(); }

	template <int OTHER_BIGINT_TOTAL_BITS, bool LhsGreater>
	struct assign_helper {
		template <typename T2>
		void operator()(sbigint &lhs, const T2 &rhs) const {
			const BIGINT_BASE * const accessorHack = (BIGINT_BASE*)&rhs;
			int i = 0;
#ifdef BIG_ENDIAN
			if (rhs < (sbigint<OTHER_BIGINT_TOTAL_BITS>)0U) {	//Sign extend
				for (; i < BIGINTSIZE - OTHER_BIGINT_TOTAL_BITS / BASE_BITS; ++i)
					lhs.data[BASE_INDEX(i)] = BASE_MAX;
			} else {
				for (; i < BIGINTSIZE - OTHER_BIGINT_TOTAL_BITS / BASE_BITS; ++i)
					lhs.data[BASE_INDEX(i)] = 0U;
			}
			for (; i < BIGINTSIZE; ++i)
				lhs.data[BASE_INDEX(i)] = accessorHack[BASE_INDEX(i)];
#else
			for (; i < OTHER_BIGINT_TOTAL_BITS / BASE_BITS; ++i)
				lhs.data[BASE_INDEX(i)] = accessorHack[BASE_INDEX(i)];
			if (rhs < (sbigint<OTHER_BIGINT_TOTAL_BITS>)0U) {	//Sign extend
				for (; i < BIGINTSIZE; ++i)
					lhs.data[BASE_INDEX(i)] = BASE_MAX;
			} else {
				for (; i < BIGINTSIZE; ++i)
					lhs.data[BASE_INDEX(i)] = 0U;
			}
#endif
		}
	};

	template <int OTHER_BIGINT_TOTAL_BITS>
	struct assign_helper<OTHER_BIGINT_TOTAL_BITS, false> {
		template <typename T2>
		void operator()(sbigint &lhs, const T2 &rhs) const {
			const BIGINT_BASE *accessorHack = (BIGINT_BASE*)&rhs;
#ifdef BIG_ENDIAN
			accessorHack += (OTHER_BIGINT_TOTAL_BITS-BIGINT_TOTAL_BITS) / BASE_BITS;
#endif
			for (int i = 0; i < BIGINTSIZE; ++i)
				lhs.data[BASE_INDEX(i)] = accessorHack[BASE_INDEX(i)];
		}
	};

	template <int OTHER_BIGINT_TOTAL_BITS>
	sbigint& operator=(sbigint<OTHER_BIGINT_TOTAL_BITS> const &rhs)
	{
		assign_helper<OTHER_BIGINT_TOTAL_BITS, (BIGINT_TOTAL_BITS>OTHER_BIGINT_TOTAL_BITS)>()(*this, rhs);
		return *this;
	}

	friend void minVal(sbigint &v) {
		v = ubigint<BIGINT_TOTAL_BITS>(1) << (BIGINT_TOTAL_BITS-1);
	}

	friend void maxVal(sbigint &v) {
		ubigint<BIGINT_TOTAL_BITS>::minVal(v);
		--v;
	}

	double toDouble() const {
		if ((this->data[MSBINDEX] & HIGH_BASE_BIT) != 0U) {
			return -((-*this).asUnsigned().toDouble());
		} else {
			return asUnsigned().toDouble();
		}
	}

	std::string toString() const
	{
		std::stringstream st;
		st << *this;
		std::string s = st.str();
		s.resize(s.length()-1);	// remove trailing space
		return s;
	}

	operator std::string() const {
		return toString();
	}

	const ubigint<BIGINT_TOTAL_BITS>& asUnsigned() const
	{ return reinterpret_cast< const ubigint<BIGINT_TOTAL_BITS>& >(*this); }
	ubigint<BIGINT_TOTAL_BITS>& asUnsigned()
	{ return reinterpret_cast< ubigint<BIGINT_TOTAL_BITS>& >(*this); }

	// Stream operators
	friend std::ostream& operator << (std::ostream &os, const sbigint &a) {
		ubigint<BASE_BITS> b;
		bool neg = ((a.data[MSBINDEX] & HIGH_BASE_BIT) != 0U);
		if (neg)
			b = (-a).asUnsigned();
		else
			b = a.asUnsigned();

		unsigned short base = 10;
		char hexChar = 'a' - 0xA;
		if (os.flags() & std::ios::hex) {
			base = 16;
			if (os.flags() & std::ios::uppercase)
				hexChar = 'A' - 0xA;
		} else if (os.flags() & std::ios::oct)
			base = 8;

		std::string s;
		do {
			unsigned short digit;
			DivMod_short(b, base, &digit);
			s.push_back(char(digit + ((digit < 0xA) ? '0' : hexChar)));
		} while (!!b);

		int width = os.width(0) - s.length();
		if (neg || (os.flags() & std::ios::showpos))
			--width;

		if (os.flags() & std::ios::right)
			for (int i = width; i > 0; --i)
				os << os.fill();

		if (neg)
			os << '-';
		else if (os.flags() & std::ios::showpos)
			os << '+';

		if (os.flags() & std::ios::internal)
			for (int i = width; i > 0; --i)
				os << os.fill();

		for (int i = s.length(); i > 0;)
			os << s[--i];

		if (os.flags() & std::ios::left)
			for (int i = width; i > 0; --i)
				os << os.fill();
		return os;
	}
	friend std::istream& operator >> (std::istream &is, sbigint &a) {
		char ch;
		if (is.peek() == '-') {
			is >> ch >> a.asUnsigned();
			a = -a;
			return is;
		} else if (is.peek() == '+') {
			return is >> ch >> a.asUnsigned();
		} else {
			return is >> a.asUnsigned();
		}
	}

	friend const sbigint Divide(sbigint a, sbigint b, sbigint *remainder) {
		if ((a.data[MSBINDEX] & HIGH_BASE_BIT) != 0U) {
			BIGINT_TEMPORARY sbigint result;
			if ((b.data[MSBINDEX] & HIGH_BASE_BIT) != 0U) {
				result = Divide((-a).asUnsigned(), (-b).asUnsigned(), (ubigint<BIGINT_TOTAL_BITS>*)remainder).asSigned();
			} else {
				result = -Divide((-a).asUnsigned(), b.asUnsigned(), (ubigint<BIGINT_TOTAL_BITS>*)remainder).asSigned();
			}
			if (remainder != NULL) *remainder = -*remainder;
			return result;
		} else {
			if ((b.data[MSBINDEX] & HIGH_BASE_BIT) != 0U) {
				return -Divide(a.asUnsigned(), (-b).asUnsigned(), (ubigint<BIGINT_TOTAL_BITS>*)remainder).asSigned();
			} else {
				return Divide(a.asUnsigned(), b.asUnsigned(), (ubigint<BIGINT_TOTAL_BITS>*)remainder).asSigned();
			}
		}
	}

	// Modifying binary logical operators
	sbigint& operator &=(const sbigint& q)
	{ return ( asUnsigned() &= q.asUnsigned() ).asSigned(); }

	sbigint& operator |=(const sbigint& q)
	{ return ( asUnsigned() |= q.asUnsigned() ).asSigned(); }

	sbigint& operator ^=(const sbigint& q)
	{ return ( asUnsigned() ^= q.asUnsigned() ).asSigned(); }

	// Modifying binary mathematical operators
	sbigint& operator>>=(int shift) {
		if (!(this->data[MSBINDEX] & HIGH_BASE_BIT))
			return ( asUnsigned() >>= shift ).asSigned();

		int source = shift / BASE_BITS;
		int remaindershift = shift & (BASE_BITS-1);
		int othershift = BASE_BITS - remaindershift;
		FORWARDS_LOOP(i) {
			if (source < BIGINTSIZE) {
				this->data[i] = this->data[BASE_INDEX(source++)] >> remaindershift;
				if (othershift < BASE_BITS)
					this->data[i] |= ((source < BIGINTSIZE) ? this->data[BASE_INDEX(source)] : BASE_MAX) << othershift;
			} else {
				this->data[i] = BASE_MAX;
			}
		}
		return *this;
	}

	sbigint& operator<<=(int shift)
	{ return ( asUnsigned() <<= shift ).asSigned(); }

	sbigint& operator *=(const sbigint& q) {
		if ((this->data[MSBINDEX] & HIGH_BASE_BIT) != 0U) {
			*this = -*this;
			if ((q.data[MSBINDEX] & HIGH_BASE_BIT) != 0U) {
				return (asUnsigned() *= (-q).asUnsigned()).asSigned();
			} else {
				asUnsigned() *= q.asUnsigned();
				return *this = -*this;
			}
		} else {
			if ((q.data[MSBINDEX] & HIGH_BASE_BIT) != 0U) {
				asUnsigned() *= (-q).asUnsigned();
				return *this = -*this;
			} else {
				return (asUnsigned() *= q.asUnsigned()).asSigned();
			}
		}
	}

	sbigint& operator /=(const sbigint& q) {
		return *this = Divide(*this, q, NULL);
	}

	sbigint& operator %=(const sbigint& q) {
		Divide(*this, q, this);
		return *this;
	}


	// Binary comparison operators
	friend bool operator ==(const sbigint& a, const sbigint& b)
	{ return a.asUnsigned() == b.asUnsigned(); }

	friend bool operator !=(const sbigint& a, const sbigint& b)
	{ return a.asUnsigned() != b.asUnsigned(); }

#if defined(_MSC_VER) && (_MSC_VER < 1400)
	bool operator < (const sbigint& b) const {
		BIGINT_TEMPORARY sbigint lhs, rhs;
		lhs = *this;
		rhs = b;
		lhs.data[MSBINDEX] ^= HIGH_BASE_BIT;
		rhs.data[MSBINDEX] ^= HIGH_BASE_BIT;
		return lhs.asUnsigned() < rhs.asUnsigned();
	}

	bool operator > (const sbigint& b) const
	{ return (b < *this); }

	bool operator <= (const sbigint& b) const
	{ return !(b < *this); }

	bool operator >= (const sbigint& b) const
	{ return !(*this < b); }
#else
	// Can't use this in MSVC6 because of some odd bug where it calls the base class instead,
	// despite both sides explicitly being sbigints, in some cases!
	friend bool operator < (const sbigint& a, const sbigint& b) {
		BIGINT_TEMPORARY sbigint lhs, rhs;
		lhs = a;
		rhs = b;
		lhs.data[MSBINDEX] ^= HIGH_BASE_BIT;
		rhs.data[MSBINDEX] ^= HIGH_BASE_BIT;
		return lhs.asUnsigned() < rhs.asUnsigned();
	}

	friend bool operator > (const sbigint& a, const sbigint& b)
	{ return (b < a); }

	friend bool operator <= (const sbigint& a, const sbigint& b)
	{ return !(b < a); }

	friend bool operator >= (const sbigint& a, const sbigint& b)
	{ return !(a < b); }
#endif

	// Binary logical operators
	const sbigint operator>> (int shift) const {
		BIGINT_TEMPORARY sbigint result;
		result = *this;
		return (result >>= shift);
	}

	const sbigint operator<< (int shift) const
	{ return ( asUnsigned() << shift ).asSigned(); }

	friend const sbigint operator & (const sbigint& a, const sbigint& b)
	{ return ( a.asUnsigned() & b.asUnsigned() ).asSigned(); }

	friend const sbigint operator | (const sbigint& a, const sbigint& b)
	{ return ( a.asUnsigned() | b.asUnsigned() ).asSigned(); }

	friend const sbigint operator ^ (const sbigint& a, const sbigint& b)
	{ return ( a.asUnsigned() ^ b.asUnsigned() ).asSigned(); }

	// Binary mathematical operators
	friend const sbigint operator + (const sbigint& a, const sbigint& b)
	{ return ( a.asUnsigned() + b.asUnsigned() ).asSigned(); }

	friend const sbigint operator - (const sbigint& a, const sbigint& b)
	{ return ( a.asUnsigned() - b.asUnsigned() ).asSigned(); }

	friend const sbigint operator * (const sbigint& a, const sbigint& b) {
		BIGINT_TEMPORARY sbigint result;
		result = a;
		return (result *= b);
	}
	friend const sbigint operator / (const sbigint& a, const sbigint& b)
	{ return Divide(a, b, NULL); }

	friend const sbigint operator % (const sbigint& a, const sbigint& b) {
		BIGINT_TEMPORARY sbigint result;
		Divide(a, b, &result);
		return result;
	}

	// Modifying unary operators
	sbigint& operator++ ()
	{ return (++asUnsigned()).asSigned(); }
	const sbigint operator++ (int)
	{ return (asUnsigned()++).asSigned(); }

	sbigint& operator-- ()
	{ return (--asUnsigned()).asSigned(); }
	const sbigint operator-- (int)
	{ return (asUnsigned()--).asSigned(); }

	const sbigint operator ~ () const
	{ return ( ~asUnsigned() ).asSigned(); }

	sbigint& operator + () const  // Unary positive
	{ return (sbigint&)*this; }

	const sbigint operator - () const  // Negates a number
	{ return ( -asUnsigned() ).asSigned(); }

	//Misc
	friend const sbigint sqrt(const sbigint& q) {		// returns the square root of q
		if ((q.data[MSBINDEX] & HIGH_BASE_BIT) != 0U)
			return sbigint(0U);	// if negative just return zero
		return sqrt(q.asUnsigned()).asSigned();
	}

	friend const sbigint cubert(const sbigint& q) {		// returns the cube root of q
		BIGINT_TEMPORARY sbigint x, dx;

		if (!q) {
			return q;
		} else {
			x = q >> ((2*findHighestBitSet(q))/3);

			do {
				dx = (q/(x*x) - x)/3;
				x += dx;
			} while (!!dx);

			// truncate answer
			if (q < 0) {
				if (x*x*x < q)
					++x;
			} else {
				if (x*x*x > q)
					--x;
			}
			return x;
		}
	}

	friend const sbigint abs(const sbigint& q) {
		return ((q.data[MSBINDEX] & HIGH_BASE_BIT) != 0U) ? -q : q;
	}
	friend const sbigint factorial(const sbigint& q) {
		if ((q.data[MSBINDEX] & HIGH_BASE_BIT) != 0U)
			return sbigint(0U);
		return factorial(q.asUnsigned()).asSigned();
	}

	friend bool isPrime(const sbigint& q) {
		if ((q.data[MSBINDEX] & HIGH_BASE_BIT) != 0U)
			return false;
		return q.asUnsigned().isPrime();
	}

	friend const sbigint gcd(const sbigint &a, const sbigint &b) {
		return gcd(abs(a).asUnsigned(), abs(b).asUnsigned()).asSigned();
	}

	friend const sbigint pow(const sbigint &a, int b) {
		BIGINT_TEMPORARY sbigint temp;
		temp = pow(abs(a).asUnsigned(), b).asSigned();
		return (((a.data[MSBINDEX] & HIGH_BASE_BIT) != 0U) && ((b & 1) != 0)) ? -temp : temp;
	}

	friend bool operator < (const sbigint& q, int a) { return q < sbigint(a); }
	friend bool operator > (const sbigint& q, int a) { return sbigint(a) < q; }
	friend bool operator <=(const sbigint& q, int a) { return !(sbigint(a) < q); }
	friend bool operator >=(const sbigint& q, int a) { return !(q < sbigint(a)); }
	friend bool operator ==(const sbigint& q, int a) { return q == sbigint(a); }
	friend bool operator !=(const sbigint& q, int a) { return q != sbigint(a); }
	friend bool operator < (int a, const sbigint& q) { return sbigint(a) < q; }
	friend bool operator > (int a, const sbigint& q) { return q < sbigint(a); }
	friend bool operator <=(int a, const sbigint& q) { return !(q < sbigint(a)); }
	friend bool operator >=(int a, const sbigint& q) { return !(sbigint(a) < q); }
	friend bool operator ==(int a, const sbigint& q) { return sbigint(a) == q; }
	friend bool operator !=(int a, const sbigint& q) { return sbigint(a) != q; }

	friend const sbigint operator & (const sbigint& q, int a) { return q & sbigint(a); }
	friend const sbigint operator | (const sbigint& q, int a) { return q | sbigint(a); }
	friend const sbigint operator ^ (const sbigint& q, int a) { return q ^ sbigint(a); }
	friend const sbigint operator & (int a, const sbigint& q) { return sbigint(a) & q; }
	friend const sbigint operator | (int a, const sbigint& q) { return sbigint(a) | q; }
	friend const sbigint operator ^ (int a, const sbigint& q) { return sbigint(a) ^ q; }

	friend const sbigint operator + (const sbigint& q, int a) { return q + sbigint(a); }
	friend const sbigint operator - (const sbigint& q, int a) { return q - sbigint(a); }
	friend const sbigint operator * (const sbigint& q, int a) { return q * sbigint(a); }
	friend const sbigint operator / (const sbigint& q, int a) { return q / sbigint(a); }
	friend const sbigint operator % (const sbigint& q, int a) { return q % sbigint(a); }
	friend const sbigint operator + (int a, const sbigint& q) { return sbigint(a) + q; }
	friend const sbigint operator - (int a, const sbigint& q) { return sbigint(a) - q; }
	friend const sbigint operator * (int a, const sbigint& q) { return sbigint(a) * q; }
	friend const sbigint operator / (int a, const sbigint& q) { return sbigint(a) / q; }
	friend const sbigint operator % (int a, const sbigint& q) { return sbigint(a) % q; }
};

#endif


#include<iostream>
#include<cstring>
#include<string>
#include<math.h>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
typedef ubigint<256> bigint;

bigint n[1023];
//ubigint<256> d[1023];
vector<bigint> d;
bigint t,a,b,c,r;
string ss;
int i,j,num,tmp1,tmp2,tmp3,k;
int main(){
	//freopen("B-small.in","r",stdin);freopen("B-small.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int ncases=0;
	scanf("%d",&ncases);
	for(int cc=1;cc<=ncases;cc++){
		d.clear();
		for(i=0;i<1022;i++){n[i]=0;}
		t=0;b=0;a=0;c=0;r=0;ss="";i=0;j=0;num=0;tmp1=0;tmp2=0;tmp3=0;k=0;
		cin>>num;
		for(i=0;i<num;i++){
			cin>>ss;
			n[i]=sbigint<256>(ss);
		}
		for(i=0;i<num-1;i++){
			if(n[i]-n[i+1]==0)continue;
			if(n[i]>n[i+1]){
				t=n[i]-n[i+1];
				d.push_back(t);
			}
			else
			{
				t=n[i+1]-n[i];
				d.push_back(t);
			}
		}
		if(d.size()==0)
			b=0;
		else
			b=d[0];
		for(i=1;i<d.size();i++){
			a=d[i];b=d[i-1];
			if(a<b){t=a;a=b;b=t;}
			c=a%b;
			while(c!=0){
				a=b;b=c;c=a%b;
			}
			d[i]=b;d[i-1]=b;
			//cout<<"b "<<b<<endl;
		}
		if(b==0)r=n[0];
		else if(n[0]%b==0)
		r=0;
		else
		r=b-n[0]%b;
		cout<<"Case #"<<cc<<": "<<r<<"\n";
	}
}