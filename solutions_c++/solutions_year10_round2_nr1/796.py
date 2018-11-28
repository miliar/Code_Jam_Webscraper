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


///////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////

struct CHAR_CMP
{	// functor for operator<
	bool operator()( char*const& _Left,  char*const& _Right) const
	{	// apply operator< to operands
		return 0>strcmp(_Left, _Right);
	}
};

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int N, M;
		fscanf(fin, "%d %d", &N, &M);
		char path[256];
		typedef SET<char*, CHAR_CMP> DIRS;
		DIRS mDirs;
		int mkdirs=0;
		for (int n=0; n<N; ++n)
		{
			fscanf(fin, "%s", &path);
			for (char *c=path+1; ; ++c)
			{
				if ((*c)=='/' || (*c)==0)
				{
					char* SubDir = new char[c-path+1];
					memcpy(SubDir, path, c-path);
					SubDir[c-path]=0;
					mDirs.insert(SubDir);
					if ((*c)==0)
						break;
				}
			}
		}
		for (int m=0; m<M; ++m)
		{
			fscanf(fin, "%s", &path);
			for (char *c=path+1; ; ++c)
			{
				if ((*c)=='/' || (*c)==0)
				{
					char* SubDir = new char[c-path+1];
					memcpy(SubDir, path, c-path);
					SubDir[c-path]=0;
					if (mDirs.insert(SubDir).second)
						++mkdirs;
					if ((*c)==0)
						break;
				}
			}
		}
		foreach(DIRS, mDirs, itDir)
		{
			delete *itDir;
		}
		fprintf(FILE_OUT, "Case #%d: %d\n", i+1, mkdirs);
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
