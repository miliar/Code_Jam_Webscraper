#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>

using std::vector;
using std::string;
using std::pair;
using std::set;
using std::map;

using std::fstream;
using std::istream;
using std::ostream;
using std::cin;
using std::cout;

using std::min;

class Map
{
private: 
	pair<int, int> NextCell(const pair<int, int> &cell) const
	{
		pair<int, int> innerCell(cell);

		pair<int, int> northCell	(innerCell.first - 1,	innerCell.second		);
		if (northCell.first < 0) 
			northCell.first = 0;

		pair<int, int> westCell		(innerCell.first,		innerCell.second - 1	);
		if (westCell.second < 0) 
			westCell.second = 0;

		pair<int, int> eastCell		(innerCell.first,		innerCell.second	+ 1	);
		if (eastCell.second >= altitudes[0].size()) 
			eastCell.second = altitudes[0].size() - 1;

		pair<int, int> southCell	(innerCell.first + 1,	innerCell.second		);
		if (southCell.first >= altitudes.size()) 
			southCell.first = altitudes.size() - 1;

		int north, west, east, south;
		north = altitudes[northCell.first][northCell.second];
		west = altitudes[westCell.first][westCell.second];
		east = altitudes[eastCell.first][eastCell.second];
		south = altitudes[southCell.first][southCell.second];

		if (min(north, min(west, min(east, south))) >= altitudes[cell.first][cell.second])
			return innerCell;

		if ((south < east) && (south < west) && (south < north))
			return southCell;
		
		if ((east < west) && (east < north))
			return eastCell;
		
		if (west < north)
			return westCell;

		return northCell;
	}

	vector<string> Basins() const
	{
		int width = altitudes[0].size();
		int height = altitudes.size();
		vector<vector<pair<int, int> > > whereDrains
			(height, vector<pair<int, int> > (width, pair<int, int> (-1, -1)));

		for (int i = 0; i < height; ++i)
			for (int j = 0; j < width; ++j)
			{
				pair<int, int> coord(i, j);

				pair<int, int> nextCoord = NextCell(coord);

				while (coord != nextCoord)
				{
					coord = nextCoord;
					nextCoord = NextCell(coord);
				}

				whereDrains[i][j] = coord;
			}


		pair<pair<int, int>, char> trivialPair(whereDrains[0][0], 'a');
		map<pair<int, int>, char> bassinMap;
		bassinMap.insert(trivialPair);

		char lastUsedChar = 'a';

		vector<string> result(height);

		for (int i = 0; i < height; ++i)
		{
			string s;
			s.resize(width);
			for (int j = 0; j < width; ++j)
			{
				map<pair<int, int>, char>::iterator It = bassinMap.find(whereDrains[i][j]);
				if (It != bassinMap.end())
				{
					s[j] = It->second;
				}
				else
				{
					++lastUsedChar;
					s[j] = lastUsedChar;
					pair<pair<int, int>, char> currentPair (whereDrains[i][j], lastUsedChar);
					bassinMap.insert(currentPair);
				}
			}
			result[i] = s;
		}
		return result;		
	}

public:
	vector<vector<int> > altitudes;

	friend istream& operator >> (istream &input, Map &m)
	{
		int H, W;
		input >> H >> W;

		m.altitudes.resize(H, vector<int> (W));

		for (int i = 0; i < H; ++i)
			for (int j = 0; j < W; ++j)
				input >> m.altitudes[i][j];

		return input;
	}

	friend ostream& operator << (ostream& output, const Map &m)
	{
		vector<string> basins = m.Basins();

		for (int i = 0; i < basins.size(); ++i)
		{
			for (int j = 0; j < basins[i].size(); ++j)
			{
				output << basins[i][j] << " ";
			}
			output << std::endl;
		}
		return output;
	}
};

int main()
{
	fstream input("input.txt", std::ios::in);
	fstream output("output.txt", std::ios::out);

	int testNumber;

	input >> testNumber;

	for (int i = 0; i < testNumber; ++i)
	{
		Map m;
		input >> m;
		output << "Case #" << (i + 1) << ": " << std::endl <<  m;
	}
	
	return 0;
}