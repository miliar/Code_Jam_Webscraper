#include <iostream>
#include <fstream>
#include <string>

#define GET_CELL_INDEX(y, x, W) ((y)*(W)+(x))

using namespace std;

class Cell
{
private:
	short altitude;
	char basin;
public:
	Cell();
	void setAltitude(const short);
	friend class Map;
};

class Drain
{
private:
	char direction;
	short altitude;
public:
	Drain(const short alt) {direction = -1; altitude = alt;};
	const char getDirection() const;
	void setIfLowest(const short alt, const char dir);
};

class Map
{
private:
	Cell *terrain;
	char height, width;
public:
	Map(const char, const char);
	~Map();
	Cell *operator[](const char);
	void labelBasins();
	const string printBasins();
private:
	char labelCell(char, const char, const char);
};

Cell::Cell()
{
	altitude = -1;
	basin = 0;
}
void Cell::setAltitude(const short a)
{
	altitude = a;
}

const char Drain::getDirection() const
{
	return direction;
}
void Drain::setIfLowest(const short alt, const char dir)
{
	if (alt < altitude)
	{
		direction = dir;
		altitude = alt;
	}
}

Map::Map(const char H, const char W)
{
	height = H;
	width = W;
	terrain = new Cell[H*W];
}
Map::~Map()
{
	delete[] terrain;
}
Cell *Map::operator[](const char y)
{
	return terrain+(y*width);
}
char Map::labelCell(char nextchar, const char y, const char x)
{
	struct Drain drain((*this)[y][x].altitude);
	if ((*this)[y][x].basin)
		return (*this)[y][x].basin;
	if (y)
		drain.setIfLowest((*this)[y-1][x].altitude, 0);
	if (x)
		drain.setIfLowest((*this)[y][x-1].altitude, 1);
	if (x+1 < width)
		drain.setIfLowest((*this)[y][x+1].altitude, 2);
	if (y+1 < height)
		drain.setIfLowest((*this)[y+1][x].altitude, 3);
	switch (drain.getDirection())
	{
		case 0: nextchar = labelCell(nextchar, y-1, x); break;
		case 1: nextchar = labelCell(nextchar, y, x-1); break;
		case 2: nextchar = labelCell(nextchar, y, x+1); break;
		case 3: nextchar = labelCell(nextchar, y+1, x); break;
	}
	(*this)[y][x].basin = nextchar;
	return nextchar;
}
void Map::labelBasins()
{
	int x, y;
	char label = 'a';
	for (y=0; y<height; y++)
	{
		for (x=0; x<width; x++)
		{
			if (label == labelCell(label, y, x))
				label++;
		}
	}
}
const string Map::printBasins()
{
	string ret = "";
	char x, y;
	for (y=0; y<height; y++)
	{
		for (x=0; x<width; x++)
		{
			ret += (*this)[y][x].basin;
			ret += ' ';
		}
		ret += '\n';
	}
	return ret;
}

int main(const int argc, const char *const argv[])
{
	ifstream in;
	int T, H, W, i, j, k, alt;
	if (argc < 2)
		return -1;
	in.open(argv[1]);
	in >> T;
	for (i=0; i<T;)
	{
		in >> H >> W;
		Map map(H, W);
		for (j=0; j<H; j++)
		{	
			for (k=0; k<W; k++)
			{
				in >> alt;
				map[j][k].setAltitude(alt);
			}
		}
		map.labelBasins();
		cout << "Case #" << ++i << ":\n";
		cout << map.printBasins();
	}
	in.close();
	return 0;
}
