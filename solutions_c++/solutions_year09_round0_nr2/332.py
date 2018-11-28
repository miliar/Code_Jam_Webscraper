#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int map[100][100];
char result[100][100];

int hDirection[4] = {-1,0,0,1};
int wDirection[4] = {0,-1,1,0};

void solve(int caseNum)
{
	char currentLetter = 'a';
	int h, w;
	fin >> h >> w;
	for (int i=0; i<h; i++)
	{
		for (int j=0; j<w; j++) 
		{
			fin >> map[i][j];
			result[i][j] = ' ';
		}
	}
	for (int i=0; i<h; i++)
	{
		for (int j=0; j<w; j++) 
		{
			if (result[i][j] == ' ') 
			{
				int x = i, y = j;
				for (;;)				
				{
					bool flag = false;
					int smallAltitude = map[x][y];
					int minx =x, miny=y;
					for (int k=0; k<4; k++) {
						int hh = x+hDirection[k];
						int ww = y+wDirection[k];
						if (hh >= 0 && ww >= 0 && hh < h && ww < w && map[hh][ww] < smallAltitude) {
							smallAltitude = map[hh][ww];
							minx = hh;
							miny = ww;
							flag = true;
						}
					}
					if (!flag)
						break;
					x = minx;
					y = miny;
				}
				if (result[x][y] == ' ')
					result[x][y] = result[i][j] = currentLetter++;
				else
					result[i][j] = result[x][y];
			}
		}
	}
	fout << "Case #" << caseNum << ":" << endl;
	for (int i=0; i<h; i++)
	{
		for (int j=0; j<w; j++)
			fout << result[i][j] << " ";
		fout << endl;
	}
}

int main() 
{
	int T;
	fin >> T;
	for (int i=1; i<=T; i++) 
		solve(i);
	fin.close();
	fout.close();
}