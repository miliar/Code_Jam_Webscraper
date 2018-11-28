#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

long long C, R;
int cell[1000][1000][2];
int maxx, maxy, minx, miny;
int X1,X2,Y1,Y2;
long long t;

bool isempty(int tm)
{
	for(int i=1;i<=maxx;i++)
		for(int j=1;j<=maxy;j++)
			if (cell[i][j][tm%2]==1) return 0;
	return 1;
}

int main()
{
    fstream fin("C-small-attempt0.in",fstream::in);
    fstream fout("C-small-attempt0.out",fstream::out);
    fin >> C;
	long long per = 0;
	string tmp;
    for(int j=1;j<=C;j++)
    {
		memset(cell,0, sizeof(cell));
		fin >> R;
		minx = 1;
		maxx = 1;
		miny = 1;
		maxy = 1;
		rep(i, R)
		{
			fin >> X1 >> Y1 >> X2 >> Y2;
			maxx = max(maxx, X2);
			//minx = min(minx, X1);
			maxy = max(maxy, Y2);
			//miny = min(miny, Y1);
			for(int i=X1;i<=X2;++i)
				for(int j=Y1;j<=Y2;++j)
				{
					cell[i][j][0] = 1; 
				}
		}
			t = 0;
			while (!isempty(t))
			{
				for(int i=1;i<=maxx+1;i++)
					for(int j=1;j<=maxy+1;j++)
					{
						if (cell[i][j][t%2]==1)
						{
							if (cell[i-1][j][t%2]==1 || cell[i][j-1][t%2]==1) cell[i][j][1-t%2]=1;
							else cell[i][j][1-t%2]=0;
						}
						else
						{
							if (cell[i-1][j][t%2]==1 && cell[i][j-1][t%2]==1) cell[i][j][1-t%2]=1;
							else cell[i][j][1-t%2]=0;
						}
					}
				maxx++;
				maxy++;
				t++;
			}
		fout << "Case #" << j << ": " << t << "\n";
    }
    fin.close();
	fin.clear();
    fout.close();
	fout.clear();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}