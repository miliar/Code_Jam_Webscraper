#define ONLINE_JUDGE
//#define GenerateTest

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <cmath>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <string>
#include <stack>
#include <list>
#include <sstream>
#include <hash_set>
#include <hash_map>

#include "BigInteger\cbignum.h"

using namespace std;
#pragma comment(linker, "/STACK:64777216")

typedef long long LL;
typedef unsigned long long ULL;
typedef cBigNumber cLL;
const int size = 102;
void Solve()
{
	int tests;
	cin >> tests;
	for(int number_test = 0;number_test < tests;++number_test)
	{
		cout << "Case #" << number_test + 1 << ": "; 
		int R;
		cin >> R;
		int v[2][size][size];
		memset(v,0,sizeof(v)); 
		for(int i = 0;i < R;++i)
		{
			int x1,x2,y1,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(int x = x1;x <= x2;++x)
			{
				for(int y = y1;y <= y2;++y)
				{
					v[0][y][x] = 1;
				}
			}
		}
		int res = 0;
		for(;;)
		{
			bool is = false;
			int curr = res % 2;
			int next = !curr;
			for(int i = 0;i < size;++i)
				for(int j = 0;j < size;++j)
				{
					if(v[curr][i][j])
					{
						is = true;
					}
				}
			if(!is)
				break;
			++res;
			memset(v[next],0,sizeof(int) * size * size);
			for(int y = 1;y < size - 1;++y)
			{
				for(int x = 1;x < size - 1;++x)
				{
					if(v[curr][y][x] && (v[curr][y - 1][x] || v[curr][y][x - 1]))
					{
						v[next][y][x] = 1;
					}
					if(!v[curr][y][x]  && v[curr][y - 1][x] && v[curr][y][x - 1])
					{
						v[next][y][x] = 1;
					}
				}
			}
		}
		cout << res << endl;
	}
}

int main()
{
#ifdef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);

	freopen("output.txt", "wt", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
//	freopen("output.txt", "wt", stdout);
	
#ifdef GenerateTest
	
	freopen("output.txt", "wt", stdout);

#endif

	clock_t start = clock();
#endif

	Solve();	

#ifndef ONLINE_JUDGE 
	clock_t end = clock();
	cout <<"\n\nTime: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
#endif
	return 0;
}