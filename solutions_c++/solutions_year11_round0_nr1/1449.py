#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cassert>
#include <utility>
using namespace std;
#define VAR(i,v) __typeof((v))i=(v)
#define FOREACH(i,v) for(VAR(i,(v).begin());i!=(v).end();i++)

static
int move_robot(int pos, int target, int dt) {
	assert(dt >= 0);

	// czy da radę dotrzeć?
	if(dt >= abs(pos-target))
		return target;

	// idź ile się da
	if(target > pos)
		return pos + dt;
	else
		return pos - dt;
}

int main() {
	int _T; scanf("%d",&_T);
	for(int _iT=1; _iT<=_T; _iT++) {
		int N;
		vector< pair<int,int> > sequence;
		// wczytaj
		{
			scanf("%d", &N);
			sequence.resize(N);
			char buf[30]; int x, y;
			for(int i=0;i<N;i++) {
				scanf("%s%d", buf, &y);
				x = (buf[0] == 'B')?1:0;
				sequence[i] = make_pair(x,y);
			}
		}
		// oblicz gdzie ma isc dalej z danego pola
		vector< int > next[2];
		next[0].resize(N);
		next[1].resize(N);
		{
			int nv[2];
			nv[0]=nv[1] = 0;
			for(int i=N-1; i>=0; i--) {
				next[0][i] = nv[0];
				next[1][i] = nv[1];
				nv[sequence[i].first] = sequence[i].second;
			}
		}
		// pętla symulacji
		int T = 0;
		{
			int pos[2];
			pos[0]=pos[1] = 1;
			for(int i=0; i<N; i++) {
				int who = sequence[i].first;
				int other = who^1;
				int where = sequence[i].second;
				// potrzeba jeszcze dojsc ile brakuje oraz wdusic guzik
				int dt = abs(pos[who] - where) + 1;
				// przesun roboty
				pos[who] = where;
				pos[other] = move_robot(pos[other], next[other][i], dt);
				// dolicz czas potrzebny
				T += dt;
			}
		}
		printf("Case #%d: %d\n", _iT, T);
	}

	return 0;
}
