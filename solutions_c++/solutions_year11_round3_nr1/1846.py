#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

class Question
{
private:
	set< pair<int, int> > tiles;
	vector<string> finished;
	bool possible;
	int w,h;
public:
	Question(){}
	
	bool tile_start(int row, int col)
	{
		set< pair<int, int> >::iterator found = tiles.find(pair<int, int>(row, col));
		return tiles.end() != found;
	}
	
	char get_character(int row, int col)
	{
		if(row > 0 && tile_start(row - 1, col))
		{
			return '\\';
		}
		else if(row > 0 && col > 0 && tile_start(row - 1, col - 1))
		{
			return '/';
		}
		else if(row < h-1 && col > 0 && tile_start(row, col - 1 ))
		{
			return '\\';
		}
		else if(row > 0 && col < w - 1 && tile_start(row-1, col + 1))
		{
			possible = false;
			return '.';
		}
		else if(row < h-1 && col < w-1)
		{
			tiles.insert( pair<int, int>(row, col));
			return '/';
		}
		else 
		{
			possible = false;
			return '.';
		}
				
		return '.';
	}
	
	bool valid_white(int row, int col)
	{
		if(row > 0 && tile_start(row - 1, col))
		{
			return false;
		}
		else if(row > 0 && col > 0 && tile_start(row - 1, col - 1))
		{
			return false;
		}
		else if(row < h-1 && col > 0 && tile_start(row, col - 1 ))
		{
			return false;
		}
		
		return true;
	}
	
	void read(ifstream* in, int row, int col)
	{
		char inp;
		w = col;
		h = row;
		possible = true;
		finished = vector<string>(row);
		for (int i = 0; i < row; i ++) 
		{
			for (int j = 0; j < col; j ++)
			{
				*in >> skipws >> inp;
				if(possible)
				{
					if(inp == '.')
					{
						possible = valid_white(i, j);
						finished[i] += inp;
					}
					else 
					{
						finished[i] += get_character(i, j);
					}
				}
			}
		}
	}
	
	void print(ofstream* out, int row)
	{
		if(possible)
		{
			for (int i = 0 ; i < row; i ++) 
			{
				*out << finished[i] << endl;
			}
		}
		else {
			*out << "Impossible" << endl;
		}

	}
};


int main (int argc, char * const argv[]) {
    // insert code here...
	Question* answer;
	string file = "../../data/A-large";
	
	ifstream inputFile(string(file + ".in.txt").c_str());
	ofstream outputFile(string(file + ".out").c_str());
	
	int numCases, Case;
	inputFile >> numCases;
	int row, col;
	
	for (Case = 1; Case <= numCases; Case ++) 
	{
		inputFile >> skipws >> row >> col;
		answer = new Question();
		answer->read(&inputFile, row, col);
		
		outputFile << "Case #" << Case << ":" << endl;
		answer->print(&outputFile, row);
		delete answer;
	}
	
    return 0;
}
