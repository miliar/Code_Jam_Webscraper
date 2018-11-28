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

bool Equal(char c, char d)
{
	if ((c!='X' && c!='O' && c!='T') || (d!='X' && d!='O' && d!='T'))
		return false;
	if (c=='T' || d=='T')
		return true;
	return c==d;
}

int CheckTable( char Table[4][4] ) 
{
	for (int y=0; y<4; ++y)
	{
		// line
		for (int x=0; Equal(Table[y][x], Table[y][x+1]); ++x)
		{
			if (x==2)
				return (Table[y][x] == 'X' || Table[y][x+1] == 'X') ? 0 : 1;
		}
		// coloumn
		for (int x=0; Equal(Table[x][y], Table[x+1][y]); ++x)
		{
			if (x==2)
				return (Table[x][y] == 'X' || Table[x+1][y] == 'X') ? 0 : 1;
		}
	}
	for (int x=0; Equal(Table[x][x], Table[x+1][x+1]); ++x)
	{
		if (x==2)
			return (Table[x][x] == 'X' || Table[x+1][x+1] == 'X') ? 0 : 1;
	}
	for (int x=0; Equal(Table[x][3-x], Table[x+1][3-(x+1)]); ++x)
	{
		if (x==2)
			return (Table[x][3-x] == 'X' || Table[x+1][3-(x+1)] == 'X') ? 0 : 1;
	}
	for (int y=0; y<4; ++y)
		for (int x=0; x<4; ++x)
			if (Table[y][x]=='.')
				return 3;
	return 2;
}

void ProcessFile(FILE* fin)
{
	const char * sResult[]={"X won", "O won", "Draw", "Game has not completed"};
	int T;
	char Buffer[8];
	char Table[4][4];
	fscanf(fin, "%d", &T);
	fgets(Buffer, 8, fin);
	for (int i=0; i<T; ++i)
	{
		for (int y=0; y<4; ++y)
		{
			fgets(Buffer, 8, fin);
			memcpy(Table[y], Buffer, 4);
		}
		fgets(Buffer, 8, fin);
		int result = CheckTable(Table);
		fprintf(FILE_OUT, "Case #%d: %s\n", i+1, sResult[result]);
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
