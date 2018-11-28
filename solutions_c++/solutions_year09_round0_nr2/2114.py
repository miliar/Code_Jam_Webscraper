#include "stdafx.h"
#include <stdio.h>
#include <vector>
using std::vector;
#include <algorithm>
#include <numeric>
#include <fstream>
#include <cmath>
using namespace std;

struct cell
{
	cell():labeled(false),sink(false){}
	int x, y;
	char label;
	bool labeled;
	int altitude;
	bool sink;
};

int min_f(int x, int y)
{
	return x < y? x:y;
}

void FindSolution(cell * map, int row, int col)
{
	vector<cell> cells;

	char curr_sink = 'a';
	char label = 'z';

	for (int i = 0; i < row; ++i)
	{
		for (int j = 0; j < col; ++j)
		{
			cells.clear();

			if (!map[i*col + j].labeled)
			{
				bool bSinkFound = false;

				int x = i;
				int y = j;

				while (!bSinkFound)
				{
					if (map[x*col + y].labeled)
					{
						label = map[x*col + y].label;
						break;
					}
					
					cell cl;
					cl.x = x;
					cl.y = y;
					cells.push_back(cl);
										
					int north = map[x*col + y].altitude + 1;
					int south = map[x*col + y].altitude + 1;
					int west = map[x*col + y].altitude + 1;
					int east = map[x*col + y].altitude + 1;

					if (x > 0) north = map[(x-1)*col +y].altitude;
					if (x < row - 1) south = map[(x+1)*col +y].altitude;
					if (y > 0) west = map[x*col + y-1].altitude;
					if (y < col - 1) east = map[x*col + y + 1].altitude;

					int min_ = min_f(min_f(north,south),min_f(west,east));

					if (min_ > map[x*col + y].altitude)
					{
						// it's sink!
						map[x*col + y].sink = true;
						label = curr_sink++;
						bSinkFound = true;
						break;
					}
					else if (min_ == map[x*col + y].altitude)
					{
		/*				if (north == min_)
						{
							x = x - 1;							
							continue;
						}
						
						if (west == min_)
						{
							y = y - 1;
							continue;
						}*/

						// it's sink!
						map[x*col + y].sink = true;
						label = curr_sink++;						
						bSinkFound = true;
						break;
					}
					else
					{
						// min < altitude
						if (north == min_)
						{
							x = x - 1;							
							continue;
						}

						if (west == min_)
						{
							y = y - 1;
							continue;
						}
						
						if (east == min_)
						{
							y = y + 1;
							continue;
						}

						if (south == min_)
						{
							x = x + 1;
							continue;
						}
					}
				}

				for (int l = 0; l < cells.size(); ++l)
				{
					int x = cells[l].x;
					int y = cells[l].y;

					map[x*col + y].label = label;
					map[x*col + y].labeled = true;
				}


			}
		}
	}
}



int _tmain(int argc, _TCHAR* argv[])
{
	fstream fIn("d:\\Projects\\code jam\\2009\\B-large.in");
	fstream fOut;
	fOut.open("d:\\Projects\\code jam\\2009\\B-large.res", ios_base::out);

	int mapsNumber = 0;
	fIn >> mapsNumber;
	
	for (int i = 0; i < mapsNumber; ++i)
	{
		int row, col;
		fIn >> row;
		fIn >> col;

		cell * map = new cell [row * col];
		//char * labelmap = new char [row * col];

		for (int j = 0; j < row; ++j)
		{
			for (int k = 0; k < col; ++k)
			{
				fIn >> map [j* col + k].altitude;
			}
		}

		FindSolution(map, /*labelmap,*/ row, col);

		fOut << "Case #" << i+1 <<":\n";
		
		for (int j = 0; j < row; ++j)
		{
			for (int k = 0; k < col; ++k)
			{
				fOut << map [j* col + k].label;
				if (k < col - 1)
					fOut << " ";
			}
			fOut << "\n";
		}


		delete [] map;
		//delete [] labelmap;
	}


	//double test = 1438010552.3278773255045661463992;


	//double s = log10(3.0 + sqrt(5.0));
	//for(unsigned int i = 1; i <= testNumber; ++i)
	//{
	//	__int64 n;
	//	fIn >> n;

	//	double p = s; 
	//	p *= n;

	//	unsigned int digits = floor(p)*3;
	//	//double p = fmod(q, 3.0);
	//	//p = pow(10.0, p);
	//	//p = floor(p);
	//	p = pow(10.0, fmod(p, 3.0));

	//	for (unsigned int j =0; j < digits; ++j)
	//	{
	//		p*=10;
	//	}

	//	fOut << "Case #" << i <<": ";
	//	fOut << int(floor(fmod(p,1000)/100.0));
	//	fOut << int(floor(fmod(p,100)/10.0));
	//	fOut << int(floor(fmod(p,10)));
	//	fOut << "\n";

	//}


	return 0;
}
