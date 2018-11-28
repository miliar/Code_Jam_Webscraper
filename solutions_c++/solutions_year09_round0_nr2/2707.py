// TestProject.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>

using namespace std;

#include <boost/lexical_cast.hpp>

using namespace boost;

typedef unsigned long long uint64;
typedef long long int64;

struct locdata
{
	uint64 _alt;
	char   _ch;
	locdata(uint64 alt=0)
		:_alt(alt),
		 _ch(0)
	{
	}
};

enum Direction
{
	NORTH = 0,
	WEST,
	EAST,
	SOUTH
};

struct posdata
{
	locdata & _loc;
	Direction _dir;
	posdata (locdata &loc, Direction dir)
		:_loc(loc),
		 _dir(dir)
	{
	}

	bool operator < (const posdata &rhs) const
	{
		if (rhs._loc._alt == _loc._alt)
			return _dir < rhs._dir;

		return _loc._alt < rhs._loc._alt;
	}
};

unsigned int getpos(unsigned int j, unsigned k, unsigned int W)
{
	unsigned int pos = (j*W + k);
	return pos;
}

int _tmain(int argc, _TCHAR* argv[])
{
	vector<string> svec;
	ifstream ifile(argv[1]);
	ofstream ofile(argv[2]);
	copy(istream_iterator<string>(ifile),
		istream_iterator<string>(),
		back_inserter(svec));
	unsigned int index = 0;
	const uint64 N = lexical_cast<uint64>(svec[index++]);
	for (uint64 i = 0;
		 i < N;
		 ++i)
	{
		const unsigned int H = lexical_cast<unsigned int>(svec[index++]);
		const unsigned int W = lexical_cast<unsigned int>(svec[index++]);
		locdata * mapdata = new locdata[H*W];
		for (unsigned int j = 0;
			 j < H;
			 ++j)
		{
			for (unsigned int k = 0;
				 k < W;
				 ++k)
			{
				mapdata[getpos(j,k,W)] = locdata(lexical_cast<uint64>(svec[index++]));
			}
		}
		char global = 'a';
		for (unsigned int j = 0;
			 j < H;
			 ++j)
		{
			for (unsigned int k = 0;
				 k < W;
				 ++k)
			{
				const uint64 myalt  = mapdata[getpos(j,k,W)]._alt;
				set<posdata> cells;

				if ( j > 0 &&
					mapdata[getpos(j-1,k,W)]._alt < myalt)
				{
					cells.insert(posdata(mapdata[getpos(j-1,k,W)], NORTH));
				}
				if ( j < (H-1) &&
					mapdata[getpos(j+1,k,W)]._alt < myalt)
				{
					cells.insert(posdata(mapdata[getpos(j+1,k,W)], SOUTH));
				}

				if ( k > 0 &&
					mapdata[getpos(j,k-1,W)]._alt < myalt)
				{
					cells.insert(posdata(mapdata[getpos(j,k-1,W)], WEST));
				}
				if ( k < (W-1) &&
					mapdata[getpos(j,k+1,W)]._alt < myalt)
				{
					cells.insert(posdata(mapdata[getpos(j,k+1,W)], EAST));
				}

				if (cells.empty())
				{
					if (0 == mapdata[getpos(j,k,W)]._ch)
					{
						mapdata[getpos(j,k,W)]._ch = global++;
					}
					continue;
				}
				else if (0 == cells.begin()->_loc._ch)
				{
					if (0 == mapdata[getpos(j,k,W)]._ch)
					{
						mapdata[getpos(j,k,W)]._ch = global;
						cells.begin()->_loc._ch = global++;
					}
					else
					{
						cells.begin()->_loc._ch = mapdata[getpos(j,k,W)]._ch;
					}
					continue;
				}
				else if (0 == mapdata[getpos(j,k,W)]._ch)
				{
					mapdata[getpos(j,k,W)]._ch = cells.begin()->_loc._ch;
				}
				else if (mapdata[getpos(j,k,W)]._ch != cells.begin()->_loc._ch)
				{
					const char erasech   = (mapdata[getpos(j,k,W)]._ch > cells.begin()->_loc._ch)?
										   mapdata[getpos(j,k,W)]._ch : cells.begin()->_loc._ch;
					const char replacech = (mapdata[getpos(j,k,W)]._ch > cells.begin()->_loc._ch)?
											cells.begin()->_loc._ch:mapdata[getpos(j,k,W)]._ch;

					for (unsigned int h = 0;
						 h < H;
						 ++h)
					{
						for (unsigned int w = 0;
							 w < W;
							 ++w)
						{
							char ch = mapdata[getpos(h,w,W)]._ch;
							if (0 == ch || ch < erasech)
							{
								continue;
							}
							if (erasech == ch)
							{
								mapdata[getpos(h,w,W)]._ch = replacech;
							}
							else
							{
								mapdata[getpos(h,w,W)]._ch--;
							}
						}
					}
					global--;

				}
			}
		}
		ofile << "Case #" << i+1 << ": " << endl;
		for (unsigned int j = 0;
			 j < H;
			 ++j)
		{
			for (unsigned int k = 0;
				 k < W;
				 ++k)
			{
				ofile <<  mapdata[getpos(j,k,W)]._ch << " ";
			}
			ofile << endl;
		}


	}
}


