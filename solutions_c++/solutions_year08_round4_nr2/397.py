#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <list>
#include <numeric>
#include <bitset>
#include <ext/algorithm>
#include <ext/numeric>
#include <fstream>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
typedef long long LL; using namespace std;

int n, m;
long long A;
long long area(int xa, int ya, int xb, int yb, int xc, int yc){
	return abs((long long)(xc - xa) * (long long)(yb - ya) - 
							(long long)(xb - xa) * (long long)(yc - ya));
}

int xx, yy;

bool possible(int a, int b, long long P){
	//(xc - xa) * (yb - ya) - (xb - xa) * (yc - ya)
	// and we are looking for  a * y - x * b = P
	// trying for each x
	long long pp;
	FOR (x, n + 1){
		pp = P + (long long)(x) * (long long)(b);
		if (a == 0){
			if (pp == 0LL && area(0, 0, a, b, x, m) == abs(P)){
				yy = m;
				xx = x;
				return true;
			}
		}
		else if (pp % a == 0 && pp / a >= 0 && pp / a <= m){
			yy = pp / a;
			xx = x;
			if (xx != a || yy != b)
				if (area(0, 0, a, b, xx, yy) == abs(P))
					return true;
		}
	}
	return false;
}


int main(){
	ifstream fin("Bs.in");
	ofstream fout("Bs.out");
	int tests, x1, y1;
	fin >> tests;
	FOR (test, tests){
		fin >> n >> m >> A;
		// one point is (0, 0), and try to find a second one
		bool found = false;
		FOR (i, n + 1){
			FOR (j, m + 1){
				if (i == 0 && j == 0)
					continue;
				if (possible(i, j, A) || possible(i, j, -A)){
					x1 = i;
					y1 = j;
					found = true;
					break;
				}
			}	
			if (found)
				break;
		}
		if (!found)
			fout << "Case #" << (test + 1) << ": IMPOSSIBLE" << endl;
		else{
			cout << area(0, 0, x1, y1, xx, yy) << " " << A << endl;
			fout << "Case #" << (test + 1) << ": 0 0 " << x1 << " " << y1 << " " << xx << " " << yy << endl;
		}
	}
	system("pause");
	return 0;
}
