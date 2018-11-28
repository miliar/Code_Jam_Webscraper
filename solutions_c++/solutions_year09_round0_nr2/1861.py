#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cmath>
 
using namespace std;
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

#define MAX   105
#define MAXAL 1000000

int mat[MAX][MAX];
char ma[MAX][MAX];
int dx[4]={-1, 0, 0, 1};
int dy[4]={0, -1, 1, 0};
int h,w;

void flow(int x,int y,char ant,char nov) {
	if (ma[x][y]!=ant)
		return;
	ma[x][y]=nov;
	flow(x-1,y,ant,nov);
	flow(x+1,y,ant,nov);
	flow(x,y-1,ant,nov);
	flow(x,y+1,ant,nov);
}

void back(char ant,char nov) {
	for (int x=1;x<=h;x++)
		for (int y=1;y<=w;y++)
			if (ma[x][y] == ant)
				ma[x][y] = nov;
}
		
int main() {
	int t;
	cin >> t;
	
	for (int k=1;k<=t;k++) {
		cin >> h >> w;
		
		for (int x=0;x<MAX;x++)
			for (int y=0;y<MAX;y++)
				mat[x][y] = MAXAL , ma[x][y]='0';
				
		for (int x=1;x<=h;x++)
			for (int y=1;y<=w;y++)
				cin >> mat[x][y];
		
		
		
		char let = 'A';		
		while ( true ) {
			int big = -1;
			int bx,by;
			for (int x=1;x<=h;x++)
				for (int y=1;y<=w;y++)
					if (ma[x][y] == '0' && mat[x][y] > big) {
						big = mat[x][y];
						bx = x;
						by = y;
					}
			//cout << big << " "  << bx << " " << by << endl;
			if (big == -1)
				break;
			
			int x = bx, y = by;
			while ( true ) {
				int val = mat[x][y];
				int mi = 1000000;
				int mix,miy;
				//cout << x << " " << y << " " << let << endl;
				if (ma[x][y] != '0') {
					back(let,ma[x][y]);
					break;
				}
				ma[x][y] = let;
				for (int u=0;u<4;u++) {
					if (mat[dx[u]+x][dy[u]+y] < val) {
						if (mi > mat[dx[u]+x][dy[u]+y]) {
							mi = mat[dx[u]+x][dy[u]+y];
							mix = dx[u]+x;
							miy = dy[u]+y;
						
						}
					}
				}
				if (mi == 1000000)
					break;
				x = mix;
				y = miy;
				
			}
			let++;
		}
		char next = 'a';
		int x = 1, y = 1;
		while ( true ) {
			if (ma[x][y] >= 'a' && ma[x][y] <= 'z') {
			
			}
			else {
				flow(x,y,ma[x][y],next);
				next++;
			}
			y++;
			if (y>w) {
				x++,y=1;
				if (x>h)
					break;
			}
		}
		
		cout << "Case #" << k << ":" << endl;
		for (int x=1;x<=h;x++) {
			cout << ma[x][1];
			for (int y=2;y<=w;y++)
				cout << " " << ma[x][y];
			cout << endl;
		}
	}
	return 0;
}

