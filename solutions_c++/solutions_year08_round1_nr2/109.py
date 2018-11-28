#include <map>
#include <vector>
#include <iostream>
using namespace std ;

int main(){
	int T ;
	cin >> T ;
	for(int Case = 1 ; Case <= T ; Case++){
		int n , m ;
		cin >> n >> m ;
		vector<map<int,int> > cus(m) ;
		vector<int> flavor(n+1,0) ;
		for(int i = 0 ; i < m ; i++){
			int t ;
			cin >> t ;
			for(int j = 0 ; j < t ; j++){
				int x , y ;
				cin >> x >> y ;
				cus[i][x+y*10000] ;
			}
		}
		bool check = true ;
		for(int i = 0 ; i < n ; i++){
			int x = -1 ;
			for(int j = 0 ; j < m ; j++){
				if(cus[j].size() == 1 && cus[j].begin()->first > 10000){
					x =  cus[j].begin()->first ; break ;	
				}
			}
			if(x == -1) break ;
			flavor[x- 10000] = 1 ;
			for(int j = 0 ; j < m ; j++){
				if(cus[j].size() != 0){
					if(cus[j].find(x) != cus[j].end()) cus[j].clear() ;
					if(cus[j].find(x-10000) != cus[j].end()){
						cus[j].erase(x-10000) ;
						if(cus[j].size() == 0) check = false ;
					}
				}
			}
		}
		cout << "Case #"<< Case << ": " ;
		if(check){
			for(int i = 1 ; i < n ; i++){
				cout << flavor[i] << ' ' ;
			}
			cout << flavor[n] << endl ;
		}else{
			cout << "IMPOSSIBLE" << endl ;
		}
	}
}
