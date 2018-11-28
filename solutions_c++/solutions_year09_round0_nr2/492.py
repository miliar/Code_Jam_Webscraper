#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std ;
typedef pair<int,int> pii ;
void dfs(char rmap[][200], char count, map<pii,map<pii,int> > &tree , pii p){
	int x = p.first, y = p.second ;
	if(rmap[x][y] != 0) return ;
	rmap[x][y] = count ;
	for(map<pii,int>::iterator it = tree[p].begin() ; it != tree[p].end() ; it++){
		dfs(rmap,count,tree,it->first) ;
	}
}
int main(){	
	int n ; cin >> n ;
	int vc[4][2] = {{-1,0},{0,-1},{0,1},{1,0}} ;
	int emap[200][200] ;
	int h , w ;
	for(int t = 1 ; t <= n ; t++){
		cin >> h >> w ;
		for(int i = 0 ; i < h ; i++)
			for(int j = 0 ; j < w ; j++)
				cin >> emap[i][j] ;
		map<pii,map<pii,int> > tree ;
		for(int i = 0 ; i < h ; i++){
			for(int j = 0 ; j < w ; j++){
				pii u = pii(i,j) , v ; int min_alt = 100000 ;
				for(int k = 0 ; k < 4 ; k++){
					int vx = i + vc[k][0] , vy = j+vc[k][1] ;
					if(vx < 0 || vx >= h || vy < 0 || vy >= w) continue ;
					if(min_alt > emap[vx][vy]){
						min_alt = emap[vx][vy] ;
						v = pii(vx,vy) ;
					}
				}
				if(min_alt < emap[i][j]){
					tree[u][v] = tree[v][u] = 1 ; 
				}
			}
		}
		char rmap[200][200] = {0} ;
		char count = 'a' ;
		for(int x = 0 ; x < h ; x++){
			for(int y = 0 ; y < w ; y++){
				if(rmap[x][y] == 0) dfs(rmap,count++,tree,pii(x,y)) ;
			}
		}
		cout << "Case #" << t << ":" << endl ;
		for(int x = 0 ; x < h ; x++){
			for(int y = 0 ; y < w ; y++){
				cout << rmap[x][y] ;
				if(y < w-1) cout << " " ;
				else cout << endl ;
			}
		}
	}
}
