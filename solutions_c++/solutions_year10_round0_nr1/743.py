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

long long N, K, t;


int main()
{
    fstream fin("A-large.in",fstream::in);
    fstream fout("A-large.out",fstream::out);
    fin >> t;
	long long per = 0;
    for(int j=1;j<=t;j++)
    {
        fin >> N >> K;
		per = (1<<N);
		if ((K+1)%per==0)
			fout << "Case #" << j << ": " << "ON\n";
		else fout << "Case #" << j << ": " << "OFF\n";
    }
    fin.close();
	fin.clear();
    fout.close();
	fout.clear();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
