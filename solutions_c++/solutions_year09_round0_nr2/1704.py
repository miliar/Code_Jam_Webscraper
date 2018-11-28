#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("out.txt");

	int row, col;
const int MAX_ROWS = 110;
const int MAX_COLS = 110;
int tab[MAX_ROWS][MAX_COLS];
char flow[MAX_ROWS][MAX_COLS];
char currentC;

struct Path
{
	int r;
	int c;
};
vector<Path> path;


void findSink(int r, int c, int& minR, int& minC)
{
	int north, south, east, west;
	int minAtt = tab[r][c];
	minR = -1;
	minC = -1;
	if (r >= 1)
		north = tab[r-1][c];
	else
		north = -1;
	south = tab[r+1][c];
	east = tab[r][c+1];
	if (c >= 1)
		west = tab[r][c-1];
	else
		west = -1;

//	cout << "North: " << north << "  South: " << south << "  East: " << east << "  West: " << west << endl;

	if (north < minAtt)
	{
		if (north != -1) {
		minAtt = north;
		minR = -1;
		minC = 0;}
	}
	if (west < minAtt)
	{
		if (west != -1) {
		minAtt = west;
		minR = 0;
		minC = -1;}
	}
	if (east < minAtt)
	{
		if (east != -1 ) {
		minAtt = east;
		minR = 0;
		minC = 1;}
	}
	if (south < minAtt)
	{
		if (south != -1 ){
		minAtt = south;
		minR = 1;
		minC = 0;}
	}
	

//	cout << "minR: " << minR << "  minC: " << minC << endl;
}

void traverse(int r, int c)
{
	int minR, minC;
	findSink(r, c, minR, minC);

	// sink found
	if (minR == -1 && minC == -1)
	{
//		cout << "Found sink at " << r << ", " << c << endl;
		flow[r][c] = currentC;
		for (int i = 0; i < path.size(); i++)
		{
			flow[path[i].r][path[i].c] = currentC;
		}
		path.clear();
		currentC++;

/*		for (int r = 0; r < row; r++)
	{
		for (int c = 0; c < col; c++)
		{
			cout << flow[r][c] << " ";
		}
		cout << endl;
	}*/

		return;
	}
	else if (flow[r+minR][c+minC] != '\0')
	{
//		cout << "Found filled at " << r+minR << ", " << c+minC << endl;
		char chh = flow[r+minR][c+minC];
		flow[r][c] = chh;
		for (int i = 0; i < path.size(); i++)
		{
			flow[path[i].r][path[i].c] = chh;
		}
		path.clear();

/*		for (int r = 0; r < row; r++)
	{
		for (int c = 0; c < col; c++)
		{
			cout << flow[r][c] << " ";
		}
		cout << endl;
	}*/
		return;
	}
	else 
	{
		Path pathtemp;
		pathtemp.r = r;
		pathtemp.c = c;
		path.push_back(pathtemp);
		traverse(r + minR, c + minC);
	}
}

int main()
{
	int N;
	fin >> N;
	for (int i = 0; i < N; i++) {
	fin >> row >> col;
	
	for (int r = 0; r < MAX_ROWS; r++)
	{
		for (int c = 0; c < MAX_COLS; c++)
		{
			tab[r][c] = -1;
			flow[r][c] = '\0';
		}
	}
	for (int r = 0; r < row; r++)
	{
		for (int c = 0; c < col; c++)
		{
			fin >> tab[r][c];
		}
	}


	int minR, minC;
	currentC = 'a';
	for (int r = 0; r < row; r++)
	{
		for (int c = 0; c < col; c++)
		{
			findSink(r, c, minR, minC);

			// sink found
			if (minR == -1 && minC == -1)
			{
//				cout << "Found sink at " << r << ", " << c << endl;
				if (flow[r][c] == '\0')
				{
				flow[r][c] = currentC;
				for (int i = 0; i < path.size(); i++)
				{
					flow[path[i].r][path[i].c] = currentC;
				}
				path.clear();

/*				for (int r = 0; r < row; r++)
	{
		for (int c = 0; c < col; c++)
		{
			cout << flow[r][c] << " ";
		}
		cout << endl;
	}*/
				currentC++;
				}
			}
			else if (flow[r+minR][c+minC] != '\0')
			{
//				cout << "Found filled at " << r+minR << ", " << c+minC << endl;
				char chh = flow[r+minR][c+minC];
				flow[r][c] = chh;
				for (int i = 0; i < path.size(); i++)
				{
					flow[path[i].r][path[i].c] = chh;
				}
				path.clear();

/*				for (int r = 0; r < row; r++)
	{
		for (int c = 0; c < col; c++)
		{
			cout << flow[r][c] << " ";
		}
		cout << endl;
	}*/
			}
			else 
			{
				Path pathtemp;
				pathtemp.r = r;
				pathtemp.c = c;
				path.push_back(pathtemp);
				traverse(r + minR, c + minC);
			}
		}
	}

	fout << "Case #"<<i+1<<":\n";
	for (int r = 0; r < row; r++)
	{
		for (int c = 0; c < col; c++)
		{
			fout << flow[r][c];
			if (c != col - 1)
				fout << " ";
		}
		fout << endl;
	}

	}

}