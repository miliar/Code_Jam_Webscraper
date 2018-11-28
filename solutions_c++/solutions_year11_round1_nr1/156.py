///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="A%d.in";
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

void ProcessFile(FILE* fin)
{
	int C;
	fscanf(fin, "%d", &C);
	for (int i=0; i<C; ++i)
	{
		__int64 N, PD, PG;
		bool bPossible=true;
		fscanf(fin, "%llu %llu %llu", &N, &PD, &PG);
		int canon[]={2, 2, 5, 5};
		int DD=1, DG=1;
		for (int i=0; i<4; ++i)
		{
			if (((PD/DD)%canon[i])==0)
				DD*=canon[i];
			if (((PG/DG)%canon[i])==0)
				DG*=canon[i];
		}
		bPossible=(100/DD<=N);
		if (PG==0 && PD>0)
			bPossible=false;
		if (PG==100 && PD!=100)
			bPossible=false;
		fprintf(FILE_OUT, "Case #%d: %s\n", i+1, bPossible ? "Possible" : "Broken");
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
