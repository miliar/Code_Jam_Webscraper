#include <iostream>
#include <string>
#include <map>
using namespace std ;
int create(map<string,int>&fs, string path){
	if(fs.find(path) != fs.end() || path == "") return 0 ;
	fs[path] = 0 ;
	int n = path.length() - 1 ;
	while(path[n] != '/') n-- ;
	return create(fs,path.substr(0,n)) + 1 ;
}
int main(){
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int n , m ; cin >> n >> m ;
		int ans = 0 ;
		map<string,int> fs ;
		string path ;
		while(n--){
			cin >> path ; create(fs,path) ; 
		}
		while(m--){
			cin >> path ; ans += create(fs,path) ;
		}
		cout << "Case #" << t << ": " << ans << endl ;
	}
}
