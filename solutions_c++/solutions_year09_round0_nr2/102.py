#include <iostream>
#include <cstring>
#include <cassert>

using namespace std;

int area[1024][1024];
int colors[1024][1024];
int nextC;

int dy[] = {-1,0,0,1};
int dx[] = {0,-1,1,0};

int recC(int x, int y)
{
	assert(x>0);
	assert(y>0);
	if (colors[y][x]>=0) return colors[y][x];

	int base=area[y][x];
	int best=base, bi=-1;
	for(int i=0; i<4; ++i) {
		int x2=x+dx[i], y2=y+dy[i];
		int q=area[y2][x2];
		if (q<best) best=q, bi=i;
	}
	if (best==base)
		return colors[y][x] = nextC++;

	return colors[y][x] = recC(x+dx[bi], y+dy[bi]);
}
char letters[128];
char nextL;

char getL(int c)
{
	if (letters[c]) return letters[c];
//	if (nextL>'z') nextL='a';
	return letters[c]=nextL++;
}

int main()
{
	int t;
	cin>>t;
	for(int a=0; a<t; ++a) {
		for(int i=0; i<1024; ++i) for(int j=0; j<1024; ++j) area[i][j]=1<<20;
		nextC=0;

		int w,h;
		cin>>h>>w;
		for(int y=0; y<h; ++y) {
			for(int x=0; x<w; ++x) {
				cin>>area[y+1][x+1];
			}
		}
		memset(colors, -1, sizeof(colors));
		for(int y=0; y<h; ++y)
			for(int x=0; x<w; ++x)
				recC(x+1, y+1);

		memset(letters, 0, sizeof(letters));
		nextL='a';

		cout<<"Case #"<<a+1<<":\n";
		for(int y=0; y<h; ++y) {
			for(int x=0; x<w-1; ++x) {
				cout<<getL(colors[y+1][x+1])<<' ';
			}
			cout<<getL(colors[y+1][w])<<'\n';
		}
	}
}
