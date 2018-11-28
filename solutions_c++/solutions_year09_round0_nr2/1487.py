#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

const int SIZE = 1000;
int arr[SIZE][SIZE];
int res[SIZE][SIZE];
int R, C;

#define valid(r,c) ((r) >= 0 && (r) < R && (c) >= 0 && (c) < C)
int dir[4][2] = {{-1,0}, {0, -1}, {0, 1}, {1, 0}};	//four connected clockwise

int g;

int get(int r, int c){
	if(res[r][c] != -1)
		return res[r][c];

	int br = -1, bc;
	for(int i = 0 ; i < 4 ; i++){
		int rr = r+dir[i][0];
		int cc = c+dir[i][1];
		if(!valid(rr, cc) || arr[rr][cc] >= arr[r][c])
			continue;
		if(br == -1 || arr[rr][cc] < arr[br][bc]){
			br = rr;
			bc = cc;
		}
	}

	if(br == -1)
		return res[r][c] = g++;
	else
		return res[r][c] = get(br, bc);
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		cin >> R >> C;
		for(int r = 0 ; r < R ; r++)
			for(int c = 0 ; c < C ; c++){
				cin >> arr[r][c];
				res[r][c] = -1;
			}

		g = 0;
		for(int r = 0 ; r < R ; r++)
			for(int c = 0 ; c < C ; c++){
				if(res[r][c] != -1)continue;
				res[r][c] = get(r, c);
			}

		assert(g <= 26);

		cout << "Case #" << t+1 << ":" << endl;
		for(int r = 0 ; r < R ; r++){
			for(int c = 0 ;c  <C ; c++){
				if(c)cout << " ";
				cout << (char)('a'+res[r][c]);
			}
			cout << endl;
		}
	}

	return 0;
}
