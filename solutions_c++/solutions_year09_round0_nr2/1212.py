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

int n,H,W,t;
char cc = 'a';
vector<string> g;
vector< vector<int> > al;

bool ok(int r,int c)
{
	if (r>=0 && c>=0 && r<H && c<W) return 1;
	else return 0;
}

void go(int r,int c)
{
	g[r][c] = cc;
	int cm = 100000, c1 = -1, c2 = -1;
	if (ok(r-1,c) && al[r-1][c]<cm) { cm = al[r-1][c]; c1 = r-1; c2 = c; }
	if (ok(r,c-1) && al[r][c-1]<cm) { cm = al[r][c-1]; c1 = r; c2 = c-1; }
	if (ok(r,c+1) && al[r][c+1]<cm) { cm = al[r][c+1]; c1 = r; c2 = c+1; }
	if (ok(r+1,c) && al[r+1][c]<cm) { cm = al[r+1][c]; c1 = r+1; c2 = c; }
	if (cm<al[r][c] && g[c1][c2]=='.') go(c1,c2);
	if (ok(r-1,c) && g[r-1][c]=='.' && al[r-1][c]>al[r][c] &&
		(!ok(r-2,c) || al[r-2][c]>al[r][c]) && (!ok(r-1,c-1) || al[r-1][c-1]>al[r][c]) && (!ok(r-1,c+1) || al[r-1][c+1]>al[r][c])) go(r-1,c);
	if (ok(r,c-1) && g[r][c-1]=='.' && al[r][c-1]>al[r][c] &&
		(!ok(r,c-2) || al[r][c-2]>al[r][c]) && (!ok(r-1,c-1) || al[r-1][c-1]>al[r][c]) && (!ok(r+1,c-1) || al[r+1][c-1]>=al[r][c])) go(r,c-1);
	if (ok(r,c+1) && g[r][c+1]=='.' && al[r][c+1]>al[r][c] &&
		(!ok(r-1,c+1) || al[r-1][c+1]>al[r][c]) && (!ok(r,c+2) || al[r][c+2]>=al[r][c]) && (!ok(r+1,c+1) || al[r+1][c+1]>=al[r][c])) go(r,c+1);
	if (ok(r+1,c) && g[r+1][c]=='.' && al[r+1][c]>al[r][c] &&
		(!ok(r+2,c) || al[r+2][c]>=al[r][c]) && (!ok(r+1,c-1) || al[r+1][c-1]>=al[r][c]) && (!ok(r+1,c+1) || al[r+1][c+1]>=al[r][c])) go(r+1,c);

}

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> n;
    for(int j=1;j<=n;j++)
    {
		fin >> H >> W ;
		g.resize(H);
		al.resize(H);
		rep(i,H)
		{
			g[i].resize(W);
			al[i].resize(0);
			rep(k,W) { fin >> t; g[i][k] = '.'; al[i].push_back(t); }
		}
		t = 0;
		cc = 'a';
		while(1)
		{
			t = 0;
			for(t=0;t<W*H;t++)
			{
				if (g[t/W][t%W]=='.') break;
			}
			if (t==W*H) break;
			go(t/W,t%W);
			cc++;
		}
        fout << "Case #" << j << ":\n";
		rep(i,H)
		{
			rep(k,W)
			{
				fout << g[i][k] << " ";
			}
			fout << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
