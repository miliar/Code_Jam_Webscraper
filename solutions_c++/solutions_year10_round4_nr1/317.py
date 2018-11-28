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

class MATRIX : public VECTOR<char>
{
public:
	MATRIX(int k)
	{
		n=k;
		resize(n*n);
// 		for (int i=0; i<n*n; ++i)
// 			operator[](i)=rand();
	}
	char& Get(int line, int c)
	{
		int x, y;
		if (line<n)
		{
			y = c;
			x = n-1-line+c;
		} else
		{
			y = line-n+1+c;
			x = c;
		}
		return operator[](y*n+x);
	}
	bool IsSimmetric(int k, int xp, int yp)
	{
		for (int y=0; y<n; ++y)
		{
			for (int x=0; x<n; ++x)
			{
				char c = operator[](y*n+x);
				int mx = x+xp;
				int my = y+yp;

				int sx1 = my-xp;
				int sy1 = mx-yp;

				if (sx1>=0 && sx1<n && sy1>=0 && sy1<n && c != operator[](sy1*n+sx1))
					return false;

				int sx2 = k-1-my-xp;
				int sy2 = k-1-mx-yp;

				if (sx2>=0 && sx2<n && sy2>=0 && sy2<n && c != operator[](sy2*n+sx2))
					return false;
			}
		}
		return true;
	}
	int GetClass()
	{
		int t=0;
		for (t=0;; ++t)
		{
			for (int x=0; x<=t; ++x)
				for (int y=0; y<=t; ++y)
					if (IsSimmetric(n+t, x, y))
						return t;
		}
		return 0;
	}
	int n;
};

///////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int k;
		fscanf(fin, "%d", &k);
		MATRIX m(k);
		for (int line=0; line<2*k-1; ++line)
		{
			for (int c=0; c<(line<k ? line+1 : 2*k-1-line ); ++c)
			{
				int cc;
				fscanf(fin, "%d", &cc);
				m.Get(line, c)=cc;
			}
		}
		int t=m.GetClass();
		fprintf(FILE_OUT, "Case #%d: %d\n", i+1, (k+t)*(k+t)-k*k );
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
