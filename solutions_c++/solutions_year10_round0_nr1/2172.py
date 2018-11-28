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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it!=(v).end(); ++it)
int atoi(string &x) { stringstream ss(x); int temp; ss>>temp; return temp;}
string itoa(int i) { stringstream ss; ss<<i; return ss.str();}

ifstream fin;
ofstream fout;

void solve(int c)
{
	int N, K;
	fin >> N >> K;
	int power = (1 << N);
	if (K % power == power - 1)
		fout << "Case #" << c << ": ON" << endl;
	else
		fout << "Case #" << c << ": OFF" << endl;
}

int main() {
	fin.open("A-large.in");
	fout.open("A-large.out");

	int numCases;
	fin >> numCases;
	for (int c=1; c<=numCases; c++)
		solve(c);

	fin.close();
	fout.close();
	return 0;
}

