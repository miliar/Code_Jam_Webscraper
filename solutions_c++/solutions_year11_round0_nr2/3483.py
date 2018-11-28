#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std ;
int main(){
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int c ; cin >> c ;
		map<string,string> cr ;
		while(c--){
			string s ; cin >> s ;
			cr[string(1,s[0])+string(1,s[1])] = string(1,s[2]) ;
			cr[string(1,s[1])+string(1,s[0])] = string(1,s[2]) ;
		}
		map<string, int> opp ;
		int o ; cin >> o ;
		while(o--){
			string s ; cin >> s ;
			opp[string(1,s[0])+string(1,s[1])] = 1 ;
			opp[string(1,s[1])+string(1,s[0])] = 1 ;
		}
		int n ; string spell ; cin >> n >> spell ;
		vector<string> elist ;
		for(int i = 0 ; i < n ; i++){
			string e = string(1,spell[i]) ;
			elist.push_back(e) ;
			while(elist.size() >= 2){
				string e1 = elist[elist.size() - 1], e2 = elist[elist.size() - 2] ;
				if(cr.find(e1+e2) != cr.end()){
					elist.pop_back() ; elist.pop_back() ;
					elist.push_back(cr[e1+e2]) ;
				}else{
					break ;
				}
			}
			e = elist[elist.size() - 1] ;
			for(int i = 0 ; i < elist.size() - 1 ; i++){
				string e2 = elist[i] ;
				if(opp.find(e+e2) != opp.end()){
					elist.clear() ; break ;
				}
			}
		}
		cout << "Case #" << t << ": [" ;
		for(int i = 0 ; i < elist.size() ; i++){
			cout << ((i == 0) ? "" : ", ") << elist[i] ;
		}
		cout << "]" << endl ;
	}
}
