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

int t;
int N;
vector<string> play;
vector<int> wins;
vector<int> games;
vector<double> WP;
vector<double> OWP;
vector<double> OOWP;

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> t;
    for(int j=1;j<=t;j++)
    {
        fin >> N;
		play.resize(N);
		wins.resize(N);
		games.resize(N);
		WP.resize(N);
		OWP.resize(N);
		OOWP.resize(N);
		rep(i, N)
			fin >> play[i];
		rep(i, N)
		{
			wins[i] = games[i] = 0;
			rep(k, N)
			{
				if (play[i][k]!='.') games[i]++;
				if (play[i][k]=='1') wins[i]++;
			}
			WP[i] = (double)(wins[i]) / games[i];
		}

		int twi, tga;
		int nopp;
		
		rep(i, N)
		{
			nopp = 0;
			OWP[i] = 0.;
			rep(k, N)
			{
			if (i!=k)
			{
				twi = wins[k];
				tga = games[k];
				if (play[i][k]!='.') { tga--; nopp++; }
				if (play[i][k]=='0') twi--;
				if (play[i][k]!='.') OWP[i] += (double)(twi) / tga;
			}		
			}
			OWP[i] /= nopp;
		}

		rep(i, N)
		{
			nopp = 0;
			OOWP[i] = 0.;
			rep(k, N)
			{
			if (i!=k)
			{
				if (play[i][k]!='.')
				{
					nopp++;
					OOWP[i] += OWP[k];
				}
			}
			}
			OOWP[i] /= nopp;
		}

		fout << "Case #" << j << ":\n";
		rep(i, N)
		{
			fout << 0.25 * WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
