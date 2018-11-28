#include<cstdio>
#include<map>
#include<vector>
#include<sstream>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a;i < b;++i)
#define FORZ(i,t) for(int i = 0;i < t;++i)
#define PB push_back

typedef long long LL;

int grid[1001][1001],M,N,vis[1001][1001];

int val[100];

bool solve(int xx,int yy,int l) {
	int color = grid[xx][yy];
	int mod = (xx + yy) % 2;
	FOR(i,xx,xx+l)
		FOR(j,yy,yy+l)	{
		if(vis[i][j])
			return false;
		if( (i + j) % 2 == mod ){
			if(grid[i][j] != color)
				return false;
		}
		else {
			if(grid[i][j] == color)
				return false;
		}
	}
	return true;
}

int main(){
	int test = GI;
	
	FOR(i,1,test+1){
		memset(vis,0,sizeof vis);
		M = GI,N = GI;
		N /= 4;
		for(char a = '0';a <= '9';++a)
			val[a] = a - '0';
		for(char a = 'A';a <= 'F';++a)
			val[a] = a - 'A' + 10;
	string s;
		FOR(j,0,M) {
				cin >> s;
				int k = 0;
				FOR(l,0,s.size()){
					grid[j][k << 2] = (val[s[l]] & (1 << 3)) > 0; 
					grid[j][(k << 2) + 1] = (val[s[l]] & (1 << 2)) > 0; 
					grid[j][(k << 2) + 2] = (val[s[l]] & (1 << 1)) > 0; 
					grid[j][(k << 2) + 3] = (val[s[l]] & (1 << 0)) > 0; 
					++k;
				}						
			}

		
		printf("Case #%d: ",i);
		N*=4;
		/*
		FOR(l,0,M){
			printf("\n");
			FOR(m,0,N)
				printf("%d ",grid[l][m]);
		}
*/
		vector<pair<int,int> > ans;ans.clear();

		for(int l = min(N,M);l >= 2;--l){
			int ml = 0;
			for(int i = 0;i < M-l+1;++i)
				for(int j =0;j < N-l+1;++j)
					if(solve(i,j,l))			
					{
						++ml;
						FOR(x,i,i+l)
							FOR(y,j,j+l)
							vis[x][y] = 1;
					}
			if(ml)
				ans.push_back(make_pair(l,ml));
		}

		int tot = N*M;
		FOR(j,0,ans.size()) {
           tot -= ans[j].first * ans[j].first * ans[j].second;
        }
	
		printf("%d\n",ans.size() + (tot > 0));

		FOR(j,0,ans.size()) {
			printf("%d %d\n",ans[j].first,ans[j].second);
		}
		if(tot)
		printf("%d %d\n",1,tot);
	}

	return 0;
}
