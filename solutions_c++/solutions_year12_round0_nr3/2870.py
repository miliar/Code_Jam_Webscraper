// RecycledNumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int c[8];

inline int digits(int a)
{
	if (a > 999999)
		return 7;
	else if (a > 99999)
		return 6;
	else if (a > 9999)
		return 5;
	else if (a > 999)
		return 4;
	else if (a > 99)
		return 3;
	else if (a > 9)
		return 2;
	return 1;
}

inline int pow(int e)
{
	int r = 1;
	while (e--)
		r *= 10;
	return r;
}

inline void toArray(int n, int d)
{
	int i = 0, p;
	while (d > i)
	{
		p = pow(d - i - 1);
		c[i++] = n / p;
		n %= p;
	}
}

inline int isRecycled(int n, int a, int b)
{
	int d = digits(n), m, r = 0;
	toArray(n, d);
	for (int i = 1; i < d; i++)
	{
		if (c[i] != 0 && c[i] >= c[0])
		{
			m = 0;
			for (int j = 0; j < d; j++)
				m += c[(i + j) % d] * pow(d - j - 1);
			if (m > n && m <= b)
			{
				r++;
			}
		}
	}
	if (r && d == 4 && c[0] == c[2] && c[1] == c[3])
		r /= 2;
	else if (d == 6 && c[0] == c[2] && c[0] == c[4] && c[1] == c[3] && c[1] == c[5])
		r -= 3;
	else if (r && d == 6 && c[0] == c[3] && c[1] == c[4] && c[2] == c[5])
		r /= 2;
	return r;
}

int main(int argc, char* argv[])
{
	int t, a, b, r;
	cin>>t;
	for (int i = 1; i <= t; i++)
	{
		r = 0;
		cin>>a>>b;
		for (int j = a; j <= b; j++)
			r += isRecycled(j, a, b);
		cout<<"Case #"<<i<<": "<<r<<endl;
	}
	return 0;
}

