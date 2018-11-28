#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

typedef struct LatLon
{
	int x;
	int y;
}LatLon;


int choose(int **arr, int i, int j, int H, int W)
{
	int pos = -1;
	int min = 0x7fffffff;
	if(i != 0)
	{
		if(min > arr[i - 1][j])
		{
			min = arr[i - 1][j];
			pos = 0;
		}
	}
	if(j != 0)
	{
		if(min > arr[i][j - 1])
		{
			min = arr[i][j - 1];
			pos = 1;
		}
	}
	if(j != W - 1)
	{
		if(min > arr[i][j + 1])
		{
			min = arr[i][j + 1];
			pos = 2;
		}
	}
	if(i != H - 1)
	{
		if(min > arr[i + 1][j])
		{
			min = arr[i + 1][j];
			pos = 3;
		}
	}

	if(min >= arr[i][j])
	{
		return -1;
	}

	return pos;
}

int main()
{
	ifstream in("D:\\B-small-attempt0.in.txt");
	ofstream out("D:\\result.txt");
	
	int T, H, W;
	in >> T;

	int **map;
	char **result;

	for(int i = 0; i < T; i++)
	{
		in >> H >> W;
		map = (int**)malloc(sizeof(int*) * H);
		result = (char**)malloc(sizeof(char*) * H);
		for(int j = 0; j < H; j++)
		{
			map[j] = (int*)malloc(sizeof(int) * W);
			for(int k = 0; k < W; k++)
				in >> map[j][k];
			result[j] = (char*)calloc(sizeof(char) * W, 1);
		}
		char letter = 'a';

		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				vector<LatLon> v;
				int jj = j;
				int kk = k;
				while(1)
				{
					if(result[jj][kk] == 0)
					{
						int pos = choose(map, jj, kk, H, W);
						if(pos != -1)
						{
							LatLon ll;
							ll.y = jj;
							ll.x = kk;
							v.push_back(ll);
							if(pos == 0)
							{
								jj--;
							}
							else if(pos == 1)
							{
								kk--;
							}
							else if(pos == 2)
							{
								kk++;
							}
							else
							{
								jj++;
							}
						}
						else
						{
							result[jj][kk] = letter;
							for(int l = 0; l < (int)v.size(); l++)
							{
								LatLon ll = v[l];
								result[ll.y][ll.x] = letter;
							}
							letter++;
							break;
						}
					}
					else
					{
						for(int l = 0; l < (int)v.size(); l++)
						{
							LatLon ll = v[l];
							result[ll.y][ll.x] = result[jj][kk];
						}
						break;
					}
				}
			}
		}

		out << "Case #" << i + 1 << ":" << endl;
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				if(k != 0)
				{
					out << " ";
				}
				out << result[j][k];
			}
			out << endl;
		}

		for(int j = 0; j < H; j++)
		{
			free(map[j]);
			free(result[j]);
		}
		free(map);
		free(result);

	}

	out.flush();
}
