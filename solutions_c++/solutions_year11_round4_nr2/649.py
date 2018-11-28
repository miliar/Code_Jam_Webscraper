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
int R, C, D;
vector< vector<int> > mass;
string tmp;

int main()
{
    fstream fin("B-small-attempt0.in",ifstream::in);
    fstream fout("B-small-attempt0.out",ofstream::out);
    fin >> T;
    for(int tcase=1;tcase<=T;tcase++)
    {
		//cout << tcase << "\n";
		fin >> R >> C >> D;
		mass.resize(R);
		rep(i, R) mass[i].resize(C);
		rep(i, R)
		{
			fin >> tmp;
			rep(j, C) mass[i][j] = D + (int)(tmp[j]-'0');
		}
		int re = 0;
		bool fl = 0;
		for(re=min(R,C);re>=3;--re)
		{
			rep(i, R-re+1)
			{
				rep(j, C-re+1)
				{
					int xmas = 0.;
					int ymas = 0.;
					rep(k, re)
						rep(m, re)
						if (!(k==0 && m==0) && !(k==re-1 && m==0) && !(k==0 && m==re-1) && !((k==re-1) && (m==re-1)))
						{
							xmas += (2*k - (re-1)) * mass[i+k][j+m];
							ymas += (2*m - (re-1)) * mass[i+k][j+m];
						}
					if (xmas==0 && ymas==0)
					{
						fl = 1;
						fout << "Case #" << tcase << ": " << re << "\n";
						cout << "Case #" << tcase << ": " << re << "\n";
					}
					if (fl) break;
				}
				if (fl) break;
			}
			if (fl) break;
		}
		if (!fl)
		{
			fout << "Case #" << tcase << ": " << "IMPOSSIBLE" << "\n";
			cout << "Case #" << tcase << ": " << "IMPOSSIBLE" << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
