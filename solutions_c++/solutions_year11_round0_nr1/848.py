#include <cstdio>
#include <algorithm>
using namespace std;

typedef pair<char, int> op;
typedef pair<int,int>  pos;

int N;
op ops[109];

int solve(){
	pos blue(1,0), orange(1,0);
	int time = 0;
	for(int i=0; i<N; i++){
		int np = ops[i].second;
		if(ops[i].first == 'B'){
			int dist = abs(blue.first - np);
			int nt = dist + blue.second + 1;
			time = max(time + 1, nt);
			blue = pos(np, time);
		}
		else{
			int dist = abs(orange.first - np);
			int nt = dist + orange.second + 1;
			time = max(time + 1, nt);
			orange = pos(np, time);
		}
	}
	return time;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){
		scanf("%d ",&N);
		for(int i=0; i<N; i++){
			char ch;
			int b;
			scanf("%c %d ",&ch, &b);
			ops[i] = op(ch, b);
		}
		printf("Case #%d: %d\n",c,solve());
	}
}
