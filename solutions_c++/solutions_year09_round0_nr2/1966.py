#include <fstream>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

int H, W, T;
vector<int> g_map;
vector<int> g_labels;

vector<int> g_rowbuffer;
vector<int> g_colbuffer;

int g_neighX[4] = {0, -1, 1, 0};
int g_neighY[4] = {-1, 0, 0, 1};
int g_lbl = 0;

void FillAllBuffer(int lbl)
{
	for (int i=0; i<g_rowbuffer.size(); i++)
	{
		int idx=g_rowbuffer[i]*W + g_colbuffer[i];
		g_labels[idx] = lbl;
	}
	g_rowbuffer.clear();
	g_colbuffer.clear();
}

void PrintLables()
{
	for (int i=0; i<H; i++)
	{
		for (int j=0; j<W; j++)
		{
			cout << g_labels[i*W+j] << " ";
		}
		cout << endl;
	}
}

void FillLabel(int row, int col)
{
	int idx  = row * W + col;
	
	int minVal = g_map[idx], minRow=-1, minCol =  -1;
	for (int i=0; i<4; i++)
	{
		int neighRow = row + g_neighY[i];
		int neighCol = col + g_neighX[i];
		if (neighRow >=0 && neighRow < H && neighCol >= 0 && neighCol < W)
		{
			int neighNum = neighRow * W + neighCol;
			if ( g_map[neighNum] < minVal)
			{
				minVal = g_map[neighNum];
				minRow = neighRow;
				minCol = neighCol;
			}
		}
	}

	if (minRow != -1)
	{
		if (g_labels[minRow * W + minCol] != -1)
		{
			FillAllBuffer(g_labels[minRow * W + minCol]);
		}
		else{
			g_rowbuffer.push_back(minRow);
			g_colbuffer.push_back(minCol);
		}
	}
	else
	{		
		FillAllBuffer(g_lbl++);
	}
}

void Watershed()
{
	g_labels.assign(H*W, -1);
	g_lbl = 0;
	for (int i=0; i<H; i++)
	{
		for (int j=0; j<W; j++)
		{
			int idx  = i * W + j;
			if (g_labels[idx] != -1)
				continue;
			g_rowbuffer.push_back(i);
			g_colbuffer.push_back(j);
			FillLabel(i, j);
			while (!g_rowbuffer.empty())
			{
				int row = g_rowbuffer.back();
				int col = g_colbuffer.back();
				FillLabel(row, col);
			}
		//	PrintLables();

		}
	}
}

ifstream inFile;
ofstream outFile;

void ParseInput()
{
	inFile >> H >> W;
	g_map.clear();
	for (int i=0; i<H; i++)
	{
		for (int j=0; j<W; j++)
		{
			int val = 0;
			inFile >> val;
			g_map.push_back(val);
		}
	}
}

void PrintOutput(int caseNum)
{
	outFile << "Case #" << caseNum << ":" << endl;
	for (int i=0; i<H; i++)
	{
		for (int j=0; j<W; j++)
		{
			char str = g_labels[i*W+j] + 'a';
			outFile << str << " " ;
		}
		outFile << endl;
	}
}

int main()
{
//	const char *inFileName = "B-small-attempt0.in";
	const char *inFileName = "B-large.in";
//	const char *inFileName = "test.in";
//	const char *outFileName = "B-small.out";
	const char *outFileName = "B-large.out";

	inFile.open(inFileName);
	outFile.open(outFileName);
	
	inFile >> T;
	for (int caseNum = 0; caseNum < T; caseNum++)
	{
		ParseInput();
		Watershed();
		PrintOutput(caseNum+1);
	}
}