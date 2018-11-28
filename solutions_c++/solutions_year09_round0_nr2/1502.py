#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
using namespace std;

vector<vector<int> > v;
vector<vector<char> > vc;
vector<vector<pair<int,int> > > vp;

char cnext;

char rec(int x, int y) {
	if (vc[x][y] != 0)
		return vc[x][y];
  if (vp[x][y].first == x && vp[x][y].second == y) {
   	vc[x][y] = cnext++;
  	return vc[x][y];
  }
	vc[x][y] = rec(vp[x][y].first, vp[x][y].second);
	return vc[x][y];
}


int main() {
	freopen("inputb.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int cnt = 0;
	while (t--) {
 		++cnt;	
		cnext = 'a';
		int h, w;
		cin >> h >> w;
		v.resize(h+2);
		vp.resize(h+2);
		vc.resize(h+2);
		v[0].resize(w+2);
		v[h+1].resize(w+2);
		fill(v[0].begin(),   v[0].end(),   1 << 20);
		fill(v[h+1].begin(), v[h+1].end(), 1 << 20);
		for (int i = 1; i <= h; ++i) {
			v[i].resize(w+2);
			vp[i].resize(w+2);
			vc[i].resize(w+2);
			fill(vc[i].begin(), vc[i].end(), 0);
			v[i][0] = v[i][w+1] = 1 << 20;
			for (int j = 1; j <= w; ++j) {
				cin >> v[i][j];
			}
		}
		for (int i = 1; i <= h; ++i) {
			for (int j = 1; j <= w; ++j) {
			 if (v[i-1][j] < v[i][j] && v[i-1][j] <= v[i][j-1] && v[i-1][j] <= v[i+1][j] && v[i-1][j] <= v[i][j+1]) {
			  vp[i][j].first = i-1;
			  vp[i][j].second = j;
			 } else if (v[i][j-1] < v[i][j] && v[i][j-1] <= v[i+1][j] && v[i][j-1] <= v[i][j+1]) {
			  vp[i][j].first = i;
			  vp[i][j].second = j-1;
			 } else if (v[i][j+1] < v[i][j] && v[i][j+1] <= v[i+1][j]) {
			  vp[i][j].first = i;
			  vp[i][j].second = j+1;
			 } else if (v[i+1][j] < v[i][j]) {
			  vp[i][j].first = i+1;
			  vp[i][j].second = j;
			 } else {
			  vp[i][j].first = i;
			  vp[i][j].second = j;
			 }
			 //cout << "(" << vp[i][j].first << "," << vp[i][j].second << ") ";
			}
		}
		cout << "Case #" << cnt << ":" << endl;
		for (int i = 1; i <= h; ++i) {
			for (int j = 1; j <= w; ++j) {
				rec(i, j);
				cout << vc[i][j] << " ";
			}
			cout << endl;
		}

	}

	return 0;
}
