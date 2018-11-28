#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define pb push_back
#define SIZE(x) ((int)(x.size()))
#define LENGTH(x) ((int)(x.length()))
#define PI 3.14159265358979323846264338327950288

typedef long long ll;
typedef unsigned long long ull;
int TS,R,C;
char matrix[60][60];

inline bool can(){
	for (int i=0; i<R; ++i) {
		for (int j=0; j<C; ++j) {
			if (matrix[i][j]=='#' && i+1<R && j+1<C && matrix[i+1][j]=='#' && matrix[i][j+1]=='#' && matrix[i+1][j+1]=='#') {
				matrix[i][j]='/';
				matrix[i][j+1]='\\';
				matrix[i+1][j]='\\';
				matrix[i+1][j+1]='/';
				return true;
			}
		}
	}
	return false;
}

int main(){
	cin>>TS;
	for (int testId=1; testId<=TS; ++testId) {
		bool did=true;
		cin>>R>>C;
		getchar();
		for (int i=0; i<R; ++i) {
			for (int j=0; j<C; ++j) {
				matrix[i][j]=getchar();
				if (matrix[i][j]=='#')did=false;
			}
			getchar();
		}
		
		while (can()) {
			did=true;
		}
		cout<<"Case #"<<testId<<":"<<endl;
		for (int i=0; i<R; ++i) {
			for (int j=0; j<C; ++j) {
				if (matrix[i][j]=='#')did=false;
			}
		}
		if (!did)cout<<"Impossible"<<endl;
		else {
			for (int i=0; i<R; ++i) {
				for (int j=0; j<C; ++j) {
					cout << matrix[i][j];
				}
				cout << endl;;
			}
		}

		
	}
	return 0;
}
