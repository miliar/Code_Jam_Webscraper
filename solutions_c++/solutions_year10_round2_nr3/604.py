///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="C%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

//#ifdef GCONF_MSSTL_TUNING
#define _SECURE_SCL 0
#define _SCL_SECURE_NO_DEPRECATE
#define _HAS_ITERATOR_DEBUGGING 0
//#endif

//#undef _HAS_EXCEPTIONS
//#define _HAS_EXCEPTIONS 0

#include <set>
#include <vector>
#include <map>	
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <limits>
#include <memory>

template <class T>
inline const T& min(const T& a,const T& b)
{
	return (a < b)? a : b ;
}

template <class T>
inline const T& max(const T& a,const T& b)
{
	return (a > b)? a : b ;
}

#define VECTOR std::vector
#define LIST   std::list
#define SET    std::set
#define MAP    std::map
#define MULTIMAP std::multimap
#define DEQUE  std::deque
#define STACK  std::stack
#define PAIR   std::pair
#define AUTO_PTR std::auto_ptr

#define foreach(TYPE, CONT, ITER) for(TYPE::iterator ITER=(CONT).begin(); ITER != (CONT).end(); ++ITER)
#define foreach_const(TYPE, CONT, ITER) for(TYPE::const_iterator ITER=(CONT).begin(); ITER != (CONT).end(); ++ITER)

const bool OUT_FILE = true;
FILE *FILE_OUT;

///////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
typedef unsigned int NUMBER;

NUMBER C[512*512];
int N;

unsigned int primeTab[] =
{      2,      3,      5,      7,     11,    13,    17,    19,    23,    29,
31,     37,     41,     43,     47,    53,    59,    61,    67,    71,
73,     79,     83,     89,     97,   101,   103,   107,   109,   113,
127,    131,    137,    139,    149,   151,   157,   163,   167,   173,
179,    181,    191,    193,    197,   199,   211,   223,   227,   229,
233,    239,    241,    251,    257,   263,   269,   271,   277,   281,
283,    293,    307,    311,    313,   317,   331,   337,   347,   349,
353,    359,    367,    373,    379,   383,   389,   397,   401,   409,
419,    421,    431,    433,    439,   443,   449,   457,   461,   463,
467,    479,    487,    491,    499,   503};

#define MODULO 100003
typedef LIST<int> PRIMES;
typedef MAP<int, PRIMES> PRIME_NUMBER;
PRIME_NUMBER mPrimes;

typedef MAP<int, int> CANONICAL;

PRIMES& GETPRIMES(int number)
{
	PRIMES& Res = mPrimes[number];
	if (Res.empty())
	{
		unsigned int* Prime=primeTab;
		while (number!=1)
		{
			while (number % (*Prime)) ++Prime;
			number /= *Prime;
			Res.push_back(*Prime);
		}
	}
	return Res;
}

NUMBER COMB(int n, int k)
{
	CANONICAL mCann;
	for (NUMBER i=n-k+1; i<=n; ++i)
	{
		PRIMES& Primes = GETPRIMES(i);
		foreach(PRIMES, Primes, it)
		{
			++mCann[*it];
		}
// 		X *= i;
// 		res *= i;
	}
	for (NUMBER i=2; i<=k; ++i)
	{
		PRIMES& Primes = GETPRIMES(i);
		foreach(PRIMES, Primes, it)
		{
			--mCann[*it];
		}
	}
	NUMBER res=1;
	foreach(CANONICAL, mCann, it)
	{
		for(int i=0; i<it->second; ++i)
		res=(res*it->first)%MODULO;
	}
	return res;
}

NUMBER GETC(int n, int k)
{
	if (k==0)
		return 1;

	if (n<=2)
		return 0;

	if (k>n-2)
		return 0;

	NUMBER* Value = C+n*512+k;
	if ((*Value)!=~(NUMBER()))
		return *Value;
	if (k==1)
		*Value=(n-1)/2;
	else
	{
		*Value=0;
		for (int i=0; i<=k; ++i)
		{
			*Value=((*Value)+GETC(n-1-k, k-i)*COMB(k, i))%MODULO;
		}
	}
	//printf("C%d,%d=%d\n", n, k, *Value);
	return *Value;
}

void ProcessFile(FILE* fin)
{
	memset(C, 0xFF, 512*512*sizeof(NUMBER));
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		fscanf(fin, "%d", &N);
 		NUMBER res=0;
 		for (int i=0;i<=N-2;++i)
 			res=(res+GETC(N, i))%MODULO;
 		fprintf(FILE_OUT, "Case #%d: %d\n", i+1, res);
	}
}

///////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	char fileName[256];
	printf ("Which file: ");
	fgets ( fileName, 256, stdin );
	if (fileName[0]>13)
	{
		int i = atoi (fileName);
		FILE_FROM = FILE_TO = i;
	}
	for (int file_from=FILE_FROM; file_from<=FILE_TO; ++file_from)
	{
		sprintf(fileName, FILENAME, file_from);
		FILE *fin = fopen(fileName, "r");
		if (!fin)
		{
			printf("!!! CANNOT INF FILE %s", fileName);
			continue;
		} else {
			printf("Processing file: %s ...\n", fileName);
		}
		if (OUT_FILE)
		{
			char fileNameOut[256];
			sprintf(fileNameOut, "%s.out", fileName);
			FILE_OUT = fopen(fileNameOut, "w");
		} else
		{
			FILE_OUT = stdout;
		}
		ProcessFile(fin);
		fclose(fin);
		if (OUT_FILE)
			fclose(FILE_OUT);
	}
	printf("\nREADY!!!\n");
	getc(stdin);
	return 0;
}
