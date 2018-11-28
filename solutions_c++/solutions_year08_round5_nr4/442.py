#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

#define MOD 10007
#define X 110
#define point pair<int,int>

int b[X][X];
vector<point > rocks;

int main(){
	int n;
	scanf("%d",&n);
	for(int testCase = 1; testCase <= n; ++testCase){
		for(int i = 0; i < X; ++i) for(int j = 0; j < X; ++j) b[i][j] = 0;
		
		int h,w,r;
		scanf("%d %d %d\n",&h, &w, &r);
		rocks.clear();
		for(int i = 0; i < r; ++i){
			point tmp;
			scanf("%d %d",&tmp.first, &tmp.second);
			rocks.push_back(tmp);
		}

		b[1][1] = 1;
		for(int row = 1; row <= h; ++row) for(int col = 1; col <= w; ++col){
			bool ok = true;
			for(int i = 0; i < rocks.size(); ++i) 
			if(rocks[i].first == row && rocks[i].second == col){
				b[row][col] = 0;
				ok = false;
			}	
			if (ok)
			{
				if(row >= 3 && col >= 2) b[row][col] += b[row-2][col-1];
				if(row >= 2 && col >= 3) b[row][col] += b[row-1][col-2];
				b[row][col] %= MOD;
			}
		}

		printf("Case #%d: %d\n",testCase, b[h][w]);
	}

}
