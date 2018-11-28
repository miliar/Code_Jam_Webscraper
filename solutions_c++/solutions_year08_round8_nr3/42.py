# include <cstdio>
# include <cstdlib>
# include <set>
# include <map>
# include <vector>
# include <algorithm>
# include <cmath>
# include <fstream>
# include <iomanip>
# include <sstream>
# include <string>
# include <iostream>

using namespace std;

ifstream fin ("input.txt");
ofstream fout ("output.txt");


int to [1024][1042];
long long cnt [1024][1042];

bool ok = true;
int k ;

long long res = 1;

void dfs (int num, int prev) {


	long long rest = k - to [prev][0];

	for (int i = 1; i <= to[num][0]; ++ i)
		if (to [num][i] != prev) {
		
			if (rest == 0){
				res = 0;
				return ;
			}
			res = (res * (rest)) % 1000000009;

			-- rest;

			dfs (to [num][i], num);
		}
}

int main () {


	int tests; 

	fin >> tests;
	for (int test = 1; test <= tests; ++ test) {

		int n;

		fin >> n >> k;

		int x, y;

		for (int i = 1; i <= n; ++ i) to[i][0] = 0;

		for (int i = 0; i < n - 1; ++ i) {
		
			fin >> x >> y;

			to [x][ ++ to [x][0]] = y;

			to [y][++ to [y][0]] = x;
		}

		res = 1;

		for (int i = 1; i <= to [1][0]; ++ i) {		
			res *= (k - i + 1);
			res %= 1000000009;
		}

		for (int i = 1; i <= to [1][0]; ++ i) {
		
			dfs (to[1][i], 1);
		}
	
		fout << "Case #" << test << ": " << res << endl; 

	}

	return 0;
}
