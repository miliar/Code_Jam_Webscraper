#include <iostream>
using namespace std;

typedef long long LL;

int H,W;
int map[100][100];
char labels[100][100];

void dfs(int r, int c, char label) {
	if (labels[r][c]) {
		return;
	}
	int bestAlt=map[r][c];
	int bestR=-1, bestC=-1;
	int d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
	for (int i=0; i<4; ++i) {
		int nr=r+d[i][0];
		int nc=c+d[i][1];
		if (nr>=0 && nc>=0 && nr<H && nc<W && map[nr][nc]<bestAlt) {
			bestAlt=map[nr][nc];
			bestR=nr;
			bestC=nc;
		}
	}
	if (bestR>=0) {
        dfs(bestR, bestC, label);
		labels[r][c]=labels[bestR][bestC];
	}
	else {
		labels[r][c]=label;
	}
}

int main() {
	int T;
	cin>>T;
	for (int i=0; i<T; ++i) {
		cin>>H>>W;
		for (int j=0; j<H; ++j) {
			for (int k=0; k<W; ++k) {
				cin>>map[j][k];
			}
		}
		cout<<"Case #"<<(i+1)<<':'<<endl;
		char label='a';
		memset(labels,0,sizeof labels);
		for (int j=0; j<H; ++j) {
			for (int k=0; k<W; ++k) {
				if (k) {
					cout<<' ';
				}
				dfs(j,k,label);
				if (labels[j][k]==label) {
					++label;
				}
				cout<<labels[j][k];
			}
			cout<<endl;
		}
	}
	return 0;
}
