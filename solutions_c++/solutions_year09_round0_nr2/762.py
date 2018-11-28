#include <iostream>
#include <cmath>
#include <cstdlib>
#include <functional>
#include <algorithm>
#include <string>
#include <vector>


using namespace std;

#define NMAX 111
int H, W; 
int  alt[NMAX][NMAX];
char ans[NMAX][NMAX];
char basin='a';

bool next(int &x, int &y) {
	int x1=x, y1=y, b=alt[y1][x1];
	if(y>0)		if(alt[y-1][x]<b) { x1=x; y1=y-1; b=alt[y1][x1]; }
	if(x>0)		if(alt[y][x-1]<b) { x1=x-1; y1=y; b=alt[y1][x1]; }
	if(x<W-1)	if(alt[y][x+1]<b) { x1=x+1; y1=y; b=alt[y1][x1]; }
	if(y<H-1)	if(alt[y+1][x]<b) { x1=x; y1=y+1; b=alt[y1][x1]; }

	bool o = (x!=x1)||(y!=y1);
	x=x1; y=y1;
	return o;
}

char flow(int x, int y) {
	int x1, y1;
	x1=x; y1=y;
	while(next(x1,y1)) 
		;

	char c = ans[y1][x1];
	if(!c) {
		c = basin++;
	}

	x1=x; y1=y;
	ans[y1][x1] = c;
	while(next(x1,y1)) 
		ans[y1][x1] = c;
	ans[y1][x1] = c;
	return c;
}

int main() {
	ios_base::sync_with_stdio(0);
	int T; cin>>T;

	// CASES
	for(int icase=1; icase<=T; ++icase) {
		// INIT, IN
		cin>>H>>W;
		memset(alt,0,sizeof(alt));
		for(int y=0; y<H; ++y) {
			for(int x=0; x<W; ++x) {
				cin>>alt[y][x];
			}
		}

		// SOLVE
		basin='a';
		memset(ans,0,sizeof(ans));

		for(int y=0; y<H; ++y) {
			for(int x=0; x<W; ++x) {
				if(!ans[y][x])
					flow(x,y);
			}
		}

		cout<<"Case #"<<icase<<":"<<endl;
		for(int y=0; y<H; ++y) {
			for(int x=0; x<W; ++x) {
				if(x>0) cout<<" ";
				cout<<ans[y][x];
			}
			cout<<endl;
		}


	}

	return 0;
}

/*
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8

*/



