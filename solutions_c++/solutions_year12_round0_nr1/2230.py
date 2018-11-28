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

int chmap[300];

int main()
{
    fstream fin("A-small-attempt0.in",ifstream::in);
    fstream fout("A-small-attempt0.out",ofstream::out);
	chmap[' '] = ' ';
	chmap['a'] = 'y';
	chmap['b'] = 'h';
	chmap['c'] = 'e';
	chmap['d'] = 's';
	chmap['e'] = 'o';
	chmap['f'] = 'c';
	chmap['g'] = 'v';
	chmap['h'] = 'x';
	chmap['i'] = 'd';
	chmap['j'] = 'u';
	chmap['k'] = 'i';
	chmap['l'] = 'g';
	chmap['m'] = 'l';
	chmap['n'] = 'b';
	chmap['o'] = 'k';
	chmap['p'] = 'r';
	chmap['q'] = 'z';
	chmap['r'] = 't';
	chmap['s'] = 'n';
	chmap['t'] = 'w';
	chmap['u'] = 'j';
	chmap['v'] = 'p';
	chmap['w'] = 'f';
	chmap['x'] = 'm';
	chmap['y'] = 'a';
	chmap['z'] = 'q';
    fin >> T;
	char cc[400];
	fin.getline(cc, 400);
    for(int j=1;j<=T;j++)
    {
		fin.getline(cc, 400);
		for(int i=0;cc[i];++i)
			cc[i] = chmap[cc[i]];
        fout << "Case #" << j << ": " ;
		for(int i=0;cc[i];++i) fout << cc[i];
		fout << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
