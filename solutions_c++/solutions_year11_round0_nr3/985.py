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
vector<int> C;

int main()
{
    fstream fin("C-large.in",ifstream::in);
    fstream fout("C-large.out",ofstream::out);
    fin >> t;
    for(int j=1;j<=t;j++)
    {
		C.resize(0);
		int re = 0;
		bool flr = 1;
		fin >> N;
		int tmpn;
		rep(i,N)
		{
			fin >> tmpn;
			C.push_back(tmpn);
		}
		sort(C.begin(), C.end());
		int s1 = C[0];
		int s2 = C[1];
		rep(i, N-2) s2 ^= C[i+2];
		if (s1!=s2) fout << "Case #" << j << ": NO\n";
        else 
		{
			re = 0;
			rep(i, N-1) re += C[i+1];
			fout << "Case #" << j << ": " << re << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << " s\n";
    system("PAUSE");
    return 0;
}
