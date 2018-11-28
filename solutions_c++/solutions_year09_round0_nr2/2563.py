#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <string>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

#ifndef NOMINMAX
  #ifndef max
    #define max(a,b) (((a) > (b)) ? (a) : (b))
  #endif
  #ifndef min
    #define min(a,b) (((a) < (b)) ? (a) : (b))
  #endif
#endif 

#define read(a) { scanf("%d", &(a)); }
#define swap(a, b) { (a) ^= (b); (b) ^= (a); (a) ^= (b); }

#define MAX 101

int he[MAX][MAX];
int flow[MAX][MAX];
int sol[MAX][MAX];

int T, H, W;

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0,  1};

int cases = 0;

void do_case()
{
	printf("Case #%d:\n", cases+1);
	queue<pair<int,int>> q1;
	For(j, 0, H-1)
	For(i, 0, W-1)
	{
		int min = he[i][j];
		For(k, 0, 3)
		{
			int x = i + dx[k];
			int y = j + dy[k];
			
			if (x < 0 || x >= W || y < 0 || y >= H)
				continue;

			if(he[x][y] < min)
			{
				min = he[x][y];
				flow[i][j] = k;
			}
		}
		if (flow[i][j] == -1)
				q1.push(MP(i,j));
	}


	pair<int,int> p2 = MP(0, 0);
	while(sol[p2.first][p2.second] == -1 && flow[p2.first][p2.second] != -1)
	{
		sol[p2.first][p2.second] = 0;
		int x = p2.first;
		int y = p2.second;
		p2.first = x + dx[flow[x][y]];
		p2.second = y + dy[flow[x][y]];
	}

	sol[p2.first][p2.second] = 0;

	int n = 1; int an = 0;
	while (q1.size() > 0)
	{
		queue<pair<int,int>> q2;
		pair<int,int> pp = q1.front(); q1.pop();
		if (sol[pp.first][pp.second] != -1)
			an = 0;
		else
			an = n;
		q2.push(pp); 
		while (q2.size() > 0)
		{
			pair<int,int> p = q2.front(); q2.pop();
			sol[p.first][p.second] = an;
			
			For(k, 0, 3)
			{
				int x = p.first + dx[k];
				int y = p.second + dy[k];
				
				if (x < 0 || x >= W || y < 0 || y >= H)
					continue;
				
				int x2 = x + dx[flow[x][y]];
				int y2 = y + dy[flow[x][y]];

				if (x2 == p.first && y2 == p.second)
					q2.push(MP(x,y));
			}
		}
		if (an != 0)
			n++;
	}
	
	For(j, 0, H-1)
	{
		printf("%c", ('a' + sol[0][j]));
		//printf(" %2d", flow[0][j]);
		For(i, 1, W-1)
		{
			printf(" %c", ('a' + sol[i][j]));
			//printf(" %2d", flow[i][j]);
		}
		printf("\n");
	}
	cases++;
}

int main()
{
	read(T);
	For(cases, 0, T-1)
	{
		read(H); read(W);
		Fill(he, INT_MAX);
		Fill(flow, -1);
		Fill(sol, -1);
		For(j, 0, H-1)
		For(i, 0, W-1)
		{
			int num;
			read(num);
			he[i][j] = num;
		}
		do_case();
	}

	return 0;
}