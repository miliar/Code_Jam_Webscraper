
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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define all(c)                 (c).begin(),(c).end()
#define forc(i,c)              for(int i=0;i<(c).size();i++)
#define F0R(i,N)               for(int i=0;i<N;++i)
#define forn(i,x,n)            for(int i=x;i<=(n);i++)

/// end of templates & utils


bool cmp( int a, int b ) {
   return a > b;
 }

int func(ifstream &line) {
	int cnt;
	line >> cnt;
	vector<int> x;
	vector<int> y;

	F0R(i,cnt) {
		int xx;
		line >> xx;
		x.push_back(xx);
	}

	F0R(i,cnt) {
		int yy;
		line >> yy;
		y.push_back(yy);
	}

	sort(x.begin(), x.end());
	sort(y.begin(), y.end(), cmp);

	int sum = 0;
	forc(i,x) {
		int xxx = x[i];
		int yyy = y[i];
		sum += (x[i] * y[i]);
	}

	return sum;
}

int main()
{
	ifstream infile("A-small.in");
	ofstream outfile("A-small.out", ios::out);

	int fileLen = 0;
	infile >> fileLen;
	for (int i = 0; i < fileLen; i++) {
		outfile << "Case #" << i+1 << ": " << func(infile) << endl;
	}

	outfile.close();

	return 0;
}
//---------------------------------------------------------------------------

