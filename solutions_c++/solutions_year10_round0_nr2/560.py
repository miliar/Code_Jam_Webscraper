#include <iostream>
#include "stdio.h"
using namespace std;

#define MAX_DIGITS	51

class GLONG;

int numCount;
//unsigned long slarbo[1000];
GLONG* slb[2000];

class GLONG {
public:
	int	digits[MAX_DIGITS];
	int length;

	GLONG();
	int getAt(int index) { return digits[index]; }
	void assign(const char* str);
	void assign(GLONG& a);
	void decr(GLONG& a);
	void decrMul(GLONG& a, int exp10);
	void incr(GLONG& b);
	void incrMul(GLONG& a, int exp10);
	void updateLength();
	void shiftLeft(int exp10);
	bool isZero();
	bool isOne();
	bool isGreaterThan(GLONG& a);
	bool isLowerThan(GLONG& a);
	bool isPositive();
	void clear() { memset(digits, 0, sizeof(int) * MAX_DIGITS); length = 1; }
	string toString();
};

GLONG::GLONG()
{
	clear();
}

void GLONG::assign(GLONG& a)
{
	clear();
	for (int i = 0; i < MAX_DIGITS; i++)
		digits[i] = a.digits[i];
	//this->length = a.length;
	updateLength();
}

void GLONG::assign(const char* str)
{
	int len = strlen(str);
	int cur = MAX_DIGITS - 1;

	for(int i = len - 1; i >= 0; i--)
	{
		digits[cur--] = str[i] - '0';
	}
	updateLength();
}

void GLONG::decr(GLONG& b)
{
//	printf("decr %s , %s\n", toString().c_str(), b.toString().c_str());
//	printf("     %d , %d\n", this->length, b.length);

	int i, j;

	for (i = MAX_DIGITS - 1; i > 0; i--)
	{
		digits[i] -= b.getAt(i);
		if (digits[i] < 0)
		{
			digits[i] += 10;
			digits[i-1]--;
		}
	}
//	printf("after decr %s , %s\n", toString().c_str(), b.toString().c_str());
	updateLength();
}

void GLONG::shiftLeft(int e)
{
	for (int i = 0; i < e; i++)
	{
		for (int j = 0; j < MAX_DIGITS - 1; j++)
			digits[j] = digits[j + 1];
		digits[MAX_DIGITS - 1]  = 0;
	}
	updateLength();
}

void GLONG::decrMul(GLONG& m, int exp10)
{
	if (exp10 < 1)
	{
		decr(m);
		return;
	}

	GLONG b;
	b.assign(m);

	//printf("decrMul %s , %s, %d\n", toString().c_str(), b.toString().c_str(), exp10);
	b.shiftLeft(exp10);
	//printf("=decr %s , %s\n", toString().c_str(), b.toString().c_str());

	int i, j;

	for (i = MAX_DIGITS - 1; i > 0; i--)
	{
		digits[i] -= b.getAt(i);
		if (digits[i] < 0)
		{
			digits[i] += 10;
			digits[i-1]--;
		}
	}
	//printf("after decr %s , %s\n", toString().c_str(), b.toString().c_str());

	updateLength();
}

void GLONG::incr(GLONG& b)
{
//	printf("incr %s , %s\n", toString().c_str(), b.toString().c_str());
//	printf("     %d , %d\n", this->length, b.length);

	int i, j;

	for (i = MAX_DIGITS - 1; i > 0; i--)
	{
		digits[i] += b.digits[i];
		if (digits[i] > 9)
		{
			digits[i] -= 10;
			digits[i-1]++;
		}
	}
//	printf("after incr %s , %s\n", toString().c_str(), b.toString().c_str());
	updateLength();
}

void GLONG::incrMul(GLONG& m, int exp10)
{
	if (exp10 < 1)
	{
		incr(m);
		return;
	}

	GLONG b;
	b.assign(m);

//	printf("incrMul %s , %s, %d\n", toString().c_str(), b.toString().c_str(), exp10);
	b.shiftLeft(exp10);
//	printf("=incr %s , %s\n", toString().c_str(), b.toString().c_str());

	int i, j;

	for (i = MAX_DIGITS - 1; i > 0; i--)
	{
		digits[i] += b.digits[i];
		if (digits[i] > 9)
		{
			digits[i] -= 10;
			digits[i-1]++;
		}
	}
//	printf("after incr %s , %s\n", toString().c_str(), b.toString().c_str());
	updateLength();
}

void GLONG::updateLength()
{
	int i;

	for (i = 0; i < MAX_DIGITS; i++)
		if (digits[i])
			break;

	this->length = MAX_DIGITS - i;

	for (i = 0 ; i< MAX_DIGITS; i++)
		if (digits[i] < 0 || digits[i]>9)
			printf("ASSERTION FAILED. digits[%d]=%d\n", i, digits[i]);
}

bool GLONG::isZero() 
{
	for (int i = 0; i < MAX_DIGITS; i++)
		if (digits[i] != 0)
			return false;

	return true;
}

bool GLONG::isOne()
{
	if (digits[MAX_DIGITS] != 1)
		return false;

	for (int i = 0; i < MAX_DIGITS - 1; i++)
		if (digits[i] != 0)
			return false;

	return true;
}

bool GLONG::isPositive()
{
	for (int i = 0; i < MAX_DIGITS; i++)
	{
		if (digits[i] > 0)
			return true;
		if (digits[i] < 0)
		{
			printf("ASSERTION FAILED. digits[%d] is negative.\n", i);
		}
	}

	return false;
}

bool GLONG::isGreaterThan(GLONG& a)
{
	if (this->length > a.length)
		return true;
	if (this->length < a.length)
		return false;

	int i;
	for (i = 0; i < MAX_DIGITS; i++)
	{
		if (this->digits[i] > a.digits[i])
			return true;
		else if (this->digits[i] < a.digits[i])
			return false;
	}

	return false;
}

bool GLONG::isLowerThan(GLONG& a)
{
//	printf("isLowerThan\n%s\n%s\n", this->toString().c_str(), a.toString().c_str());

	if (this->length < a.length)
		return true;
	if (this->length > a.length)
		return false;

	int i;
	for (i = 0; i < MAX_DIGITS; i++)
	{
		if (this->digits[i] < a.digits[i])
			return true;
		else if (this->digits[i] > a.digits[i])
			return false;
	}

	return false;
}

string GLONG::toString()
{
	string r;
	int i;

	for (i = 0; i < MAX_DIGITS;i++)
	{
		if (digits[i])
			break;
	}
	for (; i < MAX_DIGITS; i++)
		r += (digits[i] + '0');

	if (r.length() < 1)
		r = "0";

	return r;
}

string get_token(string& src, int n)
{
	int	tc = -1;;
	int wspace = 1;
	string	strt;

	for (int i = 0, len = src.size(); i <= len; i++) 
	{
		if (src[i] == 0x0 || isspace(src[i])) 
		{
			if (!wspace)
			{
				if (tc == n)
					break;
			}
			wspace = 1;
		}
		else 
		{
			if (wspace)
			{
				wspace = 0;
				++tc;
			}
			if (tc == n)
				strt += src[i];
		}
	}

	return strt;
}


//unsigned long get_gcd(unsigned long a, unsigned long b)
GLONG* get_gcd(GLONG& m, GLONG &n)
{
	GLONG* r = new GLONG;

	if (m.isZero())
	{
		r->assign(n);
		return r;
	}
	
	if (m.isOne() || n.isOne())
	{
		r->assign("1");
		return r;
	}

	GLONG	a;
	GLONG	b;

	a.assign(m);
	b.assign(n);

	while (b.isPositive())
	{
		if (a.isGreaterThan(b))
		{
			if (a.length > b.length + 1)
				a.decrMul(b, (a.length - b.length - 1));
			else
				a.decr(b);
		}
		else
		{
			if (b.length > a.length + 1)
				b.decrMul(a, (b.length - a.length - 1));
			else
				b.decr(a);
		}

		if (b.isOne())
		{
			r->assign("1");
			return r;
		}
	}

	r->assign(a);

	return r;
}

int findSolution()
{
	GLONG* pGcd;
	GLONG* pGcd2;
	GLONG min;
	int min_i = 0;
	int i,j;

	// find minimum
	min.assign(*slb[0]);
	for (i = 1; i < numCount; i++)
	{
		//if (min > slarbo[i])
		if (min.isGreaterThan(*slb[i]))
		{
			//min = slarbo[i];
			min.assign(*slb[i]);
			min_i = i;
		}
	}

	for (i = 0; i < numCount; i++)
	{
		//slarbo[i] -= min;
		slb[i]->decr(min);
		//printf("%lu ", slarbo[i]);
	}
	//printf("\n");

	// get gcd
	pGcd = get_gcd(*slb[0], *slb[1]);
	for (i = 2; i < numCount; i++)
	{
		//gcd = get_gcd(gcd, slb[i]);
		pGcd2 = get_gcd(*pGcd, *slb[i]);
		delete pGcd; 
		pGcd = pGcd2;
	}

	// find nearest
//	printf("\ngcd=%s\nmin=%s\n", pGcd->toString().c_str(), min.toString().c_str());

	GLONG	val;
	GLONG	val2;
	GLONG	jump;
	val.assign(*pGcd);

	if (pGcd->isOne())
	{
		printf("0\n");
		return 0;
	}

	// fast go
	if (val.isLowerThan(min) && (min.length - val.length > 1))
	{
		int je = min.length - val.length - 1;
		while(je > 0)
		{
//			printf("val=%s\n", val.toString().c_str());
//			printf("x10..=%d\n", je);
			jump.assign(*pGcd);
			jump.shiftLeft(je);
			val2.assign(val);
			while(1) {
				val2.incr(jump);
				if (val2.isLowerThan(min))
					val.assign(val2);
				else
					break;
			}
			je--;
		}
//		printf("fast val=%s\n", val.toString().c_str());
//		if (val.isLowerThan(min))
//			printf("still lower than min\n");
	}

	while(val.isLowerThan(min))
	{
//		if (min.length - pGcd->length > 2)
//			val.incrMul(*pGcd, min.length - pGcd->length - 1);
//		else
			val.incr(*pGcd);
	}

	delete pGcd;

	val.decr(min);

	string result = val.toString();

	printf("%s\n", result.c_str());

	return 0;
}

int main()
{
	char buf[16384];
	string lbuf;
	string tbuf;
	int caseCount;
	int i,j;

	gets(buf);
	caseCount = atoi(buf);
	//printf("caseCount=%d\n", caseCount);
	for(i = 0; i < caseCount; i++)
	{
		gets(buf);
		lbuf = buf;
		tbuf = get_token(lbuf, 0);
		//printf("numCount=%s ", tbuf.c_str());
		numCount = atoi(tbuf.c_str());
		//printf("%d\n", numCount);

		//memset(slarbo, 0, sizeof(unsigned long)*1000);
		for (j =0 ; j<numCount; j++)
		{
			tbuf = get_token(lbuf, j + 1);

			if (caseCount == 91)
				printf("token[%d]=%s\n", j+1,tbuf.c_str());

			slb[j] = new GLONG;
			slb[j]->clear();
			slb[j]->assign(tbuf.c_str());
		}

		printf("Case #%d: ", i+1);
		findSolution();

		for (j =0 ; j<numCount; j++)
		{
			delete slb[j];
		}
	}
}

