#include <iostream>

using namespace std;

#define MAXSIZE 20
#define NO_SHED '%'

struct Cell { int alt; char shed; };

Cell map [MAXSIZE][MAXSIZE];
int mapHeight, mapWidth;

bool isSink (int y, int x)
{
	return (
		(y < 1 || map[y-1][x].alt >= map[y][x].alt)
		&& (y > mapHeight - 2 || map[y+1][x].alt >= map[y][x].alt)
		&& (x < 1 || map[y][x-1].alt >= map[y][x].alt)
		&& (x > mapWidth - 2 || map[y][x+1].alt >= map[y][x].alt)
	);
}

void findDrain (int y, int x, int &newY, int &newX)
{
	newY = y;
	newX = x;
	
	if (y > 0
		&& (x < 1 || map[y-1][x].alt <= map[y][x-1].alt) // as low as west
		&& (x > mapWidth - 2 || map[y-1][x].alt <= map[y][x+1].alt) // and east
		&& (y > mapHeight - 2 || map[y-1][x].alt <= map[y+1][x].alt) // and south
	)
	// flow north
	{
		newY = y-1;
		return;
	}
		
	else if (x > 0
		&& (x > mapWidth - 2 || map[y][x-1].alt <= map[y][x+1].alt) // and east
		&& (y > mapHeight - 2 || map[y][x-1].alt <= map[y+1][x].alt) // and south
	)
	// flow west
	{
		newX = x - 1;
		return;
	}
		
	else if (x < mapWidth - 1		 
		&& (y > mapHeight - 2 || map[y][x+1].alt <= map[y+1][x].alt) // and south
	)
	// flow east
	{
		newX = x+1;
		return;
	}
		
	else if (y < mapHeight - 1)
	// flow south
	{
		newY = y+1;
		return;
	}
	
	cerr << "No suitable drain found for y=" << y << ", x=" << x << endl;
	throw 42;
}

void markShed(int y, int x, char & name)
{
	if (map[y][x].shed != NO_SHED)
		name = map[y][x].shed;
	if (!isSink(y,x))
	{
		int newX, newY;
		findDrain (y, x, newY, newX);
		markShed(newY, newX, name);
	}
	map[y][x].shed = name;
}

int main ()
{
	int numberMaps;
	cin >> numberMaps;
	
	for (int mapnum=0; mapnum < numberMaps; ++mapnum)
	{
		
		char currentShed = 'a';

		// Load map
		cin >> mapHeight >> mapWidth;
		for (int y = 0; y < mapHeight; ++y)
		{
			for (int x = 0; x < mapWidth; ++x)
			{
				cin >> map[y][x].alt;
				map[y][x].shed = NO_SHED;
			}
		}
		

		for (int y = 0; y < mapHeight; ++y)
		{
			for (int x = 0; x < mapWidth; ++x)
			{
				if (map[y][x].shed == NO_SHED)
				{
					markShed (y, x, currentShed);
					++currentShed;
				}
			}
		}

		
		// Print map
		cout << "Case #" << mapnum+1 << ": \n";
		for (int y = 0; y < mapHeight; ++y)
		{
			for (int x = 0; x < mapWidth; ++x)
			{
				cout << map[y][x].shed << ' ';
			}
			cout << endl;
		}
	}
	
	
	
	return 0;
}