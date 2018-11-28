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

int n,T;
int re;
int cma[50];
string t;

int go()
{
	int ci=-1;
	rep(i,n)
		if (cma[i]>i) { ci=i; break; }
	if (ci==-1) return 0;
	int ci2=-1;
	for(int i=ci+1;i<n;i++)
		if (cma[i]<=ci) { ci2=i; break; }
	for(int i=ci2;i>ci;i--)
	{
		swap(cma[i],cma[i-1]);
		re++;
	}
	return 1;
}

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
		re = 0;
		fin >> n;
		rep(i,50) cma[i] = 0;
		rep(i,n)
		{
			fin >> t;
			rep(j,n) { if (t[j]=='1') cma[i] = j; }
		}
		while (go());
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
