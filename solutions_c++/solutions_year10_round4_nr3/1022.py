/*
Author : OmarEl-Mohandes
PROG   : C
LANG   : C++
*/
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <complex>
#include <valarray>
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define REP(i,k,m) for(int i=k;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)
int mat[108][108];
int mat2[108][108];
bool check()
{
	for (int i = 0; i < 108; ++i) {
		for (int j = 0; j < 108; ++j) {
			if(mat[i][j])return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("C.in" , "rt" , stdin);
	freopen("C.out" , "wt" , stdout);
	int t , r;
	scanf("%d" , &t);
	for (int c = 0; c < t; ++c) {
		memset(mat , 0 , sizeof mat);
		scanf("%d" , &r);
		int x1 , y1 , x2 , y2;
		for (int i = 0; i < r; ++i) {
			scanf("%d%d%d%d" , &y1 , &x1 , &y2 , &x2);
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					mat[x][y] = 1;
		}
		int res = 0;
		while(check())
		{
			res ++;
			memset(mat2 , 0 , sizeof mat2);
			for (int i = 0; i < 108; ++i) {
				for (int j = 0; j < 108; ++j) {
					if(mat[i][j] == 0 && (i-1 >= 0 && mat[i-1][j]) && (j-1 >= 0 && mat[i][j-1]))mat2[i][j] = 1;

					if(mat[i][j] == 1 && (i-1 < 0 || !mat[i-1][j]) && (j-1 < 0 || !mat[i][j-1]))mat2[i][j] = 0;
					else if(mat[i][j] == 1 )mat2[i][j] = 1;
				}
			}

			for (int i = 0; i < 108; ++i) {
				for (int j = 0; j < 108; ++j) {
					mat[i][j] = mat2[i][j];
				}
			}
		}
		printf("Case #%d: %d\n" , c+1 , res);
	}
	return 0;
}
