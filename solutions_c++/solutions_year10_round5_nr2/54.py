#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Edge{
public:
	int cur; int cost;
	Edge(int cur, int cost) : cur(cur), cost(cost) {}
	bool operator < (const Edge &e) const { return cost > e.cost; }
};

int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		long long L; int N; cin >> L >> N;
		int B[100];
		int step[100001];
		for(int i=0;i<N;i++) cin >> B[i];
		sort(B, B+N);
//		int INF = B[N-1]+1;
//		for(int i=0;i<B[N-1];i++) step[i] = INF;
		memset(step, -1, sizeof(step));
		priority_queue< Edge > qu; qu.push(Edge(0,0));
		while(!qu.empty()){
			Edge e = qu.top(); qu.pop();
			int cur = e.cur; int cost = e.cost;
			if(step[cur]!=-1) continue;
			step[cur] = cost;
			for(int i=0;i<N-1;i++)
				qu.push(Edge((cur+B[i])%B[N-1], cost+(cur+B[i]<B[N-1])));
		}
		/*
		for(int i=0;i<B[N-1];i++){
			for(int j=0;j<B[N-1];j++)
				if(step[j]==INF)
				for(int k=0;k<N-1;k++)
					if(step[(j+B[N-1]-B[k])%B[N-1]]!=INF)
						step[j] = min(step[j], step[(j+B[N-1]-B[k])%B[N-1]]+(j>=B[k]));
		}
		*/
		if(step[L%B[N-1]] != -1) printf("Case #%d: %lld\n", test, L/B[N-1]+step[L%B[N-1]]);
		else printf("Case #%d: IMPOSSIBLE\n", test);
	}
}

/*
// for small
int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		long long L; int N; cin >> L >> N;
		int B[100];
		int step[100001];
		for(int i=0;i<N;i++) cin >> B[i];
		sort(B, B+N);
		int INF = B[N-1]+1;
		for(int i=0;i<B[N-1];i++) step[i] = INF;
		step[0] = 0;
		for(int i=0;i<B[N-1];i++){
			for(int j=0;j<B[N-1];j++)
				if(step[j]==INF)
				for(int k=0;k<N-1;k++)
					if(step[(j+B[N-1]-B[k])%B[N-1]]!=INF)
						step[j] = min(step[j], step[(j+B[N-1]-B[k])%B[N-1]]+(j>=B[k]));
		}
		if(step[L%B[N-1]] != INF) printf("Case #%d: %lld\n", test, L/B[N-1]+step[L%B[N-1]]);
		else printf("Case #%d: IMPOSSIBLE\n", test);
	}
}
*/