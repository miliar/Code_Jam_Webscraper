/*
ID: zinking1
PROG: Snapper chain
LANG: C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef  long long int64;
typedef  vector<int64> VI;

struct segment{
	int x1;
	int x2;
	segment( int xx1, int xx2):x1(xx1),x2(xx2){}
	bool intersect( segment& r ){
		return (x1-r.x1)*(x2-r.x2) < 0;
	}
};

typedef vector<segment> VS;

int getIntersections( VS& v){
	int total = 0;
	int n=v.size();
	for( int i=0; i<n; i++ ){
		for( int j=i+1; j<n; j++ ){
			if( v[i].intersect(v[j]) ) total++;
		}
	}

	return total;
}

int main() {
	ifstream ifile("A-large.in");
	ofstream ofile("A-large.out");

	int tc = 0;
	
	ifile >> tc;
	for( int i=0; i<tc; i++ ){
		VS vc;
		int segments = 0;
		ifile >> segments;
		for( int j=0; j<segments; j++ ){
			int xx1 =0, xx2 = 0;
			ifile >>  xx1 >> xx2;
			segment s(xx1,xx2);
			vc.push_back( s );
		}
		ofile <<"Case #" << i+1 << ": "<< getIntersections( vc ) << endl;
	}
	

	return 0;


}