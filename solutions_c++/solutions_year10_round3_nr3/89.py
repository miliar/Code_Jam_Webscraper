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

int N, M;

short* SIZES;
char* STATES;

int GetSize(int x, int y)
{
	if (STATES[y*N+x]==2)
		return 0;
	short& SIZE = SIZES[y*N+x];
	if (SIZE)
		return SIZE;
// 	if (STATES[y*N+x]==2)
// 	{
// 		SIZE=0;
// 		return SIZE;
// 	}
	
	SIZE=1;
	if (x+1<N && y+1<M && STATES[(y+1)*N+x+1]==STATES[y*N+x])
	{
		SIZE+=GetSize(x+1, y+1);
		int SIZETEST=1;
		for (int xx=x+1, flag=STATES[y*N+x]^1; xx<N && SIZETEST<SIZE && STATES[y*N+xx]==flag; ++xx, flag ^= 1, ++SIZETEST);
		if (SIZETEST<SIZE) SIZE = SIZETEST;
		SIZETEST=1;
		for (int yy=y+1, flag=STATES[y*N+x]^1; yy<M && SIZETEST<SIZE && STATES[yy*N+x]==flag; ++yy, flag ^= 1, ++SIZETEST);
		if (SIZETEST<SIZE) SIZE = SIZETEST;
	}
	return SIZE;
}

__forceinline void UpdateBoard(int X, int Y, int SX, int SY)
{
	for (int y=Y; y<Y+SY; ++y)
		memset(SIZES+y*N+X, 0, SX*sizeof(short));

/*	for (int x=X; x<X+SX; ++x)
	{
		for (int y=Y; y<Y+SY; ++y)
		{
			SIZES[y*N+x]=GetSize(x, y);
		}
	}*/
}

struct more
{	// functor for operator<
	bool operator()(const int& _Left, const int& _Right) const
	{	// apply operator< to operands
		return (_Left > _Right);
	}
};

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		fscanf(fin, "%d %d\n", &M, &N);
		SIZES = new short[N*M];
		memset(SIZES, 0, N*M*sizeof(short));
		STATES = new char[N*M];
		for (int m=0; m<M; ++m)
		{
			for (int nn=0, n=0; nn<(N+3)/4; ++nn)
			{
				char c;
				fscanf(fin, "%c", &c);
				c=(c>='0' && c<='9') ? c-'0' : c-('A'-10);
				for (int j=0; j<4 && n<N; ++j, ++n)
				{
					STATES[m*N+n]=(c>>(3-j))&1;
				}
			}
			fscanf(fin, "\n");
		}
		typedef MAP<int, int, more > CHESS;
		CHESS mChess;
		typedef PAIR<int, int> PLACE;
		//UpdateBoard(0, 0, N, M);
		int BestSizeLast=0;
		int LEFT=N*M;
		int c=0;
		PLACE BestPlace;
		while (true)
		{
			int BestSize=0;
			bool bFinish=false;
 			if (BestSizeLast)
 			{
 				if (++BestPlace.first==N)
 				{
 					BestPlace.first=0;
 					if (++BestPlace.second==M)
 						BestPlace.second=0;
 				}
 			}
 //			BestPlace.first=0;
// 			BestPlace.second=0;
 			int y=BestPlace.second;
 			int x=BestPlace.first;
 			PLACE BestPlaceLast(BestPlace);
			bool bFirst=true;
			bool bWasRound=false;
 			for (;;)
 			{
 				int Size = GetSize(x, y);
 				if (Size>BestSize || (bWasRound && Size==BestSize))
 				{
					bWasRound=false;
 					BestSize=Size;
 					BestPlace.first=x;
 					BestPlace.second=y;
 					if (BestSize==BestSizeLast)
 						break;
 				}
				if (!bFirst && x==BestPlaceLast.first && y==BestPlaceLast.second)
					break;
				bFirst=false;
 				if (++x==N)
 				{
 					x=0;
 					if (++y==M)
 					{
 						y=0;
 						--BestSizeLast;
						bWasRound=true;
 					}
 				}
 			}
//  			for (int y=0; !bFinish && y<M; ++y)
//  			{
//  				for (int x=0; !bFinish && x<N; ++x)
//  				{
//  					int Size = GetSize(x, y);
//  					if (Size>BestSize)
//  					{
//  						BestSize=Size;
//  						BestPlace.first=x;
//  						BestPlace.second=y;
//   						if (BestSize==BestSizeLast)
//   							bFinish=true;
//  					}
//  				}
//  			}
			if (BestSize==0)
				break;
			LEFT -= BestSize;
			if (((++c)%100)==0)
				printf("Left: %d\n", LEFT);
			++mChess[BestSize];
			for (int y=BestPlace.second; y<BestPlace.second+BestSize; ++y)
				memset(STATES+y*N+BestPlace.first, 2, BestSize);
			int UX = max(0, BestPlace.first-BestSize+1);
			int UY = max(0, BestPlace.second-BestSize+1);
			
  			for (int y=UY; y<BestPlace.second; ++y)
  			{
  				for (int x=UX; x<BestPlace.first+BestSize; ++x)
  				{
 // 					if (y>=BestPlace.second && x>=BestPlace.first)
 // 						continue;
  					short& SIZE = SIZES[y*N+x];
  					if (x+SIZE>BestPlace.first && y+SIZE>BestPlace.second)
  						SIZE=0;
  				}
  			}
  			for (int y=BestPlace.second; y<BestPlace.second+BestSize; ++y)
  			{
  				for (int x=UX; x<BestPlace.first; ++x)
  				{
  					short& SIZE = SIZES[y*N+x];
  					if (x+SIZE>BestPlace.first && y+SIZE>BestPlace.second)
  						SIZE=0;
  				}
  			}

			BestSizeLast = BestSize;

			//UpdateBoard(UX, UY, BestPlace.first+BestSize-UX, BestPlace.second+BestSize-UY);

		}

		delete []SIZES;
		delete []STATES;
		fprintf(FILE_OUT, "Case #%d: %d\n", i+1, mChess.size());
		foreach (CHESS, mChess, itChess)
		{
			fprintf(FILE_OUT, "%d %d\n", itChess->first, itChess->second);
		}
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
