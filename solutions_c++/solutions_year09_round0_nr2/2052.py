#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

char* NextElement( unsigned X,
				  unsigned Y,
				  unsigned Height,
				  unsigned Width,
				  unsigned**map,
				  char** charMap,
				  unsigned& retX, unsigned& retY )
{
	unsigned smallestAttitude(map[Y][X]);
	retX = X;
	retY = Y;
	if(Y >= 1)
		if( map[Y-1][X] < smallestAttitude )
		{
			smallestAttitude = map[Y-1][X];
			retX = X;
			retY = Y - 1;
		}
	if( X >= 1)
		if(map[Y][X-1] < smallestAttitude )
		{
			smallestAttitude = map[Y][X-1];
			retX = X-1;
			retY = Y;
		}
	if( X + 1 < Width )
		if(map[Y][X+1] < smallestAttitude)
		{
			smallestAttitude = map[Y][X+1];
			retX = X+1;
			retY = Y;
		}
	if (Y + 1 < Height)
		if(map[Y+1][X] < smallestAttitude)
		{
			retX = X;
			retY = Y+1;
		}
	if (X == retX)
		if(Y == retY)
		{
			return 0;
		}
	return &charMap[retY][retX];
}

void SolveTask( const char* inputFileName, const char* outputFileName )
{
	std::ifstream inFile( inputFileName );
	std::ofstream oFile( outputFileName );

	unsigned T(0);
	inFile >> T;
	for (unsigned i = 0; i < T; i++)
	{
		unsigned Height(0);
		inFile >> Height;
		unsigned Width(0);
		inFile >> Width;
		unsigned** data = new unsigned*[Height];
		char** pOut = new char*[Height];
		for( unsigned j = 0; j < Height; j++ )
		{
			data[j] = new unsigned[Width];
			pOut[j] = new char[Width];
			for( unsigned k = 0; k < Width; k++ )
			{
				inFile >> data[j][k];
				pOut[j][k] = 0;
			}
		}
		char resIfNew = 'a';
		std::list<char*> stack;

		for( unsigned j = 0; j < Height; j++ )
		{
			for( unsigned k = 0; k < Width; k++ )
			{
				if( pOut[j][k] )
					continue;
				unsigned curX(k);
				unsigned curY(j);
				stack.push_back(&pOut[j][k]);
				char* nextChar = NextElement(k, j, Height, Width, data, pOut, curX, curY);
				while( nextChar )
				{
					if(*nextChar)
						break;
					stack.push_back(nextChar);
					nextChar = NextElement( curX, curY, Height, Width, data, pOut, 
						curX, curY );
				}
				if(nextChar)
				{
					for( std::list<char*>::iterator it = stack.begin(); it != 
						stack.end(); it++)
					{
						(*(*it)) = (*nextChar);
					}
				}
				else
				{
					for( std::list<char*>::iterator it = stack.begin(); it != 
						stack.end(); it++)
					{
						(*(*it)) = resIfNew;
					}
					resIfNew++;
				}
				stack.clear();
			}
		}
		oFile << "Case #" << (i+1) << ":" << std::endl;
		for( unsigned j = 0; j < Height; j++ )
		{
			for( unsigned k = 0; k < Width; k++)
			{
				oFile << pOut[j][k];
				if( k+1 < Width)
					oFile << " ";
				else
					oFile << std::endl; 
			}
		}
		for( unsigned j = 0; j < Height; j++ )
		{
			delete []data[j];
			delete []pOut[j];
		}
		delete []data;
		delete []pOut;
	}
}

void main()
{
 SolveTask( "d:/1.txt", "d:/2.txt");
}