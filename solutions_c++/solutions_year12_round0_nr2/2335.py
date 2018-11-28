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
int N, S, p;
vector<int> sc;

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
		sc.resize(0);
		fin >> N >> S >> p;
		int tmps;
		rep(i, N) 
		{
			fin >> tmps;
			sc.push_back(tmps);
		}
		sort(sc.begin(), sc.end());
		int tus, tss;
		int ret = 0;
		for(int i=sc.size()-1;i>=0;--i)
		{
			tus = (sc[i]+2) / 3;
			tss = (sc[i]+4) / 3;
			if (tus>=p)
			{
				ret++;
			}
			else if (S>0 && tss>=p && sc[i]<=28 && sc[i]>=2)
			{
				ret++;
				S--;
			}
		}
        fout << "Case #" << j << ": " << ret << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
