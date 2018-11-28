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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int a[100][100], b[100][100];
int dir[4][2] = {0,-1,-1,0,1,0,0,1};
int id, H, W;
int s[10000];
int m[10000];

int find_root(int k) {
	if (s[k] < 0) return k;
	return s[k] = find_root(s[k]);
}

void union_set(int root1, int root2) {
	if (s[root1] < s[root2]) s[root2] = root1;
	else {
		if (s[root1] == s[root2]) s[root2]--;
		s[root1] = root2;
	}
}

void flow(int x, int y) {
	int i, j, k, xx, yy;
	j = -1;
	k = a[x][y];
	for (i=0; i<4; i++) {
		xx = x + dir[i][1];
		yy = y + dir[i][0];
		if (xx<0 || xx>= H || yy<0 || yy>=W) continue;
		if (a[xx][yy] < k) k = a[xx][yy], j=i;
	}
	if (j != -1) {
		xx = x + dir[j][1];
		yy = y + dir[j][0];
		int ra = find_root(x*W+y);
		int rb = find_root(xx*W+yy);
		if (ra != rb) union_set(ra, rb);
	}
}

char print(int x, int y) {
	int r = find_root(x*W+y);
	if (m[r] == -1) m[r]=id,id++;
	return char(m[r]+'a');
}

int main() {
	//ifstream cin("B-small.in");
	ifstream cin("B-large.in");
	ofstream cout("B-out");
	int T, Case;
	int i, j, k;
	
	for (cin>>T, Case=1; T; T--,Case++) {
		memset(a, 0, sizeof(a));
		memset(b, -1, sizeof(b));
		memset(s, -1, sizeof(s));
		memset(m, -1, sizeof(m));
		cin>>H>>W;
		for (i=0; i<H; i++) {
			for (j=0; j<W; j++)
				cin>>a[i][j];
		}	
		for (i=0; i<H; i++) {
			for (j=0; j<W; j++) {
				flow(i,j);
			}
		}
		id = 0;
		cout<<"Case #"<<Case<<":"<<endl;
		for (i=0; i<H; i++) {
			cout<<print(i, 0);
			for (j=1; j<W; j++) {
				cout<<" "<<print(i, j);
			}
			cout<<endl;
		}
	}

}