#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>

using namespace std;

typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

int f, r, c;
string maze[60];
int dist[60][60][60][60];

struct cmp{
	bool operator()(const pair<pair<int,int>, pair<int,int> >& p1, const pair<pair<int,int>, pair<int,int> >& p2){
		if (dist[p1.first.first][p1.first.second][p1.second.first][p1.second.second] 
			== dist[p2.first.first][p2.first.second][p2.second.first][p2.second.second] )
			return p1 < p2;
		else return dist[p1.first.first][p1.first.second][p1.second.first][p1.second.second] 
			< dist[p2.first.first][p2.first.second][p2.second.first][p2.second.second];
	}
};

int dijkstra(){
	for (int i = 0; i < 60; i++)
		for (int j = 0; j < 60; j++)
			for (int k = 0; k < 60; k++)
				for (int m = 0; m < 60; m++)
					dist[i][j][k][m] = 0x3f3f3f3f;
	dist[0][0][0][0] = 0;
	set<pair<pair<int,int>, pair<int,int> > , cmp> q;
	q.insert(make_pair(make_pair(0,0),make_pair(0,0)));
	while (!q.empty()){
		pair<pair<int,int>, pair<int,int> > pi = *q.begin(); q.erase(pi);
		int row = pi.first.first, column = pi.first.second;
		int digleft = pi.second.first, digright = pi.second.second;
		int curdist = dist[row][column][digleft][digright];
		//if (curdist < 10) cout << row << " " << column << " "  << digleft << " " << digright << " " << dist[row][column][digleft][digright] << endl;
		if (row == r-1) return curdist;
		int left = column, right = column;
		for (int i = column - 1; i >= 0; i--){
			if (maze[row][i] == '.' && (maze[row+1][i] == '#')) left = i;
			else if (i >= digleft && i <= digright && (maze[row+1][i] == '#')) left = i;
			else break;
		}
		for (int i = column + 1; i < c; i++){
			if (maze[row][i] == '.' && (maze[row+1][i] == '#')) right = i;
			else if (i >= digleft && i <= digright && (maze[row+1][i] == '#')) right = i;
			else break;
		}
		//cout << "left = " << left << ", right = " << right << endl;
		if (left != right){
			//cout << "here" << endl;
			for (int i = left; i <= right; i++){
				int j = row+2;
				while (j < r && maze[j][i] == '.') j++;
				j--;
				if (j - row > f) continue;
				if (dist[j][i][i][i] > curdist+1){
					pair<pair<int,int>, pair<int,int> > newpi = make_pair(make_pair(j,i),make_pair(i,i));
					q.erase(newpi);
					dist[j][i][i][i] = curdist+1;
					q.insert(newpi);
				}
				if (j == row + 1){
					//cout << "i = " << i << ", j = " << j << ", j = row + 1" << endl;
					if (i != left){
						for (int k = i+1; k <= right; k++){
							if (dist[j][i][i][k] > curdist + k - i + 1){
								pair<pair<int,int>, pair<int,int> > newpi = make_pair(make_pair(j,i),make_pair(i,k));
								q.erase(newpi);
								dist[j][i][i][k] = curdist+k-i+1;
								q.insert(newpi);
							}
						}
					}
					if (i != right){
					for (int k = i-1; k >= left; k--){
							if (dist[j][i][k][i] > curdist + i - k + 1){
								pair<pair<int,int>, pair<int,int> > newpi = make_pair(make_pair(j,i),make_pair(k,i));
								q.erase(newpi);
								dist[j][i][k][i] = curdist+i-k+1;
								q.insert(newpi);
							}
						}
					}
				}
			}
		}
		if (left > 0 && (maze[row][left-1] == '.' || (left-1 >= digleft && left-1 <= digright))){
			//cout << "push_front, left" << endl;
			int i = left - 1;
			int j = row+2;
			while (j < r && maze[j][i] == '.') j++;
			j--;
			if (j - row > f) continue;
			if (dist[j][i][i][i] > curdist){
				pair<pair<int,int>, pair<int,int> > newpi = make_pair(make_pair(j,i),make_pair(i,i));
				q.erase(newpi);
				dist[j][i][i][i] = curdist;
				q.insert(newpi);
			}
		}
		if (right < c - 1 && (maze[row][right+1] == '.' || (right+1 >= digleft && right+1 <= digright))){
			//cout << "push_front, right" << endl;
			int i = right + 1;
			int j = row+2;
			while (j < r && maze[j][i] == '.') j++;
			j--;
			if (j - row > f) continue;
			if (dist[j][i][i][i] > curdist){
				pair<pair<int,int>, pair<int,int> > newpi = make_pair(make_pair(j,i),make_pair(i,i));
				q.erase(newpi);
				dist[j][i][i][i] = curdist;
				q.insert(newpi);
			}
		}
	}
	return -1;
}

int main(){
	int abc; cin >> abc;
	for (int zzz = 1; zzz <= abc; zzz++){
		cin >> r >> c >> f;
		for (int i = 0; i < r; i++)
			cin >> maze[i];
		int ans = dijkstra();
		if (ans == -1) cout << "Case #" << zzz << ": No" << endl;
		else cout << "Case #" << zzz << ": Yes " << ans << endl;
	}
	return 0;
}
