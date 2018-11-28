#include <iostream>
#include <map>
using namespace std;

int H,W;
int height[100][100];
int basin_[100][100];

void check(int& best, int& besti, int& bestj, int i, int j) {
	if (height[i][j]<best) {
		best=height[i][j];
		besti=i;
		bestj=j;
	}
}

int basin(int i, int j) {
	if (basin_[i][j]!=i*W+j) {
		int best=height[i][j];
		int besti=i;
		int bestj=j;
		if (i>0) check(best,besti,bestj,i-1,j);
		if (j>0) check(best,besti,bestj,i,j-1);
		if (j+1<W) check(best,besti,bestj,i,j+1);
		if (i+1<H) check(best,besti,bestj,i+1,j);
		if (besti==i&&bestj==j) basin_[i][j]=i*W+j;
		else basin_[i][j] = basin(besti,bestj);
	}
	return basin_[i][j];
}

int main() {
	int T;
	cin>>T;
	for (int t=1;t<=T;++t) {
		cout << "Case #" << t << ":" << endl;
		cin >> H >> W;
		for (int i=0;i<H;++i) {
			for (int j=0;j<W;++j) {
				cin >> height[i][j];
				basin_[i][j]=-1;
			}
		}
		map<int,char> id;
		char letter='a';
		for (int i=0;i<H;++i) {
			for (int j=0;j<W;++j) {
				int b = basin(i,j);
				if (id[b]=='\0') id[b]=letter++;
			}
		}
		for (int i=0;i<H;++i) {
			for (int j=0;j<W;++j) {
				if (j) cout << " ";
				cout << id[basin_[i][j]];
			}
			cout << endl;
		}
	}
}
