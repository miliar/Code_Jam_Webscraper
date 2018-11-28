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
int C, D, N;
vector<string> nbase;
vector<string> opp;
string invk;

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> t;
    for(int j=1;j<=t;j++)
    {
		nbase.resize(0);
		opp.resize(0);
		fin >> C;
		string tmps;
		rep(i,C) 
		{
			fin >> tmps;
			nbase.push_back(tmps);
		}
		fin >> D;
		rep(i,D) 
		{
			fin >> tmps;
			opp.push_back(tmps);
		}
		fin >> N;
		fin >> invk;
		string res;
		res.resize(0);
		rep(i,N)
		{
			res.push_back(invk[i]);
			bool fl = 0;
			int tind = res.size()-1;
			if (tind>0)
			{
				rep(k,C)
				{
					if ((res[tind-1]==nbase[k][0] && res[tind]==nbase[k][1])
						|| (res[tind-1]==nbase[k][1] && res[tind]==nbase[k][0]))
					{
						fl = 1;
						res = res.substr(0, tind-1);
						res.push_back(nbase[k][2]);
						break;
					}
				}
				if (!fl)
				{
					char tmpc = invk[i];
					rep(m,tind)
					{
						rep(k,D)
						{
							if ((res[m]==opp[k][0] && res[tind]==opp[k][1])
								|| (res[m]==opp[k][1] && res[tind]==opp[k][0]))
							{
								fl = 1;
								res.resize(0);
								break;
							}
						}
						if (fl) break;
					}
				}
			}
		}
        fout << "Case #" << j << ": [" ;
		if (res.size()>0) rep(i, res.size()-1) fout << res[i] << ", ";
		if (res.size()>0) fout << res[res.size()-1] << "]\n";
		else fout << "]\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << " s\n";
    system("PAUSE");
    return 0;
}
