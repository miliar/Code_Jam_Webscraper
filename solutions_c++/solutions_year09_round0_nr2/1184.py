#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

struct Node
{
	bool visited;
	char label;
	Node *next;
	Node *prevs[4];
	int prevCount;
};

int al[100][100];
Node fl[100][100];
int H, W;

bool getNeighbor(int i, int j, int &ni, int &nj)
{
	bool isSink = true;
	int lowest = al[i][j];
	if ( i > 0 && al[i-1][j] < lowest)
	{
		lowest = al[i-1][j];
		ni = i-1;
		nj = j;
		isSink = false;
	}
	if ( j > 0 && al[i][j-1] < lowest)
	{
		lowest = al[i][j-1];
		ni = i;
		nj = j-1;
		isSink = false;
	}
	if ( j < W-1 && al[i][j+1] < lowest)
	{
		lowest = al[i][j+1];
		ni = i;
		nj = j+1;
		isSink = false;
	}
	if ( i < H-1 && al[i+1][j] < lowest)
	{
		lowest = al[i+1][j];
		ni = i+1;
		nj = j;
		isSink = false;
	}
	return isSink;
}
void makeFlow(int r, int c)
{
	if (fl[r][c].visited) return;

	Node *node = &fl[r][c];
	node->visited = true;
	node->label = 0;
	node->prevCount = 0;
	node->next = NULL;

	int ni, nj;
	if (!getNeighbor(r,c,ni,nj))
	{
		node->next = &fl[ni][nj];
		makeFlow(ni, nj);
		node->next->prevs[node->next->prevCount++]= node;
	}
}
void makeFlow()
{
	for (int i=0; i < H; ++i)
		for(int j=0; j<W; ++j)
			makeFlow(i, j);
}

void label(Node *node, char l)
{
	if (node == NULL || node->label !=0) return;

	node->label = l;
	label(node->next, l);
	for (int i = 0; i < node->prevCount; ++i)
		label(node->prevs[i], l);
}

void label()
{
	char l='a';
	for (int i=0; i < H; ++i)
		for (int j=0; j < W; ++j)
			if (fl[i][j].label == 0)
				label(&fl[i][j], l++);
}

void readData()
{
	memset( al, 0, sizeof(al));
	memset( fl, 0, sizeof(fl));
	std::cin >> H >> W;
	for (int i=0; i < H; ++i)
		for (int j=0; j< W; ++j)
			std::cin >> al[i][j];
}
void printLabels()
{
	for (int i=0; i < H; ++i)
	{
		for (int j=0; j< W; ++j)
		{
			if (j) std::cout << " ";
			std::cout << fl[i][j].label;
		}
		std::cout << std::endl;
	}
}

int main()
{
	int tt;
	std::cin >> tt;
	for(int i=0; i < tt;++i)
	{
		readData();
		makeFlow();
		label();
		std::cout << "Case #" << i+1 <<":" << std::endl;
		printLabels();
	}
	return 0;
}
