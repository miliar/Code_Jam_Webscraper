#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 



vector<int> freq;

typedef unsigned int uint;
uint N,K,L,P;

void read_data(ifstream& ifs)
{
	freq.clear();
	ifs >> P >> K >> L;
	uint tmp;
	REP(i,L)
	{
		ifs >> tmp;
		freq.push_back(tmp);
	}
};

void print_data()
{
	cout << P << "\t" << K << "\t" << L << endl;
	REP(i,L)
		cout << freq[i] << "\t";
	cout << endl;
};

//bool greater(uint a, uint b){ return a > b; };

uint compute_strokes()
{
	uint res = 0;
	sort(ALL(freq),greater<uint>());
	REP(i,freq.size())
		res += freq[i]*(i/K+1);
	return res;
};

int main(int argc, char* argv[])
{
	ifstream in(argv[1]);

	in >> N;
	REP(i,N)
	{
		read_data(in);
		//print_data();
		cout << "Case #" << i+1 << ": " << compute_strokes() << endl;
	};
	return 0;
};
