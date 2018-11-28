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

int T;
vector<string> tiles;
int R, C;

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> T;
    for(int tcase=1;tcase<=T;tcase++)
    {
        fin >> R >> C;
		tiles.resize(R);
		rep(i, R)
			fin >> tiles[i];

		bool ok = 1;
			rep(i, R)
			{
				rep(j, C)
				{
					if (tiles[i][j]=='#')
					{
						if (j==tiles[i].size()-1 || tiles[i][j+1]!='#') { ok = 0; continue; }
						if (i==tiles.size()-1 || tiles[i+1][j]!='#') { ok = 0; continue; }
						if (tiles[i+1][j+1]!='#') { ok = 0; continue; }
						tiles[i][j] = tiles[i+1][j+1] = '/';
						tiles[i][j+1] = tiles[i+1][j] = '\\';
					}
				}
				if (!ok) break;
			}
		if (ok)
		{
			fout << "Case #" << tcase << ":\n"; 
			rep(i, R)
			{
				fout << tiles[i] << "\n";
			}
		}
		else fout << "Case #" << tcase << ":\n" << "Impossible\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
