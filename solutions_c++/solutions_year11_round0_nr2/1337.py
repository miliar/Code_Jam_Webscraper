#include <iostream>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <utility>

using namespace std ;

int main(){
	int T ;
	cin >> T ;
	for(int it = 1 ; it <= T ; it++){
		int C , D , N ;
		map<pair<char,char> , char > com ;
		set<pair<char,char> > res ;
		cin >> C ;
		for(int i = 0 ; i < C ; i++){
			string f ;
			cin >> f;
			com[make_pair(f[0],f[1])] = f[2] ;
			com[make_pair(f[1],f[0])] = f[2] ;
		}
		cin >> D ;
		for(int i = 0 ;i < D ; ++i){
			string f ;
			cin >> f ;
			res.insert(make_pair(f[0] , f[1]));
			res.insert(make_pair(f[1] , f[0]));
		}

		cin >> N ;
		string seq ;
		cin >> seq ;
		vector<char> ans ;
		for(int i = 0 ;i < N ; i++){
			ans.push_back(seq[i]);
			if(ans.size() >= 2){
				int n = ans.size();
				if(com.count(make_pair(ans[n-2],ans[n-1]))){
					ans[n-2] = com[make_pair(ans[n-2] , ans[n-1])] ;
					ans.pop_back();
				}
			}
			if(ans.size() >= 2){
				int n = ans.size() ;
				for(int iw = 0 ; iw+1 < ans.size() ; iw++)
					if(res.count(make_pair(ans[iw] , ans[n-1]))){
						ans.clear();
						break ;
					}
			}
		}

		ostringstream os ;
		for(int i=0;i+1 < ans.size();i++)
			os << ans[i] << ", " ;
		if(ans.size())
			os << ans[ans.size()-1] ;

		string fRes = os.str();

		fRes = "[" + fRes + "]" ; 

		cout << "Case #" << it << ": " << fRes << endl ;
	}
	return 0 ;
}
