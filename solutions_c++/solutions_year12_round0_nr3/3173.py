#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <cstdlib>

using namespace std;

long long fac(long long n)
{
	if (n == 0) return 1;
	if (n == 1) return 1;
	return n * fac(n-1);
}

long long comb(long long n)
{
	return (fac(n) / (2*fac(n-2)));
}


long long resolve(long long n,long long m)
{
	long long tmp;
	long long res = 0;
	for(long long i = n; i < m ; ++i)
	{
		//tmp3 = 0;
		string sn;
		vector<long long> rep;
		char tmp2[10];
		sn = ltoa(i,tmp2,10);
		rotate(sn.begin(),sn.begin() +1, sn.end());
		tmp = atol(sn.c_str());
		while(tmp != i)
		{
			if(tmp > i && tmp <= m ) 
			{
				++res;
			}
			rotate(sn.begin(),sn.begin() +1, sn.end());
			tmp = atol(sn.c_str());
		}
		//if(tmp3)
		//res += comb(1 + tmp3);
	}
	return res;
}

int main()
{
	std::ifstream file("C-small-attempt1.in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	long long nb,n,m;

	file >> nb;

	for(long long i = 0; i < nb ; ++i)
	{
		file >> n;
		file >> m;

		file2 << "Case #" << i+1 << ": " << resolve(n,m) << endl;
	}
}