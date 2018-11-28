#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

std::ifstream input;
std::ofstream output;

struct tCell
{
	int alt;
	char sink;

	tCell() : alt(-1), sink(-1) { }
};

void TestCase(int testCase);

int main()
{
	input.open("B-large.in");
	output.open("output.txt", std::ios_base::trunc);
	
	int numTestCases = 0;
	input >> numTestCases;
	for(int i=0; i<numTestCases; ++i)
	{
		TestCase(i + 1);
	}

	output.close();
	input.close();

	return 0;
}

char findSink(std::vector<tCell> &cells, char &nextSink, int height, int width, int i, int j)
{
	tCell *pCell = &cells[i*width + j];
	if(pCell->sink != -1)
		return pCell->sink;

	int north, west, east, south;
	north = west = east = south = INT_MAX;

	if(i > 0)
		north = cells[(i-1)*width + j].alt;
	if(j > 0)
		west = cells[i*width + j-1].alt;
	if(j < width-1)
		east = cells[i*width + j+1].alt;
	if(i < height-1)
		south = cells[(i+1)*width + j].alt;
	
	int lowest = std::min(north, std::min(west, std::min(east, south)));
	if(lowest < pCell->alt)
	{
		if(lowest == north)
			return pCell->sink = findSink(cells, nextSink, height, width, i-1, j);
		else if(lowest == west)
			return pCell->sink = findSink(cells, nextSink, height, width, i, j-1);
		else if(lowest == east)
			return pCell->sink = findSink(cells, nextSink, height, width, i, j+1);
		else if(lowest == south)
			return pCell->sink = findSink(cells, nextSink, height, width, i+1, j);
	}

	return pCell->sink = nextSink++;
}

void TestCase(int testCase)
{
	int height, width;
	input >> height;
	input >> width;

	std::vector<tCell> cells(height * width);
	char nextSink = 'a';

	for(int i=0; i<height*width; ++i)
	{
		input >> cells[i].alt;
	}

	for(int i=0; i<height; ++i)
	{
		for(int j=0; j<width; ++j)
		{
			cells[i*width + j].sink = findSink(cells, nextSink, height, width, i, j);
		}
	}

	output << "Case #" <<  testCase << ":\n";
	for(int i=0; i<height; ++i)
	{
		for(int j=0; j<width; ++j)
		{
			output << cells[i*width + j].sink;
			if(j != width-1)
				output << ' ';
		}
		output << '\n';
	}
}
