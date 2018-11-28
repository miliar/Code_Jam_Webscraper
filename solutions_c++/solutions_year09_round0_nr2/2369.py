#include <iostream.h>
#include <fstream.h>
#include <list.h>

#define MAXLEVEL 100
#define MAXLEN 5000

int H, W, X, T;
int h, w;
int i,j;

char sLine[MAXLEN];

int elevationmap[MAXLEVEL][MAXLEVEL];
char basinmap[MAXLEVEL][MAXLEVEL];

char currentletter;

ifstream inFile;

struct position
{
	int x;
	int y;
};


position pos,lowest;

bool notfull(void)
{
	int ii,jj;
	bool retval = false;
	
	for (jj=0;jj<H;jj++)
	{
		for (ii=0;ii<W;ii++)
		{
			if ( basinmap[ii][jj] == '-' )
			{
				retval = true;
				break;
			}
		}
		if ( retval )
		{
			break;
		}
	}
	return retval;
}

void findnext(void)
{
	int ii,jj;
	bool found = false;
	
	for (jj=0;jj<H;jj++)
	{
		for (ii=0;ii<W;ii++)
		{
			if ( basinmap[ii][jj] == '-' )
			{
				pos.x = ii;
				pos.y = jj;
				found = true;
				break;
			}
		}
		if ( found )
		{
			break;
		}
	}
}

void replacebasin(char ctoreplace)
{
	int ii,jj;
	for (jj=0;jj<H;jj++)
	{
		for (ii=0;ii<W;ii++)
		{
			if ( basinmap[ii][jj] == currentletter )
			{
				basinmap[ii][jj] = ctoreplace;
			}
		}
	}
}

int main(int argc, char* argv[])
{
	
	
	if ( argc < 2 )
	{
		inFile.open("B-test.in");
	}
	else
	{
		inFile.open(argv[1]);
	}
	
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	inFile.getline(sLine,MAXLEN);
	

	for (X=0;X<T;X++)
	{
		inFile >> H;
		inFile >> W;
		inFile.getline(sLine,MAXLEN);
		
		for (h=0;h<MAXLEVEL;h++)
		{
			for (w=0;w<MAXLEVEL;w++)
			{
				elevationmap[w][h] = -1;
				basinmap[w][h] = '-';
			}
		}
		for (h=0;h<H;h++)
		{
			for (w=0;w<W;w++)
			{
				inFile >> elevationmap[w][h];
			}
			inFile.getline(sLine,MAXLEN);
		}
		
		pos.x = 0;
		pos.y = 0;
		currentletter = 'a';
		
		while ( notfull() )
		{
			findnext();
			while ( basinmap[pos.x][pos.y] == '-' )
			{
				basinmap[pos.x][pos.y] = currentletter;
				
				lowest.x = pos.x;
				lowest.y = pos.y;
				// check north
				if ( pos.y-1 >= 0 )
				{
					if ( elevationmap[pos.x][pos.y-1] < elevationmap[lowest.x][lowest.y] )
					{
						lowest.x = pos.x;
						lowest.y = pos.y-1;
					}
				}
				// check west
				if ( pos.x-1 >= 0 )
				{
					if ( elevationmap[pos.x-1][pos.y] < elevationmap[lowest.x][lowest.y] )
					{
						lowest.x = pos.x-1;
						lowest.y = pos.y;
					}
				}
				// check east
				if ( pos.x+1 < W )
				{
					if ( elevationmap[pos.x+1][pos.y] < elevationmap[lowest.x][lowest.y] )
					{
						lowest.x = pos.x+1;
						lowest.y = pos.y;
					}
				}
				// check south
				if ( pos.y+1 < H )
				{
					if ( elevationmap[pos.x][pos.y+1] < elevationmap[lowest.x][lowest.y] )
					{
						lowest.x = pos.x;
						lowest.y = pos.y+1;
					}
				}
				
				if ( ( lowest.x == pos.x ) && ( lowest.y == pos.y ) )
				{
					// no new basin point found, find new start point
					break;
				}
				else
				{
					// found new basin point - check if it already has a letter
					// and merge the two basins if that is the case
					if ( basinmap[lowest.x][lowest.y] != '-' )
					{
						replacebasin(basinmap[lowest.x][lowest.y]);
						currentletter--;
						break;
					}
				}
				pos.x = lowest.x;
				pos.y = lowest.y;
			}
			currentletter++;
		}
		
		
		
		
		
		
		
		cout << "Case #" << X+1 << ": " << endl;
		for (h=0;h<H;h++)
		{
			for (w=0;w<W;w++)
			{
				printf("%c",basinmap[w][h]);
				if ( w < W-1 )
					printf(" ");
			}
			cout << endl;
		}
	}
	
	inFile.close();
	return 0;
}