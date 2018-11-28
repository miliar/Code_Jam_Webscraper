#include<cstdio>
#include<fstream>
#include<iostream>
using namespace std;
int t, r, n, k, g[2005], nnext[1005], nr[1005], byl[1005], tera, runda;
long long s[1005], cyk[1005], ret;
ifstream istr("plik.txt");
ofstream ostr("out.txt");
void lecim()
{
	istr >> r >> k >> n;
	for(int i = 0; i < n; ++i)
	{
		istr >> g[i];
		g[n + i] = g[i];
		byl[i] = 0;
	}

	for(int i = 0; i < n; ++i)
	{
		s[i] = 0;
		int pos = 0;
		while(pos < n && s[i] + g[i+pos] <= k) s[i] += g[i+(pos++)];
		nnext[i] = (i + pos) % n;
	}

	ret = 0;
	tera = 0;
	runda = 0;

	while(runda < r && !byl[tera])
	{
		byl[tera] = 1;
		cyk[tera] = ret;
		ret += s[tera];
		nr[tera] = runda;
		tera = nnext[tera];
		++runda;
	}

	if (runda < r)
	{
		ret += ((r - runda) / (runda - nr[tera])) * (ret - cyk[tera]);
		runda = r - ((r - runda) % (runda - nr[tera]));
	}

	while(runda < r)
	{
		ret += s[tera];
		cyk[tera] = ret;
		nr[tera] = runda;
		tera = nnext[tera];
		++runda;
	}

	ostr << ret << "\n";
}

int main()
{
	istr >> t;
	for(int i = 1; i <= t; ++i)
	{
		ostr << "Case #" << i << ": ";
		lecim();
	}

	istr.close();
	ostr.close();
	return 0;
}