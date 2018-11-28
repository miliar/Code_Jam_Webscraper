#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

struct state {
	bool mark[103];
	int releases;
	int sum;
	
	state( bool mark[103]=NULL, int releases=0, int sum=0 ): releases(releases), sum(sum) {
		for (int i = 0; i < 103; i++) this->mark[i] = mark[i];
	}
	
	friend bool operator < (state a, state b) {
		return a.sum > b.sum;
	}
};


int casos, P, Q;
int choices[103];
int sum;
int caso;
bool mark[103];
priority_queue<state> heap;

void process() {
	while( !heap.empty() ) heap.pop();
	
	memset(mark,false,sizeof(mark));
	state ini = state(mark,0,0);
	
	
	heap.push(ini);
	
	while (!heap.empty()) {
		state now = heap.top();
		heap.pop();
		
		if (now.releases==Q) {
			caso++;
			printf("Case #%d: %d\n",caso,now.sum); fflush(stdout);
			break;
		}
		
		for (int i = 0; i < Q; i++) {
			if (!now.mark[ choices[i] ]) {
				state next = state( now.mark, now.releases+1, now.sum );
				next.mark[ choices[i] ] = true;
				sum = 0;
				for (int n = choices[i]-1; n > 0; n--,sum++) {
					if (next.mark[n]) break;
				}
				for (int n = choices[i]+1; n <= P; n++, sum++) {
					if (next.mark[n]) break;
				}
				next.sum += sum;
				heap.push( next );
			}
		}
		
	}
	
}


void read() {
	memset(choices,0,sizeof(choices));
	scanf("%d %d",&P,&Q);
	for (int i = 0; i < Q; i++) {
		scanf("%d",&choices[i]);
	}
}

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	scanf("%d",&casos);
	caso = 0;
	
	while (casos--) {
		read();
		process();
	}
	
	
	return 0;
}
