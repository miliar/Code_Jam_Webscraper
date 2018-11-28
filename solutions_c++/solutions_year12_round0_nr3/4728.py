#include <iostream>
#include <sstream>
#include <string>

long recycle(long A, long B)
{
long rec = 0;
for(long n = A; n < B; n++) { for(long m = n+1; m <= B; m++)
	{
		std::string nstr;
		std::string mstr;

		std::stringstream nstream;
		nstream << n;
		nstr = nstream.str();

		std::stringstream mstream;
		mstream << m;
		mstr = mstream.str();

		short numlen = nstr.length();
		std::string mcutl, mcutr;
		for(int i = 1; i < numlen; i++)
		{
			mcutl = mstr.substr(0,i);
			mcutr = mstr.substr(i);
//			std::cout << "DEBUG:" << i << " " << mstr << " l" << mcutl << " r" << mcutr << " " << nstr << "==" << mcutr + mcutl << std::endl;
			if(nstr == (mcutr + mcutl)) { rec++; break; };
		};
	};
};
return rec;
}

int main()
{
	int T;
	std::cin >> T;
	long A[T], B[T];
	for(int x = 0; x < T; x++)
	{
		std::cin >> A[x];
		std::cin >> B[x];
	
//	std::cout << "DEBUG: " << A[x] << " " << B[x] << std::endl;
	};

	long y[T];
	for(int x = 0; x < T; x++)
	{
		y[x] = recycle(A[x],B[x]);
		std::cout << "Case #" << x+1 << ": " << y[x] << std::endl;
	};
	return 0;
}
