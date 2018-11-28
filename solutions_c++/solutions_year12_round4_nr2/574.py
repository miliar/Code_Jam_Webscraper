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
int N, W, L;
vector< int > rad;
vector< pair<int, int> > radus;
vector< pair<int, int> > crd;
vector<int> crdx;
vector<int> ma;

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
        fin >> N >> W >> L;
		rad.resize(N);
		radus.resize(N);
		rep(i,N) 
		{
			fin >> rad[i];
			radus[i] = make_pair(rad[i], i);
		}
		sort(radus.begin(), radus.end());
		reverse(radus.begin(), radus.end());
		rep(i, N) rad[i] = radus[i].first;
		ma.resize(N);
		rep(i, N) ma[radus[i].second] = i;
		int st = 0;
		int cc = 0;
		crdx.resize(0);
		crd.resize(0);
		while (st<N)
		{
			if (st==0)
			{
				//if (rad[0]<W)
				{
					crd.push_back(make_pair(0,0));
					st++;
					cc = rad[0];
					crdx.push_back(0);
					continue;
				}
				/*else
				{
					fout << "Case #" << j << ": " << "-1\n";
					break;
				}*/
			}
			if (cc+rad[st]>W) break;
			crd.push_back(make_pair(cc+rad[st], 0));
			crdx.push_back(cc + rad[st]);
			cc += 2*rad[st];
			st++;
		}
		if (st==N)
		{
			fout << "Case #" << j << ": ";
			rep(i,N) fout << crd[ma[i]].first << "\t" << crd[ma[i]].second << "\t";
			fout << "\n";
			//fout << W << "\t" << L << "\n";
			continue;
		}
		int curind = 0;
		int cy = rad[curind];
		while (st<N)
		{
			if (curind>=crdx.size())
			{
				fout << "Case #" << j << ": " << "-1\n";
				break;
			}
			if (cy+rad[st]>L)
			{
				curind++;
				cy = rad[curind];
				continue;
			}
			crd.push_back(make_pair(crd[curind].first, cy + rad[st]));
			cy += 2*rad[st];
			st++;
		}
		if (st==N)
		{
			fout << "Case #" << j << ": ";
			rep(i,N) fout << crd[ma[i]].first << "\t" << crd[ma[i]].second << "\t";
			fout << "\n";
			//fout << W << "\t" << L << "\n";
		}
		//fout << "Case #" << j << ": " << tms[N-1][M-1] << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
