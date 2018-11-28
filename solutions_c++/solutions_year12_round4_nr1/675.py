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
int D;
int N;
vector< vector<int> > pr;
vector<int> maxuns;

int conn(int r1, int i1, int i2)
{
	int r2 = pr[i2][0] - pr[i1][0];
	if (r1-r2<0) return -1;
	return 1;
}

int solve(int r, int st)
{
	if (maxuns[st]>=r) return 0;
	if (pr[st][0]+r>=D) return 1;
	int ret = 0;
	for(int i=st+1;i<N;++i)
				if (conn(r, st, i)>0)
				{
					ret = solve(min(pr[i][1], pr[i][0]-pr[st][0]), i);
					if (ret) return 1;
				}
	maxuns[st] = r;
	return 0;
}

int main()
{
    fstream fin("A-small-attempt1.in",ifstream::in);
    fstream fout("A-small-attempt1.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
		fin >> N;
		pr.resize(N);
		maxuns.resize(N);
		rep(i, N)
		{
			pr[i].resize(2);
			fin >> pr[i][0] >> pr[i][1];
			maxuns[i] = 0;
		}
		fin >> D;
		if (solve(pr[0][0],0))
			{
				fout << "Case #" << j << ": " << "YES\n";
			}
		else
			{
				fout << "Case #" << j << ": " << "NO\n";
			}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
