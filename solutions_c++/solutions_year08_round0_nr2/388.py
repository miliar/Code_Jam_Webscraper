// g++ -O3 -o trains trains.cpp
// Bertrand Nouvel Google Jam Qualif 2008

#include <map>
#include <cmath>

std::map< int , int , std::less<int> > deparr_at_a;
std::map< int , int , std::less<int> > deparr_at_b;

int read_time() {
	int h;
	int m;
	scanf("%02d:%02d",&h,&m);
	return h*60+m;
}


int main(int argc, char ** argv) {
	int depa,depb;int ca,cb;
	std::map< int , int , std::less<int> >::iterator it;
	int dep,arr,T=0;

	scanf("%d",&T);	

	for (int t=0; t<T; t++) {
		// a->b
		deparr_at_a.clear();
		deparr_at_b.clear();
		int delay,NA,NB;
		scanf("%d",&delay);	
		scanf("%d %d",&NA,&NB);	
		for (int na=0; na<NA; na++) {
			dep=read_time(); 
			arr=read_time()+delay;  
			if ((it=deparr_at_a.find(dep))!=deparr_at_a.end()) {
				it->second-=1;
			}
			else {
				deparr_at_a[dep]=-1;
			}
			if ((it=deparr_at_b.find(arr))!=deparr_at_b.end()) {
				it->second+=1;
			}
			else {
				deparr_at_b[arr]=1;
			}
		}

		for (int nb=0; nb<NB; nb++) {
			dep=read_time(); 
			arr=read_time()+delay;  
			if ((it=deparr_at_b.find(dep))!=deparr_at_b.end()) {
				it->second-=1;
			}
			else {
				deparr_at_b[dep]=-1;
			}
			if ((it=deparr_at_a.find(arr))!=deparr_at_a.end()) {
				it->second+=1;
			}
			else {
				deparr_at_a[arr]=1;
			}
		}
	
	
		depa=0; ca=0;
		for (it=deparr_at_a.begin();it!=deparr_at_a.end();++it) {
			ca+=it->second;
			if (ca<depa) depa=ca;
		}

		depb=0; cb=0;
		for (it=deparr_at_b.begin();it!=deparr_at_b.end();++it) {
			cb+=it->second;
			if (cb<depb) depb=cb;
		}

		printf("Case #%d: %d %d\n",t+1,-depa,-depb);
	}
} 

