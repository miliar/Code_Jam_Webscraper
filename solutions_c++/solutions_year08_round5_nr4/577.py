#include<iostream>
#include<cstdlib>
#include<cmath>

using namespace std;

#define MOD 10007
int rock[102][102];
int ways[102][102];

int main(){
	int N; cin >> N;
	for(int t=1; t<=N; t++){
		int H, W, R; cin >> H >> W >> R;
		memset(rock,0,sizeof(rock));
		for(int i=0; i<R; i++){
			int r,c; cin >> r >> c;
			rock[r-1][c-1]=1;
		}
		memset(ways,0,sizeof(ways));
		ways[0][0]=1;

		int dx[]={-1,-2};
		int dy[]={-2,-1};
		for(int i=0; i<H; i++)for(int j=0; j<W; j++){
			if(i==0 && j==0)continue;
			if(rock[i][j]==1)continue;
			for(int k=0; k<2; k++){
				if(i+dx[k]<0 || j+dy[k]<0)continue;
				ways[i][j]+=ways[i+dx[k]][j+dy[k]];
				ways[i][j]%=MOD;
			}
		}
		cout << "Case #" << t << ": " << ways[H-1][W-1] << "\n";
	}

}
