

#include<iostream>
#include <fstream>
#include <vector>


using namespace std;

enum direction
{
	SINK =  0,
	NORTH, 
	WEST, 
	EAST, 
	SOUTH
};


int getNextNeighbour(const vector<vector<int> >& value, int l, int c)
{
	int curHeight = value[l][c];
	int minHeight = curHeight;
	int dir = SINK;
	if (l != 0 && value[l - 1][c] < minHeight)
	{
		dir = NORTH;
		minHeight =  value[l - 1][c];
	}
	if (c != 0 && value[l][c - 1] < minHeight)
	{
		dir = WEST;
		minHeight =  value[l][c - 1];
	}
	if (c + 1 != value[l].size() && value[l][c + 1] < minHeight)
	{
		dir = EAST;
		minHeight =  value[l][c + 1];
	}
	if (l + 1 != value.size()/value[l].size() && value[l + 1][c] < minHeight)
	{
		dir = SOUTH;
		minHeight =  value[l + 1][c];
	}

	return dir;
}


int main(int argc, char** argv)
{
	char * input = argv[1];
	std::ifstream file (input);
	int NbrCase, line, col;
	file >> NbrCase; 
		
	for (int i = 1; i <= NbrCase; ++i)
	{
		file >> line >> col;	
		vector<vector<int> > value;
		vector<vector<char> > label;

		for(int l = 0; l < line; ++l)
			for(int c = 0; c < col; ++c)
			{
				value.push_back(vector<int>());
				label.push_back(vector<char>());
				int val;
				file >> val;
				value[l].push_back(val);
				label[l].push_back('0');
			}

		char nextLabel = 'a';

		for(int l = 0; l < line; ++l)
			for(int c = 0; c < col; ++c)
			{
				if (label[l][c] != '0')
					continue;
				int path_c = c;
				int path_l = l;
				vector <char *> path;
				while(1)
				{
					path.push_back(&(label[path_l][path_c]));
					int next = getNextNeighbour(value, path_l, path_c);
					if (next == SINK)
					{
						for (int k = 0; k < path.size(); ++k)
							*(path[k]) = nextLabel;
						nextLabel ++;
						break;
					}
					if (next == NORTH)
						path_l--;
					if (next == EAST)
						path_c++;
					if (next == WEST)
						path_c--;
					if (next == SOUTH)
						path_l++;
					if (label[path_l][path_c] != '0')
					{
						for (int k = 0; k < path.size(); ++k)
							*(path[k]) = label[path_l][path_c];
						break;
					}
				}
			}
		cout << "Case #" << i << ":" << endl;
		for(int l = 0; l < line; ++l)
			for(int c = 0; c < col; ++c)
			{
				cout << label[l][c];
				if (c == col - 1)
					cout << endl;
				else 
					cout << " ";
			}	
	}
	return 0;
}

