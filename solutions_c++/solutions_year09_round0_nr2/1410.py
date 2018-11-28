#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
using namespace std;

struct node {
	int x;
	int y;
	node (int X,int Y) {
		x = X;
		y = Y;
	}
};

bool valid (node obj, int w, int h) {
	if (0 <= obj.x && obj.x <= w-1) {
		if (0 <= obj.y && obj.y <= h-1) return true;
		return false;
	}
	return false;
}

int bfs (vector < vector <int> > mat, int i, int j, int k, vector < vector <int> > &mat2, int w, int h) {
	int arr[4][2] = {{0,-1},{-1,0},{1,0},{0,1}};
	queue <node> q;
	node obj(j,i);
	q.push(obj);
	map <int,int> parent;
	int sink = -1;
	int level = k;
	while (!q.empty()) {
		node top = q.front();
		q.pop();
		int max = 99999;
		int X = -1;
		int Y = -1;
		for (int r = 0; r < 4; r++) {
			node obj(top.x+arr[r][0], top.y+arr[r][1]);
			if (valid(obj,w,h)) {
				if (mat[top.y][top.x] > mat[obj.y][obj.x]) {
					if (max > mat[obj.y][obj.x]) {
						max = mat[obj.y][obj.x];
						X = obj.x;
						Y = obj.y;
					}
				}	
			}
		}
		if (max == 99999) {
			sink = top.y*w+top.x;
			if (mat2[top.y][top.x] != -1) level = mat2[top.y][top.x];
			break;
		}
		node obj(X,Y);
		q.push(obj);
		parent[Y*w+X] = top.y*w+top.x;
	}
	int curr = sink;
	while (curr != i*w+j) {
		mat2[curr/w][curr%w] = level;
		curr = parent[curr];
	}
	mat2[i][j] = level;
	if (level != k) return k;
	return k+1;
}

int main () {
	
	int t;
	scanf("%d",&t);

	for (int i = 1; i <= t; i++) {
		int h,w;	
		cin >> h >> w;
		vector < vector <int> > mat(h,vector<int>(w));
		for (int j = 0; j < h; j++) {
			for (int k = 0; k < w; k++) {
				scanf ("%d",&mat[j][k]);
			}
		}
		vector < vector <int> > mat2(h,vector<int>(w,-1));
		int a = 97;
		for (int j = 0; j < h; j++) {
			for (int k = 0; k < w; k++) {
				a = bfs(mat,j,k,a,mat2,w,h);
			}
		}
		cout << "Case #" << i << ":\n";
		for (int j = 0; j < h; j++) {
			for (int k = 0; k < w; k++) {
				cout << (char)mat2[j][k] << " ";
			}
			cout << "\n";
		}
	}
	return 0;
}