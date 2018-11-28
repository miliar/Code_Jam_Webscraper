#include <fstream>
#include <stack>

using namespace std;

struct cell
{
	char basin;
	int elevation;
};

struct map
{
	cell** cells;
	int height;
	int width;
};


//function prototypes
void defineBasins(map &);
void tracePath(map &, int, int, char &);
void moveDownhill(map &, int & , int &);
int findMin(int []);
void redefinePath(map &, stack<int> &, char);
bool isSink(map &, int, int);

int main()
{
	int numMaps;
	map* theMaps;

	ifstream infile;
	infile.open("dataset.txt");
	infile>>numMaps;
	theMaps = new map[numMaps];

	for(int i = 0; i < numMaps; i++)
	{
		infile>>theMaps[i].height>>theMaps[i].width;
		theMaps[i].cells = new cell*[theMaps[i].height];
		for(int j = 0; j < theMaps[i].height; j++)
			theMaps[i].cells[j] = new cell[theMaps[i].width];

		for(int j = 0; j < theMaps[i].height; j++)
		{
			for(int k = 0; k < theMaps[i].width; k++)
			{
				infile>>theMaps[i].cells[j][k].elevation;
				theMaps[i].cells[j][k].basin = '\0';
			}
		}

		defineBasins(theMaps[i]);
	}

	infile.close();

	ofstream outfile;
	outfile.open("output.txt");

	for(int i = 0; i < numMaps; i++)
	{
		if(i != 0)
			outfile<<"\n";

		outfile<<"Case #"<<i + 1<<":\n";
		for(int j = 0 ; j < theMaps[i].height; j++)
		{
			for(int k = 0; k < theMaps[i].width; k++)
				outfile<<theMaps[i].cells[j][k].basin<<" ";
	
			outfile<<"\n";
		}

		for(int j = 0; j < theMaps[i].height; j++)
			delete [] theMaps[i].cells[j];

		delete [] theMaps[i].cells;
	}

	outfile.close();

	delete [] theMaps;
	return 0;
}

void defineBasins(map & m)
{
	char currentBasin = 'a';
	for(int i = 0; i < m.height; i++)
	{
		for(int j = 0; j < m.width; j++)
			tracePath(m, i, j, currentBasin);
	}
}

void tracePath(map & m, int row, int column, char & currentBasin)
{
	stack<int> path;
	while(!isSink(m, row, column))
	{
		if(m.cells[row][column].basin == '\0')
		{
			m.cells[row][column].basin = currentBasin;
			path.push(column);
			path.push(row);
			moveDownhill(m, row, column);  //changes row and column to next cell
		}
		else
		{
			redefinePath(m, path, m.cells[row][column].basin);
			goto end;
		}
	}

	if(m.cells[row][column].basin == '\0')
	{
		m.cells[row][column].basin = currentBasin;
		currentBasin++;
	}
	else
		redefinePath(m, path, m.cells[row][column].basin);

end:
	return;
}

bool isSink(map & m, int row, int column)
{
	for(int i = -1; i < 2; i+=2)
	{
		//check north-south
		if(row + i >= 0 && row + i < m.height)
		{
			if(m.cells[row][column].elevation > m.cells[row + i][column].elevation)
				return false;
		}

		//check east-west
		if(column + i >= 0 && column + i < m.width)
		{
			if(m.cells[row][column].elevation > m.cells[row][column + i].elevation)
				return false;
		}
	}

	return true;
}

void redefinePath(map & m, stack<int> & s, char b)
{
	while(!s.empty())
	{
		int row = s.top();
		s.pop();
		int column = s.top();
		s.pop();
		m.cells[row][column].basin = b;
	}
}

void moveDownhill(map & m, int & row, int & column)
{
	int borderElevations[4]; //0: north 1: west 2:east 3:south

	if(row > 0)
		borderElevations[0] = m.cells[row-1][column].elevation;
	else
		borderElevations[0] = 100001;

	if(column > 0)
		borderElevations[1] = m.cells[row][column - 1].elevation;
	else
		borderElevations[1] = 100001;

	if(column < m.width - 1)
		borderElevations[2] = m.cells[row][column + 1].elevation;
	else
		borderElevations[2] = 100001;

	if(row < m.height - 1)
		borderElevations[3] = m.cells[row + 1][column].elevation;
	else
		borderElevations[3] = 100001;

	int minElevation = findMin(borderElevations);

	if(borderElevations[0] == minElevation)
	{
		row--;
		return;
	}
	if(borderElevations[1] == minElevation)
	{
		column--;
		return;
	}
	if(borderElevations[2] == minElevation)
	{
		column++;
		return;
	}

	row++;
}

int findMin(int elevations [])
{
	int min = elevations[0];

	for(int i = 1; i < 4; i++)
	{
		if(elevations[i] < min)
			min = elevations[i];
	}

	return min;
}