#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
using namespace std;
const int M = 210;
const int inf = 1000000000;
const double eps = 1e-8;
int r, c;
char g[M][M];
bool equ(int i, int j){
	return g[i][j] == '#'? true:false;
}
bool find(){
	int i,j;
	for(i = 0; i < r-1;i ++){
		for(j = 0; j < c-1;j ++){
			if(g[i][j] == '#'){
				if(equ(i, j+1) && equ(i+1, j) && equ(i+1, j+1)) 
				{
					g[i][j] = '/';
					g[i][j+1] = '\\';
					g[i+1][j] = '\\';
					g[i+1][j+1] = '/';
				}else return false;
			}
		}
	}
	for(i= 0; i < r; i ++)
		for(j = 0; j < c; j ++)
			if(g[i][j] == '#')
				return false;

	return true;
}
void solve(){
	int i;
	cin >> r >> c;
	for(i = 0; i< r; i ++)
		scanf ("%s", g[i]);
	bool flag = find();
	if(!flag) {
		puts("Impossible"); return ;
	}else{
		for(i = 0; i < r; i ++)
			puts(g[i]);
	}
}
int main(){
	int cas;
	int i;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf ("%d", &cas);
	for(i = 1; i <= cas; i ++){
		printf ("Case #%d:\n", i);
		solve();
	}
	return 0;
}