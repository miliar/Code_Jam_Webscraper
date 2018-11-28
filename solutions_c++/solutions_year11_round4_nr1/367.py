#include <iostream>
#include <vector>
using namespace std ;
int main(){
	int T ; cin >> T ; 
	for(int c = 1 ; c <= T ; c++){
		int x, s, r, t, n ; cin >> x >>s >>r >> t >> n ;
		vector<int> b, e, w;
		int last = 0 ;
		while(n--){
			int b1, e1, w1 ; cin >> b1 >> e1 >> w1 ;
			b.push_back(last); e.push_back(b1); w.push_back(s) ;
			b.push_back(b1); e.push_back(e1); w.push_back(w1+s) ;
			last = e1 ;
		}
		b.push_back(last); e.push_back(x); w.push_back(s) ;
		vector< pair<int,int> > itvl ;
		for(int i = 0 ; i < w.size(); i++){
			itvl.push_back(pair<int,int>(w[i],i)) ;
		}
		sort(itvl.begin(),itvl.end());
		double rt = t ;
		double ans = 0 ;
		for(int i = 0 ; i < itvl.size() ; i++){
			int k = itvl[i].second ;
			double tt = (double)(e[k]-b[k]) / (w[k]+r-s) ;
			if(tt > rt)
				tt = rt ;
			rt -= tt ;
			ans += tt + (double)(e[k]-b[k] - (w[k]+r-s) * tt ) / (w[k]) ;
		}
		printf("Case #%d: %.6f\n", c, ans) ; 
	}
}
