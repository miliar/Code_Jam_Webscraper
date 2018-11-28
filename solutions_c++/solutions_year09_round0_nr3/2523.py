#include<iostream>
#include<algorithm>
#include<list>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<math.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>

#define MIN(X,Y) (X < Y ? X : Y)
#define MAX(X,Y) (X > Y ? X : Y)
#define LENGTH(X) ((int)(X.length()))
#define SIZE(X) ((int)(X.size()))
#define SET(x,t) memset(x, t, sizeof(x))
#define FOR(i,x,y) for(int i = x; i < y; i++)

using namespace std;
fstream fin("C-small-attempt0.in", ios::in);
fstream fout("C-small.out", ios::out);

char welcome[] = "welcome to code jam";
string s;
int slen;
int count2;

void solve(int k1, int k2){
	if (k2 == 19){
		count2 ++;
		if (count2 == 10000)
			count2 = 0;
		return;
	}
	if (slen - k1 < 19 - k2)
		return;

	for (int i = k1; i < slen; i ++){
		if (s[i] == welcome[k2]){
			solve(i + 1, k2 + 1);
		}
	}
}

int main(){
	int n;
	fin >> n;
	getline(fin, s);
	for (int i = 0; i < n; i ++){
		count2 = 0;
		getline(fin, s);
		slen = s.length();
		fout << "Case #" << i + 1 << ": ";
		solve(0, 0);
		int res = count2;
		if (res < 10)
			fout << "000" << res;
		else if (res < 100)
			fout << "00" << res;
		else if (res < 1000)
			fout << "0" << res;
		else if (res < 10000)
			fout << res;
		else fout << res % 10000;
		fout << endl;
	}
	return 0;
}
