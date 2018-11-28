#include<fstream>
#include<iostream>
#include<cmath>
#include<limits>
#include<vector>
#include<algorithm>
#include<deque>
#include<list>
using namespace std;

ifstream lettura ("input.txt");
ofstream scrittura ("output.txt");

long t, l, p, c;

void leggi ()
{
	lettura >> l >> p >> c;
}

int elabora ()
{
	long fattore = c;
	int result = -1;
	for (int i = 1; i < 1000000000 && result == -1; i++)
	{
		if (l * fattore >= p)
			result = i;
		fattore *= c;
	}
	fattore = 1;
	for (int i = 0; i < 1000000000; i++)
	{
		if (fattore >= result)
			return i;
		fattore *= 2;
	}
	return -1;
}

int main ()
{
	lettura >> t;
	for (int i = 0; i < t; i++)
	{
		leggi ();
		scrittura << "Case #" << (i+1) << ": " << elabora () << endl;
	}
}
