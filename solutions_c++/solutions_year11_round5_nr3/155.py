#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std ;
int main(){
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int r, c; cin >> r >> c ;
		char m[200][200] ;
		for(int i = 0 ; i < r ; i++)
			cin >> m[i] ;
		map<int,int> g[10000],invg[10000] ;
		for(int i = 0 ; i < r ; i++){
			for(int j = 0 ; j < c ; j++){
				const char* v = "--||//\\\\" ;
				int vx[] = {0, 0,1,-1, 1,-1,1,-1} ;
				int vy[] = {1,-1,0, 0,-1, 1,1,-1} ;
				for(int k = 0 ; k < 8 ; k++){
					if(v[k] == m[i][j]){
						int x = i + vx[k], y = j+vy[k] ;
						if(x < 0) x += r ;
						if(x == r) x -= r ;
						if(y < 0) y += c ;
						if(y == c) y -= c ;
						int u = i * c + j;
						int v = x * c + y ;
						g[v][u] == 0 ;
						invg[u][v] == 0 ;
					}
				}
			}
		}
		int visited[10000] = {0} ;
		vector<int> cleaning ;
		bool fail = false ;
		for(int i = 0 ; i < r*c; i++){
			if(g[i].size() == 1) cleaning.push_back(i);
			if(g[i].size() == 0) fail = true ;
			/*for(map<int,int>::iterator it = g[i].begin() ; it != g[i].end() ; it++){
				cout << it->first << ' ' ;
			}
			cout << endl ;
			*/
		}
		//cout << "--------------" << endl ;
		if(fail){
			cout << "Case #"<< t << ": 0" << endl ;
			continue ;
		}
		while(!cleaning.empty()){
			int x = *cleaning.rbegin() ;
			cleaning.pop_back() ;
			int y = g[x].begin()->first ;
			for(map<int,int>::iterator it = invg[y].begin() ; it != invg[y].end() ; it++){
				int z = it->first ;
				g[z].erase(y) ;
				if(g[z].size() == 1) cleaning.push_back(z) ;
			}
		}
		int ans = 0 ;
		map<int,int> forbid ;
		for(int i = 0 ; i < r*c ; i++){
			if(g[i].size() >= 2 && forbid.find(i) == forbid.end()){
				if(g[i].size() != 2){
					fail = true ;
					break ;
				}
				forbid[i] = 0 ;
				ans++ ;
				map<int,int> visited ;
				vector<int> wait ;
				for(map<int,int>::iterator it = g[i].begin() ; it != g[i].end() ; it++){
					int x = it->first ;
					wait.push_back(x) ;
				}
				while(!wait.empty()){
					int x = *wait.rbegin() ;
					wait.pop_back();
					if(visited.find(x) != visited.end()) continue ;
					visited[x] = 0 ;
					for(map<int,int>::iterator it = invg[x].begin() ; it != invg[x].end() ; it++){
						int y = it->first ;
						forbid[y] = 0 ;
						for(map<int,int>::iterator it = g[y].begin() ; it != g[y].end() ; it++){
							int z = it->first ;
							wait.push_back(z) ;
						}
					}
				}
			}
		}
		
		if(fail){
			cout << "Case #"<< t << ": 0" << endl ;
			continue ;
		}
		int rans = 1 ;
		while(ans--){
			rans = (rans * 2) % 1000003 ;
		}
		cout << "Case #" << t << ": " << rans << endl ;

	}
}
