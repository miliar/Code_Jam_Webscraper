#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;


typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef long long LL;

#define swap(x, y) (x) ^= (y) ^= (x) ^= (y)
#define FOR(i, L, U)		for(int i=L; i<=U; i++)
#define EPS 1e-9

typedef struct {
	int left, right;
} LINE;

LINE line[1010];
int N;


int Process()
{	
	int i, j, seen = 0;

	FOR(i, 1, N)
		FOR(j, i+1, N) 
			if((line[i].left < line[j].left && line[i].right > line[j].right) || (line[i].left > line[j].left && line[i].right < line[j].right))
				seen++;

	return seen;
}

int main()
{
	freopen("E:\\A-large.in", "r", stdin);
	freopen("E:\\output.txt", "w", stdout);



	int TC, tcase;
	int i, j, k, seen;
	
	cin >> TC;

	FOR(tcase, 1, TC) {
		cin >> N;

		FOR(i, 1, N) 
			cin >> line[i].left >> line[i].right;
		
		seen = Process();

		printf("Case #%d: %d\n", tcase, seen);
	}


	return 0;
}