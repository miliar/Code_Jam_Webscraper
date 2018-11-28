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

class MASS_STORE;
MASS_STORE* theStore=NULL;

typedef PAIR<int, int> POS_AND_SIZE;
struct MASS_AND_PLACE
{
	__forceinline MASS_AND_PLACE(int _r=0, int _c=0, int Mass=0 )
		:mMass(Mass), r(_r*Mass), c(_c*Mass)
	{}
	__forceinline void Update(const MASS_AND_PLACE& Mass)
	{
		r += Mass.r;
		c += Mass.c;
		mMass += Mass.mMass;
	}
	__forceinline bool IsOk(__int64 r2, __int64 c2 ) const
	{
		return (__int64)2*r==r2*mMass && (__int64)2*c==c2*mMass;
	}
	__int64 mMass;
	__int64 r, c;

};
class MASS_STORE
{
	typedef MAP<POS_AND_SIZE, MASS_AND_PLACE> MASS_AND_PLACE_MAP;
	MASS_AND_PLACE_MAP mMap;

public:
	MASS_STORE(int R, int C, int D)
		:	mR(R), mC(C), mD(D)
	{
		theStore=this;
		mW = new int[C*R];
	}
	~MASS_STORE()
	{
		delete []mW;
	}
	__forceinline void Set(int r, int c, int w)
	{
		mW[r*mC+c]=w;
	}
	__forceinline void Update(MASS_AND_PLACE& Mass, int r, int c)
	{
		Mass.Update(MASS_AND_PLACE(r, c, mW[r*mC+c]));
	}
	int mR, mC, mD;
	int *mW;
};

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int R, C, D;
		fscanf(fin, "%d %d %d", &R, &C, &D);
		MASS_STORE* mt = new MASS_STORE(R, C, D);
		for (int r=0; r<R; ++r)
		{
			fscanf(fin, "\n");
			for (int c=0; c<C; ++c)
			{
				char cc;
				fscanf(fin, "%c", &cc);
				mt->Set(r, c, cc-'0');
			}
		}
		int iRes=0;
		for (int r=0; r<=R-3; ++r)
		{
			for (int c=0; c<=C-3; ++c)
			{
				MASS_AND_PLACE Mass;
				mt->Update(Mass, r, c+1);
				mt->Update(Mass, r+1, c);
				mt->Update(Mass, r+1, c+1);
				mt->Update(Mass, r+1, c+2);
				mt->Update(Mass, r+2, c+1);
				for (int kmax=min(C-c, R-r), k=3; k<=kmax; ++k)
				{
					if (Mass.IsOk(2*r+k-1, 2*c+k-1))
						if (k>iRes)
						{
							iRes = k;
						}

					mt->Update(Mass, r+k-1, c);
					mt->Update(Mass, r, c+k-1);
					mt->Update(Mass, r+k-1, c+k-1);
					for (int kk=0; kk<k-1; ++kk)
					{
						mt->Update(Mass, r+k, c+kk+1);
						mt->Update(Mass, r+kk+1, c+k);
					}
				}
			}
		}
		delete mt;
		if (iRes==0)
			fprintf(FILE_OUT, "Case #%d: IMPOSSIBLE\n", i+1);
		else
			fprintf(FILE_OUT, "Case #%d: %d\n", i+1, iRes);
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
