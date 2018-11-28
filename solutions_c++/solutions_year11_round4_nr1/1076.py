# include <cstdio>
# include <cstring>
# include <string>
# include <vector>
# include <set>
# include <map>
# include <algorithm>
# include <queue>
# include <stack>
# include <cassert>
# include <ctime>
# include <cstdlib>

using namespace std;

int T;
int X, S, R, t, N;

vector< pair< int, pair<int, int > > > vet;
vector< pair<int, int> > extra;
vector< pair<int, pair<int, int > > > v;

int main (void){
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		vet.clear();
		for(int i = 0; i < N; i++){
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			vet.push_back(make_pair(b, make_pair(e,w)));
		}		
		sort(vet.begin(), vet.end());
		
		int last = 0;
		extra.clear();
		for(int i = 0 ; i < N; i++){
			int in = vet[i].first;
			if( in > last ){
				extra.push_back(make_pair(last, in));
			}
			last = vet[i].second.first;
		}
		
		if( X > last ){
			extra.push_back(make_pair(last, X));
			last = X;
		}
		
		int sz = extra.size();
		v.clear();
		for(int i = 0 ; i < N; i++){
			int b = vet[i].first;
			int e = vet[i].second.first;
			int w = vet[i].second.second;
			v.push_back(make_pair(w,make_pair(b,e)));
		}
		
		for(int i = 0 ; i < sz; i++){
			v.push_back(make_pair(0,make_pair(extra[i].first, extra[i].second)));
		}
		
		sort(v.begin(), v.end());
		
		sz = v.size();
		
		for(int i = 0 ; i < sz; i++){
		//	printf("%d %d %d\n", v[i].first, v[i].second.first, v[i].second.second);
		}
		// printf("%d %d\n", S, R);
		double disp = t;
		double tempo = 0.0;
		for(int i = 0 ; i < sz; i++){
			int dif = v[i].second.second - v[i].second.first; // distancia a percorrer
			int w = v[i].first;
			double t1 = (double) dif/(R+w); // tempo para percorrer correndo;
			if( t1 <= disp){
				// printf("%d %f %f\n", i, t1, disp);
				disp  -= t1;
				tempo += t1;
			}
			else{
				double dist = (R+w)*disp;
				double resto = (double) dif - dist;
				tempo += (double) disp;
				tempo += (resto)/(S + w);
				disp = 0;
			}
			
		}
		
		printf("Case #%d: %.9f\n", tc, tempo);
	}
	return 0;
}