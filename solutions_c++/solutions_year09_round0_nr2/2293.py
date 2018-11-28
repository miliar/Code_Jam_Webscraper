// gcj2009b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input_file;
	ofstream output_file;
	input_file.open("B-large.in");
	output_file.open("b-large.out");
	int n_tests;
	int height, width;
	input_file >> n_tests;
	bool change = true;
	int min;
	for (int test = 0; test < n_tests; ++test)
	{
		input_file >> height >> width;
		vector<vector<int>> water;
		vector<vector<int>> basin;
		vector<int> temp_vi;
		vector<string> res;
		string map_str;
		map_str.resize(10001, ' ');
		string temp_str;
		temp_str.resize(width, ' ');
		res.resize(height, temp_str);
		temp_vi.resize(width + 2, 10001);
		water.resize(height + 2, temp_vi);
		basin.resize(height + 2, temp_vi);
		for (int j = 1; j < height + 1; ++j)
			for (int i = 1; i < width + 1; ++i)
				input_file >> water[j][i];
		change = true;
		while(change)
		{
			change = false;
			int cur_basin = 0;
			for (int j = 1; j < height + 1; ++j)
			{
				for (int i = 1; i < width + 1; ++i)
				{
					min = 10001;
					min = std::min(water[j][i], std::min(water[j-1][i], std::min(water[j][i-1], std::min(water[j][i+1], water[j+1][i]))));

					if (min != water[j][i])
					if (min == water[j-1][i])
					{
						if (basin[j-1][i] != basin[j][i])
						{
							basin[j][i] = basin[j-1][i];
							change = true;
						}
					}
					else if (min == water[j][i-1])
					{
						if (basin[j][i-1] != basin[j][i])
						{
							basin[j][i] = basin[j][i-1];
							change = true;
						}
					}
					else if (min == water[j][i+1])
					{
						if (basin[j][i+1] != basin[j][i])
						{
							basin[j][i] = basin[j][i+1];
							change = true;
						}
					}
					else if (min == water[j+1][i])
					{
						if (basin[j+1][i] != basin[j][i])
						{
							basin[j][i] = basin[j+1][i];
							change = true;
						}
					}
					if (basin[j][i] == 10001)
					{
						basin[j][i] = cur_basin;
						++cur_basin;
						change = true;
					}
				}
			}
		}
		output_file << "Case #" << test + 1 << ":" << endl;
		char cur_char = 'a';
		for (int j = 1; j < height + 1; ++j)
			for (int i = 1; i < width + 1; ++i)
			{
				if (map_str[basin[j][i]] == ' ')
				{
					map_str[basin[j][i]] = cur_char;
					++cur_char;
				}
			}
		for (int j = 1; j < height + 1; ++j)
			for (int i = 1; i < width + 1; ++i)
				res[j-1][i-1] = map_str[basin[j][i]];
		for (int j = 0; j < height; ++j)
		{
			for (int i = 0; i < width - 1; ++i)
			{
				output_file << res[j][i] << ' ';
			}
			output_file << res[j][width-1] << endl;
		}
		
	}

	input_file.close();
	output_file.close();
	return 0;
}

