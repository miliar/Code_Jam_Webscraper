#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

struct Cell;
typedef vector<vector<Cell*> > CellMap;

struct Cell
{
	Cell(unsigned int x, unsigned int y, unsigned int height, CellMap& cells) : x(x), y(y), cells(cells), sinkFound(false)
	{
		src = sink = this;
	}
	void findSink()
	{
		const int directions[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};
		sinkFound = true;
		for (int i = 0; i < 4; i++)
		{
			int dx = directions[i][0];
			int dy = directions[i][1];

			if (x + dx < 0 || x + dx >= cells.size() ||
				y + dy < 0 || y + dy >= cells[x + dx].size())
				continue;
			if (cells[x + dx][y + dy]->height < src->height)
			{
				src = cells[x + dx][y + dy];
			}
		}
		if (!src->sinkFound)
		{
			src->findSink();
		}
		sink = src->sink;
	}
	
	bool sinkFound;
	CellMap& cells;
	unsigned int x, y, height;
	Cell *src;
	Cell *sink;
};
int main()
{
	//const string FILENAME = "C:\\CodeJam\\water\\test-in.txt";
	//const string FILENAME = "C:\\CodeJam\\water\\B-small-attempt0.in";
	const string FILENAME = "C:\\CodeJam\\water\\B-large.in";
	
	const string OUTFILE = FILENAME + ".out.txt";
	
	ifstream inFile(FILENAME.c_str());
	ofstream outFile(OUTFILE.c_str());

	unsigned int t;
	inFile >> t;
	inFile.ignore();

	for (unsigned int caseId = 1; caseId <= t; caseId++)
	{
		unsigned int w, h;
		inFile >> h >> w;
		inFile.ignore();

		CellMap cells;
		for (unsigned int x = 0; x < w; x++)
		{
			cells.push_back(vector<Cell*>());
			for (unsigned int y = 0; y < h; y++)
			{
				cells[x].push_back(new Cell(x, y, 0, cells));
			}
		}

		for (unsigned int y = 0; y < h; y++)
		{
			for (unsigned int x = 0; x < w; x++)
			{
				int h;
				inFile >> h;
				cells[x][y]->height = h;
			}
		}

		for (unsigned int x = 0; x < w; x++)
		{
			for (unsigned int y = 0; y < h; y++)
			{
				cells[x][y]->findSink();
			}
		}
		outFile << "Case #" << caseId << ":" << std::endl;
		map<Cell*, char> sinkLabels;
		char label = 'a';
		for (unsigned int y = 0; y < h; y++)
		{
			for (unsigned int x = 0; x < w; x++)
			{
				Cell* sink = cells[x][y]->sink;
				if (sinkLabels.find(sink) == sinkLabels.end())
				{
					sinkLabels[sink] = label++;
				}
				
				outFile << sinkLabels[sink];
				
				if (x + 1 != w)
				{
					outFile << " ";
				}
			}
			outFile << std::endl;
		}
	}
	
	return 0;
}