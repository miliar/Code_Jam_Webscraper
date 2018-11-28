///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="B%d.in";
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

#include "ttmath/ttmath.h"
typedef ttmath::UInt<8> bignum;

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

char* GetString(__int64 value)
{
	char buffer[4096];
	char* c=buffer;
	while (value || c==buffer)
	{
		*(c++)='0'+(value%10);
		value /= 10;
	}
	*c=0;
	--c;
	char *c2=buffer;
	for (;c2<c;++c2,--c)
	{
		char ct=*c2;
		*c2=*c;
		*c=ct;
	}
	return buffer;
}

///////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////

bignum LNKO(bignum n0, bignum n1)
{
	while (n0!=n1)
	{
		if (n1<n0)
			n0-=n1;
		else
			n1-=n0;
	}
	return n0;
}

void LNKO(bignum* n, int N)
{
	for (int i=N; ; i>>=1)
	{
		for (int j=0; j<i/2; ++j)
			n[j] = LNKO(n[j*2], n[j*2+1]);
		if (i&1)
			if (i==1)
			{
				if (N>1) n[0] = LNKO(n[0], n[1]);
				break;
			} else
			n[i/2]=n[i-1];
	}
}

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int N;
		fscanf(fin, "%d", &N);
		bignum *n=new bignum[N];
		char buffer[64];
		for (int i=0;i<N;++i)
		{
			fscanf(fin, "%s", buffer);
			n[i].FromString(buffer);
		}
		std::sort(n, n+N);
		bignum lowest=n[0];
		for (int i=0;i<N-1;++i)
		{
			n[i]=n[i+1]-n[i];
		}
		std::sort(n, n+N-1);
		--N;
		bignum* nn=n;
		for(;N && (*nn)==0;--N,++nn)
		{
			int alma=0;
		}
		LNKO(nn, N);
		bignum res=(lowest%nn[0]);
		if (res>0)
			res = nn[0]-res;
		delete []n;
		fprintf(FILE_OUT, "Case #%d: %s\n", i+1, res.ToString().c_str());
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
