#include <iostream>
#include <map>
using namespace std ;
int main(){
	int T; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int r ; cin >> r ;
		map<pair<int,int> , int> cell ;
		for(int i = 0 ; i < r ; i++){
			int a , b , c , d ; cin >> a >> c >> b >> d ;
			for(int x = a ; x <= b ; x++){
				for(int y = c ; y <= d ; y++){
					cell[make_pair(x,y)] = 0 ;
				}
			}
		}
		int time = 0 ;
		while(cell.size()){
			map<pair<int,int> , int> nc ;
			for(map<pair<int,int>,int>::iterator it = cell.begin() ; it != cell.end() ; it++){
				int x = it->first.first ;
				int y = it->first.second;
				if(cell.find(make_pair(x-1,y)) != cell.end() || cell.find(make_pair(x,y-1)) != cell.end() )
					nc[make_pair(x,y)] = 0 ;
				
				if(cell.find(make_pair(x+1,y-1)) != cell.end())
					nc[make_pair(x+1,y)] = 0;
				if(cell.find(make_pair(x-1,y+1)) != cell.end())
					nc[make_pair(x,y+1)] = 0;
			}
			/*
			for(int i = 0 ; i < 6 ; i++){
				for(int j = 0 ; j < 6 ; j++){
					if(cell.find(make_pair(j,i)) != cell.end()) cout << "o" ;
					else cout << 'x' ;
				}
				cout << endl ;
			}
			cout << "-------------------" << endl ;
			*/
			cell = nc ;
			time++ ;
		}
		cout << "Case #" << t << ": " << time << endl ;
	}
}
