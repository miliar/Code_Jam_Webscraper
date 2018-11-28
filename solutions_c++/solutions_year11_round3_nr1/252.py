#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<numeric>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;
#define All(x) x.begin(),x.end()
#define push_back pb
#define MAX 55
char g[MAX][MAX];
int n,m;
void pintar(int x, int y){
	g[x][y] = '/';
	bool f = 0;
	if (y+1 > 0 && y+1 < m) if (g[x][y+1] == '#') {g[x][y+1] = '\\'; f = 1;}
	if (!f) g[x][y] = '#';
	f = 0;
	if (x+1 > 0 && x+1 < n) if (g[x+1][y] == '#') {g[x+1][y] = '\\'; f = 1;}
	if (!f){
		g[x][y] = '#';
		g[x+1][y] = '#';
	}
	f=0;
	if (x+1 > 0 && x+1 < n && y+1 > 0 && y+1 < m) if (g[x+1][y+1] == '#') { g[x+1][y+1] = '/'; f = 1;}
	if (!f){
		g[x][y] = '#';
		g[x+1][y] = '#';
		g[x+1][y+1] = '#';
	}
}

int main(){
	int runs;
	cin>>runs;
	for(int r = 1; r <= runs; r++){

		cin>>n>>m;
		int c  = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++){
				cin>>g[i][j];
				if (g[i][j] == '#') c++;
			}
		}
		printf("Case #%d:\n",r);
		if (c % 4 != 0){
			puts("Impossible");
			continue;
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if (g[i][j] == '#'){
					pintar(i,j);
				}
			}
		}
		bool f = true;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if (g[i][j] == '#'){
					f = false;
					goto sale;
				}
			}
		}
		sale:
		if (!f) puts("Impossible");
		else {
			for(int i = 0; i < n; i++){
				for(int j = 0; j < m; j++){
					cout<<g[i][j];
				}
				cout<<endl;
			}
		
		}
		
	}
	return 0;
}
