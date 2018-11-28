using namespace std;
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define PB push_back
#define ALL(x) ((x).begin()),((x).end())
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)

const int infty = 999999999;

/* Algorithms for Big Number emulation (without sign) */

using namespace std;
#include <iostream>
#include <sstream>
#include <string>

const int maxdigits = 100;
// keep maxdigits < maxint/100 for correct functioning of *(bignum,bignum)

// Base 10 bignumber:
class bignum {
public:
	unsigned int d[maxdigits];

	bignum() { for(int i=0; i<maxdigits; i++) d[i] = 0; }
	bignum(long long n) {
		int i;
		for(i=0; i<maxdigits; i++) d[i] = 0;
		for(i=0; n!=0; i++) { d[i] = n%10; n /= 10; }
	}
  
	bignum(string str) { // no error check!
		int i,n = str.length();
		for(i=0; i<maxdigits; i++) d[i] = 0;
		for(i=n-1; i>=0; i--) d[n-1-i] = str[i]-'0';
	}

	operator int() { // no overflow check!
		int res = 0, base = 1;
		for(int i=0; i<maxdigits; i++) {
			res += d[i]*base;
			base *= 10;
		}
		return res;
	}
	
	int ndigits() {
		int i;
		for(i=maxdigits-1; (d[i]==0 && i>=0); i--);
		return i+1;
	}

	string str() {
		if ( this->ndigits()==0 ) return "0";
		string res;
		for(int i=this->ndigits()-1; i>=0; i--) res += '0'+d[i];
		return res;
	}
	
	// shifts digits ndig to the left (like << operator but now base 10)
	bignum shl(int ndig) {
		int i;
		for(i=maxdigits-1; i>=ndig; i--) d[i] = d[i-ndig];
		for(; i>=0; i--) d[i] = 0;
		return *this;
	}

	// equivalent shift to right as above
	bignum shr(int ndig) {
		int i;
		for(i=0; i<maxdigits-ndig; i++) d[i] = d[i+ndig];
		for(; i<maxdigits; i++) d[i] = 0;
		return *this;
	}
	
	bignum operator +=(bignum a) {
		int i, carry = 0;
		for(i=0; i<maxdigits; i++) {
			d[i] += a.d[i] + carry;
			carry = d[i] / 10;
			d[i] %= 10;
		}
		return *this;
	}

	bignum operator -=(bignum a) {
		int i, carry = 0;
		
		for(i=0; i<maxdigits; i++) {
			d[i] += 10 - a.d[i] - carry;
			carry = d[i]>=10 ? 0 : 1;
			d[i] %= 10;
		}
			return *this;
	}
	
	bignum operator *=(bignum a) {
		bignum res;
		int i,j, carry = 0;
		
		for(i=0; i<maxdigits; i++) {
			res.d[i] = carry;
			for(j=0; j<=i; j++) res.d[i] += d[j] * a.d[i-j];
			carry = res.d[i] / 10;
			res.d[i] %= 10;
		}
		return *this = res;
	}

	bignum operator /=(unsigned long long a) {
		int i, carry = 0;
		
		for(i=maxdigits-1; i>=0; i--) {
			d[i] += carry*10;
			carry = d[i] % a;
			d[i] /= a;
		}
		return *this;
	}
	
	int operator ==(bignum a) {
		int i;
		for(i=0; i<maxdigits; i++) if ( d[i]!=a.d[i] ) return 0;
		return 1;
	}

	int operator <(bignum a) {
		int i;
		for(i=maxdigits-1; (i>0 && d[i]==a.d[i]); i--);
		return d[i] < a.d[i];
	}

	int operator >(bignum a) {
		int i;
		for(i=maxdigits-1; (i>0 && d[i]==a.d[i]); i--);
		return d[i] > a.d[i];
	}

	int operator <=(bignum a) {
		int i;
		for(i=maxdigits-1; (i>0 && d[i]==a.d[i]); i--);
		return d[i] <= a.d[i];
	}

	int operator >=(bignum a) {
		int i;
		for(i=maxdigits-1; (i>0 && d[i]==a.d[i]); i--);
		return d[i] >= a.d[i];
	}

	int divide(bignum div, bignum &quotient, bignum &remainder) {
		bignum tmp;
		int nshift;

		if ( div==bignum(0) ) {
			cerr << "Bignum error: division by zero!" << endl;
			return 0;
		}

		quotient = bignum(0);
		remainder = *this;
    
		tmp = div;
		nshift = 0;
		while ( tmp<=remainder && tmp.ndigits()<maxdigits ) {
			tmp.shl(1);
			nshift++;
		}
		tmp.shr(1);
		nshift--;

		while ( remainder>=div ) {
			while ( tmp<=remainder ) {
				quotient.d[nshift]++;
				remainder -= tmp;
			}
			tmp.shr(1);
			nshift--;
		}
		return 1;
	}
  
	bignum operator /=(bignum a) {
		bignum quot, rem;
		divide(a,quot,rem);
		return quot;
	}
  
	bignum operator %=(bignum a) {
		bignum quot, rem;
		divide(a,quot,rem);
		return rem;
	}
};

bignum operator +(bignum a, bignum b) { return a += b; }
bignum operator -(bignum a, bignum b) { return a -= b; }
bignum operator *(bignum a, bignum b) { return a *= b; }
bignum operator /(bignum a, bignum b) { return a /= b; }
bignum operator %(bignum a, bignum b) { return a %= b; }

bignum operator /(bignum a, unsigned long long b) { return a /= b; }

ostream &operator <<(ostream &s, bignum a)
{
	s << a.str();
	return s;
}

istream &operator >>(istream &s, bignum &a)
{
	string str;
	s >> str;
	a = bignum(str);
	return s;
}

//#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

const int maxL = 45;

const int primes[] = {2,3,5,7};

int main()
{
	int run, nruns;
	string n;
	char tmp[100];
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {

		scanf("%s\n",tmp);
		n = string(tmp);
		
		map<VI,bignum> freq[maxL];

		VI modszero(4,0);
		freq[0][modszero] = 1;

		for(int i=1; i<=n.length(); i++)
			for(int j=0; j<i; j++) {
				debug("%d -> %d:\n",j,i);
				bignum x(n.substr(j,i-j));
				VI moddiff = VI(4);
				for(int p=0; p<4; p++) {
					moddiff[p] = (int)(x % (bignum)primes[p]);
				}
				FOR(it,freq[j]) {
					// plus
					VI modsnew = it->first;
					for(int p=0; p<4; p++) {
						modsnew[p] += moddiff[p];
						modsnew[p] %= primes[p];

						debug("%d ",(it->first)[p]);
					}
					freq[i][modsnew] += it->second;
					debug(": %s += %s\n",freq[i][modsnew].str().c_str(),
						  it->second.str().c_str());

					if ( j==0 ) continue;
					// minus
					modsnew = it->first;
					for(int p=0; p<4; p++) {
						modsnew[p] += (primes[p]-moddiff[p]);
						modsnew[p] %= primes[p];

						debug("%d ",(it->first)[p]);
					}
					freq[i][modsnew] += it->second;
					debug(": %s += %s\n",freq[i][modsnew].str().c_str(),
						  it->second.str().c_str());
				}
			}

//		debug("%d = %s\n",n.length(),freq[n.length()][modszero].str().c_str());

		bignum res(0);
		FOR(it,freq[n.length()]) {
			if ( it->first[0]==0 ||
				 it->first[1]==0 ||
				 it->first[2]==0 ||
				 it->first[3]==0 ) res += it->second;
		}
		
		printf("Case #%d: %s\n",run+1,res.str().c_str());
	}

	return 0;
}
