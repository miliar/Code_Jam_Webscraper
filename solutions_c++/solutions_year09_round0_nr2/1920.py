#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>

using namespace std;

#define MAX_WIDTH 100
#define MAX_HIGHT 100

map<char, char> dis_map;
char dis_tag = 'a';

enum DIRECT
{
	North = 0,
	West,
	East,
	South,
	NoDIR
};

typedef struct mapNode
{
	int alt;
	DIRECT dir;
	char id;
	mapNode():
	alt(0),
	dir(NoDIR),
	id('\0')
	{}
}MapNode;

MapNode dimap[MAX_HIGHT][MAX_WIDTH];

char tag = 'a';

char followNode(int h, int w);

void process(int iHight, int iWidth)
{
	for(int h = 0; h < iHight; ++h)
	{
		for(int w = 0; w < iWidth; ++w)
		{
			int lowest = dimap[h][w].alt;
			DIRECT lowdir = NoDIR;

			if (h + 1 < iHight && dimap[h+1][w].alt < dimap[h][w].alt)
			{
//				cout << endl << "h:" << h << " hight:" << iHight << endl;
				lowest = dimap[h+1][w].alt;
				lowdir = South;
			}
			if (w + 1 < iWidth && 
					dimap[h][w+1].alt <= lowest &&
					dimap[h][w+1].alt < dimap[h][w].alt)
			{
				lowest = dimap[h][w+1].alt;
				lowdir = East;
			}
			if (w -1 >= 0 &&
					dimap[h][w-1].alt <= lowest &&
					dimap[h][w-1].alt < dimap[h][w].alt)
			{
				lowest = dimap[h][w-1].alt;
				lowdir = West;
			}
			if (h -1 >= 0 &&
					dimap[h-1][w].alt <= lowest &&
					dimap[h-1][w].alt < dimap[h][w].alt)
			{
				lowest = dimap[h-1][w].alt;
				lowdir = North;
			}

			if (lowdir == NoDIR)
			{
				dimap[h][w].id = tag++;
//				cout << endl << "h:" << h << " w:" << w << " id:" << dimap[h][w].id << endl;
			}
			dimap[h][w].dir = lowdir;
		}			
	}// high

	for(int h = 0; h < iHight; ++h)
	{
		for(int w = 0; w < iWidth; ++w)
		{
			if (dimap[h][w].dir != NoDIR)
			{
				if (dimap[h][w].id != '\0')
					continue;
				else
				{
					followNode(h, w);
				}
			}
		}// width		
	}// high
}

char followNode(int h, int w)
{
	if (dimap[h][w].dir == South)
	{
		dimap[h][w].id = followNode(h+1, w);
		return dimap[h][w].id;
	}
	else if(dimap[h][w].dir == East)
	{
		dimap[h][w].id = followNode(h, w + 1);
		return dimap[h][w].id;
	}
	else if(dimap[h][w].dir == West)
	{
		dimap[h][w].id = followNode(h, w - 1);
		return dimap[h][w].id;
	}
	else if(dimap[h][w].dir == North)
	{
		dimap[h][w].id = followNode(h-1, w);
		return dimap[h][w].id;
	}
	else
	{
		return dimap[h][w].id;
	}
}

void clean()
{
	for(int h = 0; h < MAX_HIGHT; ++h)
	{
		for(int w = 0; w < MAX_WIDTH; ++w)
		{
			dimap[h][w].dir = NoDIR;
			dimap[h][w].alt = 0;
			dimap[h][w].id = '\0';
		}// width		
	}// high

	dis_map.clear();
	tag = 'a';
	dis_tag = 'a';
}

void output(int iHight,int iWidth)
{
	for(int h = 0; h < iHight; ++h)
	{
		for(int w = 0; w < iWidth; ++w)
		{
			if (dis_map.find(dimap[h][w].id) == dis_map.end())
			{
				dis_map[dimap[h][w].id] = dis_tag++;
			}

			if (w == MAX_WIDTH-1)
			{
				cout << dis_map[dimap[h][w].id];
			}
			else
				cout << dis_map[dimap[h][w].id] << " ";
		}// width
		cout << endl;		
	}// high
}

void outputMap(int iHight,int iWidth)
{
	for(int h = 0; h < iHight; ++h)
	{
		for(int w = 0; w < iWidth; ++w)
		{
			if (w == MAX_WIDTH-1)
			{
				cout << dimap[h][w].alt;
			}
			else
				cout << dimap[h][w].alt << " ";
		}// width
		cout << endl;		
	}// high
}

void outputDir(int iHight,int iWidth)
{
	for(int h = 0; h < iHight; ++h)
	{
		for(int w = 0; w < iWidth; ++w)
		{
			if (w == MAX_WIDTH-1)
			{
				cout << dimap[h][w].dir;
			}
			else
				cout << dimap[h][w].dir << " ";
		}// width
		cout << endl;		
	}// high
}

int main()
{
	ifstream inputFile;
	inputFile.open("B-large.in");
	

	int iMapNum = 0;
	inputFile >> iMapNum;
//	cout << iMapNum;
	for (int i = 0; i < iMapNum; ++i)
	{
		int iHight = 0, iWidth = 0;
		inputFile >> iHight;
		inputFile >> iWidth;
		
		for(int h = 0; h < iHight; ++h)
		{
			for(int w = 0; w < iWidth; ++w)
			{
				inputFile >> dimap[h][w].alt;
			}			
		}// high
		process(iHight, iWidth);
		cout << "Case #" << (i + 1) << ":" << endl;
//		outputMap(iHight, iWidth);
//		outputDir(iHight, iWidth);
		output(iHight, iWidth);
		clean();
	}

	return 0;
}
