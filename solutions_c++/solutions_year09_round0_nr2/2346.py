// water.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>

typedef std::vector<int> vi;
typedef std::vector<vi> vvi;


int
basins
(int H, int W, vvi& map, vvi& contour)
{
	assert(map.size() == H);
	assert(map[0].size() == W);
	assert(contour.size() == H);
	assert(contour[0].size() == W);
//mark basins as 0
//also count
	int count = 0;
for (int h=0; h<H; h++)
for (int w=0; w<W; w++)
{
	bool basin = true;
	//north
	if (( h> 0) && (map[h-1][w] < map[h][w])) basin = false;
	//west
	if (( w> 0) && (map[h][w-1] < map[h][w])) basin = false;
	//east
	if (( w<W-1) && (map[h][w+1] < map[h][w])) basin = false;
	//south
	if ( (h<H-1) && (map[h+1][w] < map[h][w])) basin = false;
	if (basin) 
	{
		count++;
		contour[h][w] = count;
	}
}
return count;
}

void
dirs(int H, int W, vvi& map, vvi& dir)
{
	assert(map.size() == H);
	assert(map[0].size() == W);
	assert(dir.size() == H);
	assert(dir[0].size() == W);

	for (int h=0; h<H; h++)
		for (int w=0; w<W; w++)
		{
			int min=10001;
		//north
			if ((h>0) && (map[h-1][w] < min))
			{
				dir[h][w] = 0;
				min = map[h-1][w];
			}
		//west
			if ((w>0) && (map[h][w-1] < min))
			{
				dir[h][w] = 1;
				min = map[h][w-1];
			}
		//east
			if ((w<W-1) && (map[h][w+1] < min)) 
			{
				dir[h][w] = 2;
				min = map[h][w+1];
			}
		//south
			if ((h<H-1) && (map[h+1][w] < min))
			{
				dir[h][w] = 3;
				min = map[h+1][w];
			}
		}
}

void
update_contour(int H, int W, vvi& contour, vvi& dir)
{
	assert(dir.size() == H);
	assert(dir[0].size() == W);
	assert(contour.size() == H);
	assert(contour[0].size() == W);

	for (int h=0; h<H; h++)
		for (int w=0; w<W; w++)
		{
		if (contour[h][w] == -1)
		{
			int dir_c;
		switch (dir[h][w])
		{
			case
			0: dir_c = contour[h-1][w]; break;
				case
			1: dir_c = contour[h][w-1]; break;
					case
			2: dir_c = contour[h][w+1]; break;
						case
			3: dir_c = contour[h+1][w]; break;
		}
//		if (dir_c != -1) 
			contour[h][w] = dir_c;
		}
		}
}

int main
(int argc, char* argv[])
{
	std::string alpha="abcdefghijklmnopqrstuvwxyz";
	std::ifstream file("in.txt");
	std::ofstream out("out.txt");

	int T;
	int H, W;
	file >> T;

	for (int t=0; t<T; t++)
	{
		//read h w
		file >> H;
		file >> W;

		//read map
		vvi map;
		vvi contour;
		vvi dir;
		for (int h=0; h<H; h++)
		{
			vi v;
			for (int w=0; w<W; w++)
			{
				int temp;
				file >> temp;
				v.push_back(temp);
			}
			map.push_back(v);
		}

		vi v;
		for (int w=0; w<W; w++)
			v.push_back(-1);
		for (int h=0; h<H; h++)
		{
		dir.push_back(v);
		contour.push_back(v);
		}
		int b = basins(H,W,map,contour);

		dirs(H,W,map,dir);

		//update contour
		for (int i=0; i<(H>W?H*2:W*2); i++) update_contour(H, W, contour, dir);

		//assign letters
		int taken=0;
		std::string letters;
		for (int i=0; i<=b; i++) letters.push_back('-');

		for (int h=0; h<H; h++)
			for (int w=0; w<W; w++)
			{
			if ( letters[ contour[h][w] ] == '-')
			{
			letters[ contour[h][w] ] = alpha[taken];
			taken++;
			}
			}

		out << "Case #" << t+1 << ":";
	//out << b;
	out << std::endl;
	for (int h=0; h<H; h++)
	{
	
		for (int w=0; w<W; w++)
			out << letters[ contour[h][w] ] << " ";
		out << std::endl;
	}


	}


return 0;
}

