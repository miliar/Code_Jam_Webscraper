#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

int dirBack[] = {3, 2, 1, 0};

int rows, cols;

bool test(int r, int c) {
    return r>=0 && r<rows && c>=0 && c<cols;
}

int main(void) {
    int n; SC(&n);

	int tab[100][100];
	int dir[100][100];
	int res[100][100];

    FOR(_i,n) {
		cin>>rows>>cols;

		FOR(r,rows) {
			FOR(c,cols) {
				cin >> tab[r][c];
				res[r][c]=-1;
			}
		}

		//set direction
		FOR(r,rows) FOR(c,cols) {
			int bestH = tab[r][c];
			int bestDir = -1;
			FOR(i,4) 
			{
				if (test(r+dr[i], c+dc[i]) && tab[r+dr[i]][c+dc[i]] < bestH) {
					bestH = tab [r+dr[i]] [c+dc[i]];
					bestDir = i;
				}
			}
			dir[r][c] = bestDir;
		}

		int field=0;
		FOR(r,rows) FOR(c,cols) {
			if (dir[r][c] == -1) {
				queue<pI> que;
				que.push(pI(r,c));

				while(que.empty() == false) {
					int rr = que.front().first;
					int cc = que.front().second;
					que.pop();

					res[rr][cc] = field;

					FOR(i,4) {
						if (test(rr+dr[i], cc+dc[i]) && dirBack[i] == dir[rr+dr[i]][cc+dc[i]]) {
							que.push(pI(rr+dr[i], cc+dc[i]));
						}
					}
				}

				++field;
			}
		}

		int mapping[30];
		int firstFree = 0;
		FOR(i,30) mapping[i]=-1;

        printf("Case #%d:\n", _i+1);
		FOR(r,rows) {
			FOR(c,cols) {
				if (c!=0) putchar(' ');

				int curr = res[r][c];
				if (mapping[curr] == -1)
					mapping[curr] = firstFree++;

				putchar( mapping[ res[r][c] ] + 'a');
			}
			putchar('\n');
		}
    }
    return 0;
}
