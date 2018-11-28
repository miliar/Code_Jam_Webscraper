/******************\
*    CPP source    *
*     By HPFDF     *
\******************/
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <complex>
#include <vector>
#include <map>
#include <set>
#define rep(i,n)   for(int i=0;i<(n);++i)
#define fab(i,a,b) for(int i=(a);i<=(b);++i)
#define fba(i,b,a) for(int i=(b);i>=(a);--i)
#define fec(i,a)   for(typeof(a.end())i=a.begin();i!=a.end();++i)
#define fpc(i,v)   for(int i=a[v];i;i=nx[v])
#define fil(a)     memset(a,0,sizeof(a))
#define all(a)     a.begin(),a.end()
#define rdm        srand(time(NULL))
using namespace std;
const int HX = 0x3F3F3F3F;
/****************************\
*            MAIN            *
\****************************/


int t, n, m, k;
ifstream fin("B-large.in");
ofstream fou("B-large.out");
//#define fin cin
//#define fou cout

struct big_int
{
	int data[256];
	big_int(int x = 0)
	{
		data[0] = 0;
		while (x) data[++data[0]] = x % 10, x /= 10;
	}
	int& operator [] (int x)
	{
		if (x > data[0]) data[x] = 0;
		return data[x];
	}
};
bool operator <(big_int a, big_int b)
{
	if (a[0] < b[0]) return true;
	if (a[0] > b[0]) return false;
	fba(i, a[0], 1)
		if (a[i] < b[i]) return true; else
		if (a[i] > b[i]) return false;
	return false;
}
bool operator ==(big_int a, big_int b)
{
	return !(a<b || b<a);
}

big_int operator +(big_int a, big_int b)
{
	int j, t = 0, k = max(a[0], b[0]);
	fab(i, 1, k)
	{
		j = t + a[i] + b[i];
		a[i] = j % 10;
		t = j > 9;
	}
	a[0] = k;
	if (t) a[++a[0]] = t;
	return a;
}

big_int operator -(big_int a, big_int b)
{
	if (a < b)
	{
		cout << "Runtime Error : Call a-b when a < b" << endl;
		exit(0);
	}
	int j, t = 0;
	fab(i, 1, a[0])
	{
		j = a[i] - b[i] - t;
		a[i] = (10 + j) % 10;
		t = j < 0;
	}
	while (a[a[0]] == 0 && a[0]) --a[0];
	return a;
}

ostream & operator << (ostream &f, big_int a)
{
	if (a[0] == 0) f << "0"; else
	fba(i, a[0], 1) f << a[i];
	return f;
}
istream & operator >> (istream &f, big_int &b)
{
	string s;
	f >> s;
	while (s.length() && s[0] == '0') s.erase(0, 1);
	b[0] = s.length();
	fba(i, b[0], 1) b[i] = s[b[0] - i] - '0';
	return f;
}

big_int operator %(big_int a, big_int b)
{
	//cout << a << "%" << b << endl;
	big_int t = b;

	rep(i, a[0] - b[0])
	{
		fba(i, t[0], 1)
			t[i + 1] = t[i];
		t[1] = 0;
		++t[0];
	}
	
	fba(i, a[0] - b[0], 0)
	{

		//cout << "Try : " << t << endl;
		while (!(a < t)) a = a - t;
		fab(i, 1, t[0] - 1)
			t[i] = t[i + 1];
		//cout << "Now a = " << a << endl;
		--t[0];
	}
	return a;
}

big_int gcd(big_int a, big_int b)
{
	big_int c = a;
	while (a[0])
	{
		a = b % a;
		b = c;
		c = a;
	}
	return b;
}
	

//	typedef long long big_int;
big_int a[1111];
int main()
{
	fin >> t;
	fab(T, 1, t)
	{
		fin >> n;
		rep(i, n) fin >> a[i];
		sort(a, a + n);
		big_int p(0);
		fab(i, 1, n - 1)
		{
			//if (p == 0) p = a[i] - a[i - 1]; else
			p = gcd(p, a[i] - a[i - 1]);
		}
		//cout << p << endl;
		if (!p[0])
			fou << "Case #" << T << ": 0\n"; else
			{
				//	cout << a[0] << endl;
				//	cout << (a[0] % p) << endl;
				//	cout << (p - (a[0] % p)) << endl;
				fou << "Case #" << T << ": " << (p - (a[0] % p)) % p << endl;
			}
	}
}

/****************************\
*            EOF             *
\****************************/



