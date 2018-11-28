/* Rajat Goel [C++] */
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int    INF =     0x7FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      int64;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int grid[101][101],n,m;
char name[101][101],given;

int height(int r, int c) {
	if (r<0 ||r>n-1 || c<0 || c>m-1) return 10000001;
	return grid[r][c];
}

bool isSink(int r, int c) {
	if (height(r-1,c) >= height(r,c) &&
	    height(r+1,c) >= height(r,c) &&
	    height(r,c-1) >= height(r,c) &&
	    height(r,c+1) >= height(r,c))
		return true;
	return false;
}

char floodfill(int r, int c) {
	if (name[r][c]!=' ') return name[r][c];
	if (isSink(r,c)) { name[r][c] = given++; return name[r][c]; }
	int fr=r,fc=c;
	if (height(r-1,c) < height(fr,fc)) { 
		fr = r-1; fc = c;
	}
	if (height(r,c-1) < height(fr,fc)) { 
		fr = r; fc = c-1; 
	}
	if (height(r,c+1) < height(fr,fc)) {
	       	fr = r; fc = c+1;
	}
	if (height(r+1,c) < height(fr,fc)) {
	       	fr = r+1; fc = c;
	}
	name[r][c] = floodfill(fr,fc);
	return name[r][c];
}

int main() {
	int T;
	cin >> T;
	loop(cas, T){
		printf("Case #%d:\n", cas+1);
		cin >> n >> m;
		given='a';
		memset(name, ' ', sizeof(name));
		loop(i,n)loop(j,m)cin >> grid[i][j];
		loop(i,n)loop(j,m)floodfill(i,j);
		loop(i,n) {
			loop(j,m) cout << name[i][j] << " ";
			cout << endl;
		}
	}
	return 0;
}
