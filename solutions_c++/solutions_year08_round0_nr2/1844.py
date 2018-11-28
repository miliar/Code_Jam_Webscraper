#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std ;

int main(){
	int T ;
	scanf("%d",&T) ;
	for(int tcase = 1 ; tcase <= T ; tcase++){
		int rt ,na,nb;
		scanf("%d %d %d" , &rt,&na,&nb) ;
		vector<pair<int,int> > tl ;
		for(int i = 0 ; i < na ; i++){
			int h,m ;
			scanf("%d:%d " , &h,&m) ;
			int t1 = h*60 + m ;
			scanf("%d:%d " , &h,&m) ;
			int t2 = h* 60 + m + rt ;
			tl.push_back(make_pair(t1,1)) ;
			tl.push_back(make_pair(t2,-2)) ;
		}
		for(int i = 0 ; i < nb ; i++){
			int h,m ;
			scanf("%d:%d" , &h,&m) ;
			int t1 = h*60 + m ;
			scanf("%d:%d" , &h,&m) ;
			int t2 = h* 60 + m + rt ;
			tl.push_back(make_pair(t1,2)) ;
			tl.push_back(make_pair(t2,-1)) ;
		}
		sort(tl.begin() , tl.end()) ;
		int ca =0 , cb = 0 , ta= 0 , tb=0 ;
		for(int i = 0 ; i < tl.size() ; i++){
			int e = tl[i].second ;
			if(e == 1) ca-- ;
			if(e == 2) cb-- ;
			if(e == -1) ca++ ;
			if(e == -2) cb++ ;
			if(ca < 0) ca++,ta++;
			if(cb < 0) cb++,tb++ ;
			//printf("%d,%d\n" , tl[i].first , tl[i].second) ;
		}
		printf("Case #%d: %d %d\n",tcase,ta,tb) ;
	}
}
