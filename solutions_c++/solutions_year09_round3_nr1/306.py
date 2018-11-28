
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int T;

int remap(char c)
{
	if (c>='a')
		return c-'a'+10;
	return c-'0';
}

long long solve(string s)
{
	int f[36];
	int rm[36];
	int base=0;
	memset(f, 0, sizeof(f));
	memset(rm, 0, sizeof(rm));
	for (int i=0; i < s.length();i++)
		f[remap(s[i])]=1;

	for (int i=0; i < 36;i++)
		base+=f[i];
	if (base==1)
		base = 2;

	int nextDig=1;
	for (int i=0;i<s.length();)
	{
		if (s[i] < '0')
		{
			i++;
			continue;
		}
		char c = s[i];
		for (int j = i; j < s.length(); j++)
			if (s[j]==c)
				s[j] = nextDig;
		if (nextDig == 1)
			nextDig = 0;
		else
			if (nextDig == 0)
				nextDig = 2;
			else
				nextDig++;
		i++;
	}
	long long res;
	long long b=1;
	res = 0;
	for (int i = s.length()-1; i>=0; i--)
	{
		res+=s[i]*b;
		b*=base;
	}
	return res;
}

void test()
{
//	solve();
}

int main()
{
	test();
	ifstream f("A-large.in");
	ofstream of("output.out");

	f >> T;
	for (int i = 0; i < T; i++)
	{
		string s;
		f >> s;
		long long res = solve(s);
		of << "Case #" << i+1 << ": " << res << endl;
	}
}
