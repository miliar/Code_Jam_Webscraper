#include <iostream>
#include <fstream>
#include <gmpxx.h>

mpz_class getgcd(mpz_class v1, mpz_class v2)
{
	mpz_class t;
	if(v1 < v2)
	{
		t = v1;
		v1 = v2;
		v2= t;
	}
	while(1)
	{
		t = v1 %v2;
		if(t ==0)
		{
			return v2;
		}
		v1 = v2;
		v2 = t;
	}
	return 1;
}
mpz_class solve(int c, mpz_class* v)
{
	mpz_class min = v[0];
	mpz_class diff[1000];
	int diff_c = 0;
	for(int i =1; i < c;++i)
	{	
		if(v[i] > v[i -1])
		{
			diff[diff_c] = v[i] - v[i-1];
			diff_c++;
		}
		else if(v[i-1] > v[i])
		{
			diff[diff_c] = v[i-1] - v[i];
			diff_c++;
		}
		if(min > v[i])
		{
			min = v[i];
		}
	}
	
	mpz_class gcd = diff[0];
	for(int i =1;i < diff_c;++i)
	{
		gcd = getgcd(gcd, diff[i]);
	}
	mpz_class t = min % gcd;
	if(t >0)
	{
		return gcd - t;
	}
	return 0;
}

int main(int argc, char* argv[])
{
	std::ifstream inf(argv[1]);
	int cases ;
	inf >> cases;
	

	for(int i =0; i < cases;++i)
	{
		mpz_class v[1000];
		int ec = 0;
		inf >> ec;
		for(int j =0; j < ec;++j)
		{
			inf >> v[j];
		}
		std::cout << "Case #" << i+1 << ": " << solve(ec, v) << std::endl;
	}
	return 0;
}
