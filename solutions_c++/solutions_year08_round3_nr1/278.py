#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <vector>

long long DoTest(std::istream& f, int TestNum)
{
	int P, K, L;
	std::vector<long long> a;
	f>>P>>K>>L;
	for (int i = 0; i < L; ++i)
	{
		long long tmp;
		f>>tmp;
		a.push_back(tmp);
	}
	long long res = 0;
	if ( P*K >= L)
	{
		std::sort(a.begin(),a.end(),std::greater<long long>());

		long long mnozh = 1;
		for (int i = 0; i < L; ++i)
		{
			if (i == K*mnozh) mnozh++;
			res+=mnozh*a[i];
		}
	}
	else
	{
		res = -1;
	}

	if (res == -1)
		std::cout<<"Case #"<<TestNum<<": Impossible"<<std::endl;
	else
		std::cout<<"Case #"<<TestNum<<": "<<res<<std::endl;
	return 0;
}

int main(int argc, char** argv)
{
	int T;
//	std::ifstream f("A.in");
	std::cin>>T;
	for (int i = 0; i < T; ++i)
	{
		DoTest(std::cin, i+1);
	}
}
