#include <cstdio>
#include <vector>
#include <algorithm>

#define SZ(x) ((int)(x).size())

using namespace std;

struct event{
	int t, e, p;
	event(int t, int e, int p):t(t),e(e),p(p){}
};

bool usp(const event &a, const event &b){
	if ( a.t != b.t ) return a.t < b.t;
	if ( a.e != b.e ) return a.e < b.e;
	if ( a.p != b.p ) return a.p < b.p;
}

int main(){
	int tc =0, tcc = 0;
	for(scanf("%d", &tc); tc; tc--){
		int t, na, nb;
		scanf("%d\n%d %d\n", &t, &na, &nb);

		vector<event> time;

		for ( int i = 0; i < na; i++ ){
			int dh, dm, ah, am;
			scanf("%d:%d %d:%d\n", &dh, &dm, &ah, &am);
			int d = dh * 60 + dm;
			int s = ah * 60 + am + t;

			time.push_back(event(d, 1, 0));
			time.push_back(event(s, 0, 1));
		}

		for ( int i = 0; i < nb; i++ ){
			int dh, dm, ah, am;
			scanf("%d:%d %d:%d\n", &dh, &dm, &ah, &am);
			int d = dh * 60 + dm;
			int s = ah * 60 + am + t;

			time.push_back(event(d, 1, 1));
			time.push_back(event(s, 0, 0));
		}

		sort(time.begin(), time.end(), usp);

		int treba[2] = {0};
		int ima[2] = {0};

		for (int i = 0; i < SZ(time); i++){
			if ( time[i].e == 0 ){
				ima[time[i].p]++;
			}
			else {
				if ( ima[time[i].p] == 0 ) treba[time[i].p]++;
				else ima[time[i].p]--;
			}
		}

		printf("Case #%d: %d %d\n", ++tcc, treba[0], treba[1]);
	}
	return 0;
}
