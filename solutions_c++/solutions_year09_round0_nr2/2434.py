
#define maxT 100
#define maxH 100
#define maxW 100
#define maxL 10005

#include <fstream>
using namespace std;

int map[maxH][maxW];
int mapstr[maxH][maxW];
int mapdir[maxH][maxW];
int pos[4][2]={{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int T, H, W;

int findminDirect(int j, int k)
{
	int tempp = -1;
	int p;
	int min = maxL;
	for(p = 0; p < 4; p++)
	{
		if(j + pos[p][0] >= 0 && j + pos[p][0] <= H-1
		&& k + pos[p][1] >= 0 && k + pos[p][1] <= W-1)
		{
			if( map[j + pos[p][0]][k + pos[p][1]] < min )
			{
				min = map[j + pos[p][0]][k + pos[p][1]];
				tempp = p;
			}
		}
	}
	return tempp;
}

void findAllDirect()
{
	for(int i = 0; i < H; i++)
	{
		for(int j = 0; j < W; j++)
		{
			mapdir[i][j] = findminDirect(i, j);
		}
	}
}


void solver(int j, int k, int lever)
{
	int minpos, p;

	mapstr[j][k] = lever;
	minpos = mapdir[j][k];

	if( map[j + pos[minpos][0]][k + pos[minpos][1]] < map[j][k] )
	{
		if( mapstr[j + pos[minpos][0]][k + pos[minpos][1]] < 0 )
		{
			mapstr[j + pos[minpos][0]][k + pos[minpos][1]] = lever;
			solver(j + pos[minpos][0], k + pos[minpos][1], lever);
		}
	}
	
	for(p = 0; p < 4; p++)
	{
		if(j + pos[p][0] >= 0 && j + pos[p][0] <= H-1
		&& k + pos[p][1] >= 0 && k + pos[p][1] <= W-1)
		{
			if(mapdir[j + pos[p][0]][k + pos[p][1]] + p == 3 &&
			map[j + pos[p][0]][k + pos[p][1]] > map[j][k] &&
			mapstr[j + pos[p][0]][k + pos[p][1]] < 0)
			{
				mapstr[j + pos[p][0]][k + pos[p][1]] = lever;
				solver(j + pos[p][0], k + pos[p][1], lever);
			}
		}
	}
}

int main()
{
	int i, j, k;
	int lever;

	ifstream infile("B-large.in");
	ofstream outfile("B-large.out");

	infile>>T;
	for(i = 0; i < T; i++)
	{
		infile>>H>>W;
		for(j = 0; j < H; j++)
		{
			for(k = 0; k < W; k++)
			infile>>map[j][k];
		}

		for(j = 0; j < H; j++)
			for(k = 0; k < W; k++)
			mapstr[j][k] = -1;
			
		findAllDirect();
		
		lever = 0;
		solver(0, 0, lever);
		for(j = 0; j < H; j++)
		{
			for(k = 0; k < W; k++)
			{
				if(mapstr[j][k] < 0)
				{
					lever++;
					solver(j, k, lever);
				}
			}
		}
		outfile<<"Case #"<<i+1<<":"<<endl;
		for(j = 0; j < H; j++)
		{
			outfile<<(char)(mapstr[j][0]+97);
			for(k = 1; k < W; k++)
			outfile<<' '<<(char)(mapstr[j][k]+97);
			outfile<<endl;
			
			//outfile<< mapdir[j][k]<<' ';
			//outfile<<endl;
		}
	}
	infile.close();
	outfile.close();
	return 0;
}

