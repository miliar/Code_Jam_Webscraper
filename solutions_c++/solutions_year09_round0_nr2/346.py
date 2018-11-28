/*
 * B.cpp
 *
 *  Created on: 03/09/2009
 *      Author: Hamzawy
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
#include <complex>
/*#include <ext/hash_map>
 using namespace __gnu_cxx;*/
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define EPS (1e-9)
#define SIZE 100000

struct DisjointSets {

	int parent[SIZE], rank[SIZE], componentsCnt;

	DisjointSets(int n) {
		memset(rank, 0, n * sizeof(rank[0]));
		for (int i = 0; i < n; i++)
			parent[i] = i;
		componentsCnt = n;
	}

	int find(int e) {
		return parent[e] == e ? e : parent[e] = find(parent[e]);
	}

	void join(int e1, int e2) {
		int p1 = find(e1), p2 = find(e2);
		if (p1 == p2)
			return;
		if (rank[p1] == rank[p2])
			rank[p1]++;
		if (rank[p2] > rank[p1])
			swap(p1, p2);
		parent[p2] = p1;
		componentsCnt--; // new components get merged
	}
};

int arr[101][101];
char out[101][101];
int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0 };

int main() {
#ifndef ONLINE_JUDGE
	//freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
#endif
	int t, x, y;
	scanf("%d", &t);
	for (int T = 0; T < t; T++) {
		scanf("%d%d", &x, &y);
		for (int i = 0; i < x; i++)
			for (int j = 0; j < y; j++)
				scanf("%d", arr[i] + j);
		DisjointSets d(x * y);
		for (int i = 0; i < x; i++)
			for (int j = 0; j < y; j++) {
				int nx, ny, mn = OO, mni = -1;
				for (int k = 0; k < 4; k++) {
					nx = i + dx[k];
					ny = j + dy[k];
					if (nx >= 0 && ny >= 0 && nx < x && ny < y && arr[nx][ny]
							< arr[i][j] && arr[nx][ny] < mn)
						mn = arr[nx][ny], mni = k;
				}
				if (mni != -1)
					d.join(i * y + j, (i + dx[mni]) * y + j + dy[mni]);
			}
		char st = 'a';
		for(int i=0;i<x*y;i++)
			d.find(i);
		for (int i = 0; i < x; i++)
			for (int j = 0; j < y; j++) {
				bool f = 0;
				char xxx=0;
				for (int p = 0; (p < (i * y + j) )&& !f; p++) {
					int k = p / y, l = p % y;
					if (d.find(i * y + j) == d.find(k * y
							+ l))
						f = 1, xxx = out[k][l];
				}
				if (f)
					out[i][j] = xxx;
				else
					out[i][j] = st++;
			}
		//if (T)
			//printf("\n");
		printf("Case #%d:", T + 1);
		for (int i = 0; i < x; i++) {
			printf("\n");
			for (int j = 0; j < y; j++)
				printf(j ? " %c" : "%c", out[i][j]);
		}
		printf("\n");
	}
	return 0;
}
