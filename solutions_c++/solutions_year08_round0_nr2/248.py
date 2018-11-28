#include <cstdio>
#include <algorithm>

using namespace std;

struct ev{
	int t;
	bool w;
	bool d;
	ev(int x, bool y, bool z):t(x), w(y), d(z){}
	ev(){}
};

struct s{
	bool operator()(const ev &a, const ev &b) const{
		if(a.t != b.t)
			return a.t < b.t;
		else
			return a.d < b.d;
	}
};

int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int tc=0; tc<tcs; ++tc){
		int t, na, nb;
		scanf("%d %d %d", &t, &na, &nb);
		ev *evs = new ev[(na+nb)*2];
		for(int i=0; i<na+nb; ++i){
			int h0, m0, h1, m1;
			scanf("%d:%d %d:%d", &h0, &m0, &h1, &m1);
			evs[i*2] = ev(h0*60+m0, i<na, true);
			evs[i*2+1] = ev(h1*60+m1+t, i>=na, false);
		}
		sort(evs, evs + 2*(na+nb), s());

		int is[2], erg[2];
		erg[0] = erg[1] = is[0] = is[1] = 0;
		for(int i=0; i<2*(na+nb); ++i){
			if(!evs[i].d)
				++is[evs[i].w];
			else{
				if(is[evs[i].w])
					--is[evs[i].w];
				else
					++erg[evs[i].w];
			}
		}
		printf("Case #%d: %d %d\n", tc+1, erg[1], erg[0]);
	}
}
