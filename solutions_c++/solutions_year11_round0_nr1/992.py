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

vector<int> Ost,Bst;
vector<int> dr;
int N;

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> t;
    for(int j=1;j<=t;j++)
    {
		Ost.resize(0);
		Bst.resize(0);
		dr.resize(0);
		fin >> N;
		char tmp;
		int tnumb;
		int re = 0;
		rep(i,N)
		{
			fin >> tmp >> tnumb;
			if (tmp=='O')
			{
				dr.push_back(0);
				Ost.push_back(tnumb);
			}
			else
			{
				dr.push_back(1);
				Bst.push_back(tnumb);
			}
		}
		Ost.push_back(1);
		Bst.push_back(1);
		int t1, t2, pos;
		int p1 = 1;
		int p2 = 1;
		t1 = t2 = 0;
		t1 = abs(p1-Ost[0])+1;
		t2 = abs(p2-Bst[0])+1;
		pos = 0;
		while (pos<N)
		{
			if (dr[pos]==0)
			{
				re += t1;
				t2 = max(t2-t1, 1);
				p1 = Ost[0];
				Ost.erase(Ost.begin());
				t1 = abs(p1-Ost[0])+1;
			}
			else
			{
				re += t2;
				t1 = max(t1-t2, 1);
				p2 = Bst[0];
				Bst.erase(Bst.begin());
				t2 = abs(p2-Bst[0])+1;
			}
			pos++;
		}
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
