#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>

/*
Google Code Jam 2001 

online round 1b, subround c

gopher@geomys.com


solved using MSVC++ Express 2008

add to empty console project to compile


*/

using namespace std;

#define BASENAME "A-large"

//this function checks if x,y represents a corner of the blue space;
//if it does, a tile is 
bool TryForcedRed(vector<char*>& tiles, int cols, int x, int y)
{
	//first, is this a corner?
	if (tiles[y][x]!='#')
		return false;

	int adjacent=0;
	int bits=0;

	if (x>0 && tiles[y][x-1]=='#')
	{
		adjacent++;
		bits|=1;
	}
	if (x<cols-1 && tiles[y][x+1]=='#')
	{
		adjacent++;
		bits|=2;
	}

	if (y>0 && tiles[y-1][x]=='#')
	{
		adjacent++;
		bits|=4;
	}
	if (y<(int)tiles.size()-1 && tiles[y+1][x]=='#')
	{
		adjacent++;
		bits|=8;
	}

	if (adjacent<2)
		throw "impossible.";

	if (adjacent==2)
	{
		//it's a corner.
		switch(bits)
		{
		case 0x3: //right and left; impossible
		case 0xc: //up and down; impossible
			throw "impossible.";


		case 0x5: //left and up
			if (tiles[y-1][x-1]!='#')
				throw "impossible.";
			tiles[y][x]='/';
			tiles[y][x-1]='\\';
			tiles[y-1][x]='\\';
			tiles[y-1][x-1]='/';
			break;

		case 0x9: //left and down
			if (tiles[y+1][x-1]!='#')
				throw "impossible.";
			tiles[y][x]='\\';
			tiles[y][x-1]='/';
			tiles[y+1][x]='/';
			tiles[y+1][x-1]='\\';
			break;
		case 0x6: //right and up
			if (tiles[y-1][x+1]!='#')
				throw "impossible.";
			tiles[y][x]='\\';
			tiles[y][x+1]='/';
			tiles[y-1][x]='/';
			tiles[y-1][x+1]='\\';
			break;
		case 0xa: //right and down
			if (tiles[y+1][x+1]!='#')
				throw "impossible.";
			tiles[y][x]='/';
			tiles[y][x+1]='\\';
			tiles[y+1][x]='\\';
			tiles[y+1][x+1]='/';
			break;
		}
		return true;
	}
	return false;
}

int main(int argc, char* argv[])
{
	
	
	ifstream inFile(BASENAME ".in");
	ofstream outFile(BASENAME ".out");

	int numCases=0;
	inFile>>numCases;


		
	for (int caseNum=1; caseNum<=numCases; ++caseNum)
	{
		int rows, cols;
		char crap[1];

		inFile>>rows>>cols;
		//burn the return
		inFile.getline(crap,1);

		vector<char*> tiles(rows);
		
		for (int i=0; i<rows; ++i)
		{						
			tiles[i]=new char[cols+1];
			inFile.getline(tiles[i],cols+1);
		}
		
		bool impossible=false;
		try {
			int skipped;
			do {
				skipped=0;
				//find a forced corner.
				for (int y=0; y<rows; ++y)
				{
					for (int x=0; x<cols; ++x)
					{
						if (tiles[y][x]=='#')	
						{
							if (!TryForcedRed(tiles,cols,x,y))
								skipped++;
						}
					}
				}
			} while(skipped!=0);
		}
		catch(const char* impStr)
		{
			impossible=true;
		}


		outFile<<"Case #"<<caseNum<<":"<<endl;
		
		if (impossible)
		{
			outFile<<"Impossible"<<endl;
		}
		else
		{
			for (int i=0; i<rows; ++i)
			{
				outFile<<tiles[i]<<endl;
			}
		}
		
	}

	/*comment terminator*/

	return 0;
}