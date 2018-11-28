#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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
#include <fstream>
using namespace std;
template<class T> inline const T& max(const T& a, const T& b){return a > b ? a : b;}
template<class T> inline const T& min(const T& a, const T& b){return a < b ? a : b;}
template<class T> inline T sqr(const T a) {return a * a;}
const double PI = acos(-1);

char engine[120][120];
char query[1020][120];

ofstream fout("out.txt");

int getAnswer()
{
	int ret = 0;
	int  numEngine;
	int  numQuery;
	scanf("%d", &numEngine); getchar();
	int i, j;
	for (i=0; i<numEngine; ++i) gets(engine[i]);
	scanf("%d", &numQuery); getchar();
	for (i=0; i<numQuery; ++i) gets(query[i]);
	
	int last = -1;
	bool used[120] = {0};
	for (i=0; i<numQuery; ++i) {
		for (j=0; j<numEngine; ++j) {
			if (strcmp(query[i], engine[j]) == 0) {
				used[j] = true;
				last = j;
				break;
			}
		}
		for (j=0; j<numEngine; ++j) {
			if (!used[j]) break;
		}
		if (j == numEngine) {
			++ret;
			memset(used, 0, sizeof used);
			used[last] = true;
		}
	}
	return ret;
}

int main()
{
	int test;
	scanf("%d", &test);
	int t;
	for (t=1; t<=test; ++t)
	{
		int ret = getAnswer();
		fout << "Case #" << t << ": " << ret << endl;
		cout << "Case #" << t << ": " << ret << endl;
	}

	return 0;
}
