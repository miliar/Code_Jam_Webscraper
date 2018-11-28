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
int N, L, H;
vector<int> freq;

int main()
{
    fstream fin("C-small-attempt0.in",ifstream::in);
    fstream fout("C-small-attempt0.out",ofstream::out);
    fin >> T;
    for(int tcase=1;tcase<=T;tcase++)
    {
        fin >> N >> L >> H;
		freq.clear();
		freq.resize(N);
		rep(i, N) fin >> freq[i];
		bool ok = 1;
		for(int i=L;i<=H;++i)
		{
			bool ok2 = 1;
			rep(j, N)
			{
				if (freq[j]%i!=0 && i%freq[j]!=0) { ok2 = 0; break; }
			}
			if (ok2) 
			{
				fout << "Case #" << tcase << ": " << i << "\n";
				ok = 0;
				break;
			}
		}
		if (ok) fout << "Case #" << tcase << ": NO\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
