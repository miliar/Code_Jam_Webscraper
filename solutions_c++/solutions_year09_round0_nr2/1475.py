#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

const int MAXN = 128;

int h[MAXN][MAXN];
char v[MAXN][MAXN];
int t, n, m;

char new_basin = 'a';

char flow(int x, int y)
{
	if (v[x][y]) return v[x][y];
	
	int cmin = h[x][y], cx=x, cy=y;
	if (x>0) if (cmin > h[x-1][y]) cmin = h[x-1][y], cx = x-1, cy = y;
	if (y>0) if (cmin > h[x][y-1]) cmin = h[x][y-1], cx = x, cy = y-1;
	if (y<m-1) if (cmin > h[x][y+1]) cmin = h[x][y+1], cx = x, cy = y+1;
	if (x<n-1) if (cmin > h[x+1][y]) cmin = h[x+1][y], cx = x+1, cy = y;
	
	//cout << "Found min " << cmin << " at pos " << cx << " " << cy << endl;
	
	if (cx==x && cy==y)
		return v[x][y] = new_basin++;
	return v[x][y] = flow(cx, cy);
}

int main(void)
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	fin >> t;
	for (int ct=1; ct<=t; ++ct) {
		memset(v, 0, sizeof(v));
		new_basin = 'a';
		
		fin >> n >> m;
		//cout << n << " " << m << endl;
		
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
				fin >> h[i][j];
		
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
				flow(i, j);
	
		fout << "Case #" << ct << ":" << endl;
		for (int i=0; i<n; ++i) {
			for (int j=0; j<m; ++j)
				fout << v[i][j] << " ";
			fout << endl;
		}
	}
	
	return 0;
}
