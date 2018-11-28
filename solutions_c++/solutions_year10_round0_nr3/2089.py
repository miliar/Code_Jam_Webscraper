#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it!=(v).end(); ++it)
int atoi(string &x) { stringstream ss(x); int temp; ss>>temp; return temp;}
string itoa(int i) { stringstream ss; ss<<i; return ss.str();}

const int MAXN = 100;

class BigInt
{	
	int len;
	int s[MAXN];
public:
	BigInt() { memset(s, 0, sizeof(s)); len = 1;}
	BigInt(const char* num) { *this = num;}
	BigInt(const int num) { *this = num;}

	long long asInt64() const
	{
		long long res = 0;
		int p = MAXN-1;
		while (s[p] == 0)
			p--;

		long long power = 1;
		for (int i=0; i<=p; i++)
		{
			res += s[i]*power;
			power*=10;
		}
		return res;
	}

	BigInt& operator = (const char* num)
	{
		len = strlen(num);
		for (int i=0; i<len; i++)
			s[i] = num[len-1-i] - '0';
		return *this;
	}

	BigInt& operator = (const int num)
	{
		char temp[MAXN];
		sprintf(temp, "%d", num);
		*this = temp;
		return *this;
	}

	string str() const
	{
		string res = "";
		for (int i=0; i<len; i++)
			res = char(s[i]+'0') + res;
		if (res == "") res = "0";
		return res;
	}

	BigInt operator + (const BigInt& x) const
	{
		BigInt res;
		res.len = 0;
		for (int i=0, g=0; g!=0 || i<max(len, x.len); i++)
		{
			int d = g;
			if (i<len) d += s[i];
			if (i<x.len) d += x.s[i];
			res.s[res.len++] = d % 10;
			g = d / 10;
		}
		return res;
	}

	BigInt operator - (const BigInt& x) const
	{
		BigInt res;
		res.len = 0;
		for (int i=0, g=0; i < len; i++)
		{
			int d = s[i] - g;
			g = 0;
			if (d < x.s[i])
			{
				d += 10;
				g = 1;
			}
			if (i < x.len)
				d -= x.s[i];
			res.s[res.len++] = d;
		}
		int p = res.len - 1;
		while (res.s[p] == 0)
		{
			res.len--;
			p--;
		}
		return res;
	}

	BigInt operator * (const BigInt& x) const
	{
		BigInt res;
		for (int i=0; i<x.len; i++)
		{
			int digit = x.s[i];
			for (int j=0, g=0; g!=0 || j<len; j++)
			{
				int d = s[j] * digit + g;
				res.s[j+i] += d;
				g = res.s[j+i] / 10;
				res.s[j+i] %= 10;
			}
		}
		int p = MAXN-1;
		while (res.s[p] == 0)
			p--;
		res.len = p+1;
		return res;
	}

	BigInt& operator += (const BigInt& x) { *this = *this + x; return *this;}
	BigInt& operator -= (const BigInt& x) {	*this = *this - x; return *this;}
	BigInt& operator *= (const BigInt& x) {	*this = *this * x; return *this;}

	bool operator < (const BigInt& x) const
	{
		if (len != x.len) return len < x.len;
		for (int i=len-1; i>=0; i--)
			if (s[i] != x.s[i]) return s[i] < x.s[i];
		return false;
	}

	bool operator > (const BigInt& x) const { return x < *this;}
	bool operator <= (const BigInt& x) const { return !(x < *this);}
	bool operator >= (const BigInt& x) const { return !(*this < x);}
	bool operator != (const BigInt& x) const { return x < *this || *this < x;}
	bool operator == (const BigInt& x) const { return !(x < *this) && !(*this < x);}

	friend istream& operator >> (istream& is, BigInt& x);
	friend ostream& operator << (ostream& os, BigInt& x);
};

istream& operator >> (istream& is, BigInt& x)
{
	string s;
	is >> s;
	x = s.c_str();
	return is;
}

ostream& operator << (ostream& os, const BigInt& x)
{
	os << x.str();
	return os;
}

ifstream fin;
ofstream fout;

void solve(int c)
{
	int R, k, N;
	fin >> R >> k >> N;
	deque<int> size;
	for (int i=0; i<N; i++)
	{
		int s;
		fin >> s;
		size.push_back(s);
	}

	long long euro = 0;
	for (int round = 0; round < R;round++)
	{
		int remain = k;
		deque<int> newqueue;
		while (!size.empty() && remain >= size.front())
		{
			remain -= size.front();
			newqueue.push_back(size.front());
			size.pop_front();
		}
		euro += k - remain;
		while (!newqueue.empty())
		{
			size.push_back(newqueue.front());
			newqueue.pop_front();
		}
	}

	fout << "Case #" << c << ": " << euro << endl;
}

int main() {
	fin.open("C-small.in");
	fout.open("C-small.out");

	int numCases;
	fin >> numCases;
	for (int c=1; c<=numCases; c++)
		solve(c);

	fin.close();
	fout.close();
	return 0;
}

