#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include "combination.h"
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

class coord
{
public:
	int64 x,y;
};

int main() 
{
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	int t;
	in>>t;
	For(test, 1, t) {
		int64 result = 0;
		int power;
		int64 n,a,b,c,d,x0,y0,m;
		vector<coord>coords;
		vector<int64>coordsPose;
		in>>n>>a>>b>>c>>d>>x0>>y0>>m;
		coord x;
		x.x = x0;x.y = y0;
		coords.push_back(x);
		coordsPose.push_back(1);
		for( int64 i = 1; i < n; i++ )
		{
			x.x = (a * x.x + b) % m;
			x.y = (c * x.y + d) % m;
			coords.push_back(x);
			coordsPose.push_back(i+1);
		}
		vector<int64>t;
		t.push_back(1);
		t.push_back(2);
		t.push_back(3);
		do
		{
		   int64 x = (coords[t[0]-1].x+coords[t[1]-1].x+coords[t[2]-1].x)%3;
		   int64 y = (coords[t[0]-1].y+coords[t[1]-1].y+coords[t[2]-1].y)%3;
		   if ( x == 0 && y == 0  )
		   {
			   result++;
				continue;
		   }


		}
		while(stdcomb::next_combination(coordsPose.begin(),coordsPose.end(),t.begin(),t.end() ));

		out<<"Case #"<<test<<": "<<result<<endl;
	}

	exit(0);
}