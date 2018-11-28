#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


int T,H,W;
int map[128][128];
char ans[128][128];
char cc;

void calc(int x,int y) {
	static int dx[] = {0, -1, 1, 0};
	static int dy[] = {-1,0,0,1};
	int min = map[y][x];
	int dd=-1;
	char c=0;
	for (int d=0;d<4;d++) {
		if (map[y+dy[d]][x+dx[d]]<min) {
			min = map[y+dy[d]][x+dx[d]];
			dd = d;
		}
	}

	if (dd<0) {
		ans[y][x] = cc++;
		return;
	}


	c = ans[y+dy[dd]][x+dx[dd]];
	if (!c) {
		calc(x+dx[dd],y+dy[dd]);
		c = ans[y+dy[dd]][x+dx[dd]];
	}
if (c==0) {
		cout <<x << "," << y << endl;
		for (int j=1;j<=H;j++) {
			for (int k=1;k<=W;k++) {
				cout << ans[j][k] << ",";
			}
			cout << endl;
		}
		cout << "ERROR!" << endl;
		exit(0);
}
	ans[y][x] = c;
}


int main()
{

//	ifstream cin( "B-t.in" );

	cin >> T;

	for (int i=0;i<T;i++) {
		cin >> H >> W;

		for (int j=0;j<=H+1;j++) {
			for (int k=0;k<=W+1;k++) {
				map[j][k] = 999999999;
				ans[j][k] = 0;
			}
		}


		for (int j=1;j<=H;j++) {
			for (int k=1;k<=W;k++) {
				cin >> map[j][k];
			}
		}


		cc = 'a';
		for (int j=1;j<=H;j++) {
			for (int k=1;k<=W;k++) {
				if (ans[j][k]) continue;
				calc(k,j);
			}
		}

		cout << "Case #" << i+1 << ":" <<  endl;
		for (int j=1;j<=H;j++) {
			for (int k=1;k<=W;k++) {
				cout << ans[j][k] << ((k<W)?" ":"");
			}
			cout << endl;
		}


	}

	return 0;
}

