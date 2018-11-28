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

void ProcessFile(FILE* fin)
{
	int C;
	fscanf(fin, "%d", &C);
	for (int i=0; i<C; ++i)
	{
		typedef VECTOR<char> CHARS;
		CHARS Chars;
		typedef PAIR<char, char> CHARPAIR;
		typedef MAP<CHARPAIR, char> CHARMAP;
		CHARMAP Opposes;
		CHARMAP Combines;

		int c;
		fscanf(fin, "%d ", &c);
		for(int j=0; j<c; ++j)
		{
			char c0,c1,c2;
			fscanf(fin, "%c%c%c", &c0, &c1, &c2);
			Combines[CHARPAIR(c0,c1)]=c2;
			Combines[CHARPAIR(c1,c0)]=c2;
		}

		fscanf(fin, "%d ", &c);
		for(int j=0; j<c; ++j)
		{
			char c0,c1;
			fscanf(fin, "%c%c", &c0, &c1);
			Opposes[CHARPAIR(c0,c1)]=1;
			Opposes[CHARPAIR(c1,c0)]=1;
		}

		fscanf(fin, "%d ", &c);
		for(int j=0; j<c; ++j)
		{
			char c0;
			fscanf(fin, "%c", &c0);
			Chars.push_back(c0);
			if (Chars.size()>=2)
			{
				CHARMAP::iterator it = Combines.find(CHARPAIR(Chars[Chars.size()-1], Chars[Chars.size()-2]));
				if (it != Combines.end())
				{
					Chars[Chars.size()-2]=it->second;
					Chars.pop_back();
				} else
				{
					bool bOppose=false;
					foreach(CHARS, Chars, itChar)
					{
						for (CHARS::iterator it = Chars.begin(); it != itChar; ++it)
						{
							if (Opposes.find(CHARPAIR(*it, *itChar))!=Opposes.end())
							{
								bOppose=true;
								Chars.clear();
								break;
							}
						}
						if (bOppose)
							break;
					}
				}
			}

		}

		fprintf(FILE_OUT, "Case #%d: [", i+1);
		foreach(CHARS, Chars, itChar)
		{
			if (Chars.begin() != itChar) fprintf(FILE_OUT, ", ");
			fprintf(FILE_OUT, "%c", *itChar);
		}
		fprintf(FILE_OUT, "]\n");
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
