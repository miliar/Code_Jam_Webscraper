#include <iostream>
#include <vector>
#include <algorithm>
using namespace std ;
bool possible(long double time, int d, vector<pair<int,int> >& v){
	long double lastx = v[0].first - time - 1 ;
	vector<double> ans ;
	for(int i = 0 ; i < v.size() ; i++){
		long double p = v[i].first ;
		int n = v[i].second ;
		long double left = p - time ;
		if(left < lastx) left = lastx ;
		long double right = left + (n-1) * d ;
		if(left - p > time || right - p > time) return false ;
		lastx = right + d ;
		ans.push_back(left) ;
	}
	return true ;
}
int main(){
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int c, d; cin >> c >> d ;
		vector<pair<int, int> > v(c) ;
		for(int i = 0 ; i < c ; i++){
			int tp, tv ; cin >> tp >> tv ;
			v[i] = pair<int,int>(tp,tv) ;
		}
		sort(v.begin(), v.end()) ;
		long double s=0, e=1e13 ;
		while(e - s > 1e-7){
			long double m = (e+s) / 2 ;
			if(possible(m,d,v)) e = m ;
			else s = m ;
		}
		cout << "Case #" << t << ": " << s << endl ;
	}
	
}
