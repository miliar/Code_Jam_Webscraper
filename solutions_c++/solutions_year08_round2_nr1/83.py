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

int main(){
	ifstream fin("As.in");
	ofstream fout("As.out");
	int tests, n;
	long long x0, y0, A, B, C, D, M;
	fin >> tests;
	FOR (test, tests){
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long x[n], y[n];
		x[0] = x0;
		y[0] = y0;
		FOR (i, n - 1){
		  x[i + 1] = (A * x[i] + B) % M;
		  y[i + 1] = (C * y[i] + D) % M;
		}

		int ret = 0;
		FOR (i, n)
			ffor (j, i + 1, n)
				ffor (k, j + 1, n)
					if ((x[i] + x[j] + x[k]) % 3 == 0)
						if ((y[i] + y[j] + y[k]) % 3 == 0)
							ret++;
		fout << "Case #" << (test + 1) << ": " << ret << endl;
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}
