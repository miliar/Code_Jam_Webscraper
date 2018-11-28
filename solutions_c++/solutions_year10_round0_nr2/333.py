// bigint.cpp
//
#include "bigint.h"
#include <iostream>
#include <cassert>
#include <cstdlib>
using namespace std;

// return -1 if a < b
// return  0 if a == b
// return +1 if a > b
int bigcmp(bigint a, bigint b)
{
//cout << "bigcmp: " << big2int(a) << " " << big2int(b) << " size ";
	int na = a.size();
	int nb = b.size();
	while(na-1 > 0 && a[na-1] == 0)
		na--;
	while(nb-1 > 0 && b[nb-1] == 0)
		nb--;
//cout << na << " " << nb << endl;

	if (na < nb) return -1;
	if (na > nb) return 1;
	for(int i=na-1; i >= 0; i--)
	{
		if (a[i] > b[i]) return 1;
		else if (a[i] < b[i]) return -1;
	}
	return 0;
}

bigint
bigsub(bigint a, bigint b)
{
//cout << "bigsub " << big2int(a) << " " << big2int(b) << endl;
	assert(bigcmp(a,b) >= 0);
	int pa = a.size()-1;
	int pb = b.size()-1;
	int na = a.size();
	int nb = b.size();

	bigint c;

	int borrow = 0;
	for(int i=0; i < na; i++)
	{
		int da = a[i];
		int db = 0; if (i < nb) db = b[i];
		int dc = da - db - borrow;
		if (dc < 0) { dc += 10; borrow=1; }
		else borrow = 0;
		c.push_back(dc);
	}
//	cout << big2int(c) << endl;
	bigint ret;
	int pp = c.size()-1;
	for(; pp>=0 && c[pp] == 0; pp--);
	for(int i=0; i <= pp; i++)
		ret.push_back(c[i]);
	if (ret.empty())
		ret.push_back(0);
	return ret;
}

bigint abssub(bigint a, bigint b)
{
	if (bigcmp(a,b) < 0) return bigsub(b,a);
	else return bigsub(a,b);
}

bigint bigsum(bigint a, bigint b)
{
	bigint c;
	int carry = 0;
	int na = a.size();
	int nb = b.size();
	for(int i=0; i < max(na,nb); i++)
	{
		int da = 0; if (i < na) da = a[i];
		int db = 0; if (i < nb) db = b[i];
		int dc = da + db + carry;
		if (dc >= 10) { dc -= 10; carry = 1; }
		else carry = 0;
		c.push_back(dc);
	}
	if (carry) c.push_back(carry);
	return c;
}

bigint bigmult(bigint a, bigint b)
{
	bigint c(1,0);
	int na = a.size();
	int nb = b.size();
	for(int i=0; i < nb; i++)
	{
		int carry = 0;
		int db = b[i];
		bigint t(i,0);
		for(int ia=0; ia < na; ia++)
		{
			int da = a[ia];
			int dc = da * db + carry;
			carry = dc / 10; dc %= 10;
			t.push_back(dc);
		}
		if (carry)
			t.push_back(carry);
		//cout << big2int(t) << endl;
		//cout << big2int(t) << " " << big2int(c) << endl;
		c = bigsum(c, t);
	}
	return c;
}

void bigdiv(bigint a, bigint b, bigint &quo, bigint &rem)
{
assert(bigcmp(b,parseint(0)) > 0);
//cout << "bigdiv: " << big2int(a) << " " << big2int(b) << endl;
	quo.clear(); rem.clear();
	if (bigcmp(a,b) < 0)
	{
		quo = parseint(0); rem = a;
		//cout << "quo " << big2int(quo) << "\trem " << big2int(rem) << endl;
		return;
	}

	int pa = a.size()-1; while(pa > 0 && a[pa] == 0) pa--;
	int pb = b.size()-1; while(pb > 0 && b[pb] == 0) pb--;
	int na = pa+1;
	int nb = pb+1;

	//cout << "pa " << pa << " " << na << " " << pb << " " << nb << endl;
	bigint t(nb+1,0); // t holds rem from last div
	for(int i=pa, j=pb; j>=0; i--, j--)
	{
		t[j] = a[i];
	}
	pa -= nb;
	if (bigcmp(t,b) >= 0) // left shift t by 1
	{
		for(int i=0; i < nb; i++)
		{
			t[i] = t[i+1];
		}
		assert(t[nb]==0 && t[nb-1]==0);
		pa++;
	} 

	while(pa >= 0)
	{
		assert(bigcmp(t,b) < 0);
		// shift t up by 1
		int nt=t.size();
		for(int i=nt-1; i>0; i--)
		{
			t[i] = t[i-1];
		}
		t[0] = a[pa--]; // get next digit
//	cout << "t " << big2int(t) << endl;
		// t div b
		int m;
		nt = t.size();
		assert(nt>=2);
		m = 10*t[nt-1] + t[nt-2];
		m /= b[pb]; //cout << big2int(t) << " " << m << endl;
		while (bigcmp(t, bigmult(b, parseint(m))) < 0)
			m--;
		if (m <= 0) { quo.push_back(0); continue; }
		quo.push_back(m);
//		cout << "m " << m << "\t" << big2int(bigmult(b,parseint(m))) << endl;
		bigint sub = bigsub(t,bigmult(b,parseint(m)));
		assert(sub.size() <= b.size());
		for(int i=0; i < sub.size(); i++)
			t[i] = sub[i];
		for(int i=sub.size(); i < t.size(); i++)
			t[i] = 0;
		assert(t[t.size()-1]==0);
	}

	// reverse quo
	for(int i=0; i < quo.size()/2; i++)
	{
		int tmp = quo[i]; quo[i] = quo[quo.size()-1-i]; 
		quo[quo.size()-1-i] = tmp;
	}
	// copy t to rem
	rem = t;
	//cout << "quo " << big2int(quo) << "\trem " << big2int(rem) << endl;
}

bigint parseint(int n)
{
	bigint ret;
	do
	{
		ret.push_back(n%10);
		n /= 10;
	} while(n);

	return ret;
}

int big2int(bigint b)
{
	int ret=0;
	for(int i=b.size()-1; i >= 0; i--)
		ret = ret*10 + b[i];
	return ret;
}

void bigprint(bigint b)
{
	int p = b.size()-1;
	for(; p>= 0 && b[p] == 0; p--);
	if (p < 0) cout << 0 << endl;
	else 
	{
		for(; p >=0; p--)
			cout << b[p];
		cout << endl;
	}
}

// test code
/**************************8
int main()
{
	int a[] = {15000000, 0,1, 123, 79, 10000, 1953, 9999, 195, 0, 1, 100, 91, 123, 5943, 12300012};
	int b[] = {5000000, 0,1, 97,  35, 3, 729, 1, 0, 195, 10, 19, 1, 1, 296, 123};

	cout << "test bigcmp\n";
	for(int i=0; i < sizeof(a)/sizeof(int); i++)
	{
		cout << a[i] << "\t" << b[i] << endl;
		bigint aa = parseint(a[i]);
		bigint bb = parseint(b[i]);
		cout << bigcmp(aa, bb) << "\t" << bigcmp(bb,aa) << endl;
	}

	cout << "test bigsum\n";
	for(int i=0; i < sizeof(a)/sizeof(int); i++)
	{
		cout << a[i] << "\t" << b[i] << endl;
		bigint aa = parseint(a[i]);
		bigint bb = parseint(b[i]);
		int bigres = big2int(bigsum(aa,bb));
		int res = a[i] + b[i];
		cout << bigres << "\t" << res << endl;
		assert(bigres == res);
	}

	cout << "test bigsub\n";
	for(int i=0; i < sizeof(a)/sizeof(int); i++)
	{
		cout << a[i] << "\t" << b[i] << endl;
		if (a[i] < b[i]) { cout << "a < b\n"; continue; }
		bigint aa = parseint(a[i]);
		bigint bb = parseint(b[i]);
		int bigres = big2int(bigsub(aa,bb));
		int res = a[i] - b[i];
		cout << bigres << "\t" << res << endl;
		assert(bigres == res);
	}

	cout << "test abssub\n";
	for(int i=0; i < sizeof(a)/sizeof(int); i++)
	{
		cout << a[i] << "\t" << b[i] << endl;
		bigint aa = parseint(a[i]);
		bigint bb = parseint(b[i]);
		int bigres = big2int(abssub(aa,bb));
		int res = abs(a[i] - b[i]);
		cout << bigres << "\t" << res << endl;
		assert(bigres == res);
	}

	cout << "test bigmult\n";
	for(int i=0; i < sizeof(a)/sizeof(int); i++)
	{
		cout << a[i] << "\t" << b[i] << endl;
		bigint aa = parseint(a[i]);
		bigint bb = parseint(b[i]);
		int bigres = big2int(bigmult(aa,bb));
		int res = a[i] * b[i];
		cout << bigres << "\t" << res << endl;
		assert(bigres == res);
	}

	cout << "test bigdiv\n";
	for(int i=0; i < sizeof(a)/sizeof(int); i++)
	{
		cout << a[i] << "\t" << b[i] << endl;
		if (b[i] == 0) { cout << "div by zero\n"; continue; }
		bigint aa = parseint(a[i]);
		bigint bb = parseint(b[i]);
		bigint quo, rem;
		bigdiv(aa,bb,quo,rem);
		int myquo   = big2int(quo);
		int truequo = a[i] / b[i];
		int myrem   = big2int(rem);
		int truerem = a[i] % b[i];
		cout << "(" << truequo << "," << truerem << ")" << "\t" 
			"(" << myquo << "," << myrem << ")" << endl;
		assert(truequo == myquo && truerem == myrem);
	}

	// random test
	srand((unsigned)time(NULL));
	for(int i=0; i < 1000; i++)
	{
		int ra = (int)(rand()/(double)RAND_MAX * 10000); 
		int rb = (int)(rand()/(double)RAND_MAX * 10000);
		cout << ra << "\t" << rb << endl;
		bigint aa = parseint(ra);
		bigint bb = parseint(rb);
		assert(big2int(bigsum(aa,bb)) == ra+rb);
		assert(big2int(bigsum(bb,aa)) == ra+rb);

		if (ra < rb)
			assert(big2int(bigsub(bb,aa)) == rb-ra);
		else
			assert(big2int(bigsub(aa,bb)) == ra-rb);

		assert(big2int(abssub(aa,bb)) == abs(ra-rb));
			
		assert(big2int(bigmult(aa,bb)) == ra*rb);
		assert(big2int(bigmult(bb,aa)) == ra*rb);
		if (rb == 0) { cout << "div by zero\n"; continue; }
		bigint quo, rem;
		bigdiv(aa,bb,quo,rem);
		int myquo   = big2int(quo);
		int truequo = ra / rb;
		int myrem   = big2int(rem);
		int truerem = ra % rb;
		cout << "(" << truequo << "," << truerem << ")" << "\t" 
			"(" << myquo << "," << myrem << ")" << endl;
		assert(truequo == myquo && truerem == myrem);
	}
}
*********************/
// end of test code
// leading zero caused issue in bigcmp since size needs to be trimmed
// leading zero in bigdiv caused div-by-zero
