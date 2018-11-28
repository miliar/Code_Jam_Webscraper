#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int,int> par;

const int MXN = 10001;
char bio[MXN][MXN];
char flag = 0;
int l[MXN], d[MXN];

void solve(){
	flag++;
	
	int n, D;
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		scanf("%d %d", &d[i], &l[i]);		
	}
	scanf("%d", &D);
	
	queue <par> q;
	q.push(par(0,0)); //first oznacava trenutnu, a second prethodnu
	int dist, height, i;
	while(!q.empty()){
		par vrh = q.front();
		q.pop();
		if(bio[vrh.first][vrh.second] == flag) continue;
		bio[vrh.first][vrh.second] = flag;
//		printf( "%d %d\n", vrh.first, vrh.second);
		dist = abs(d[vrh.first]-d[vrh.second]);
		height = min(dist, l[vrh.first]); //visina na drugoj lijani
		if(vrh.first == 0 && vrh.second == 0) height = d[0];

		if(d[vrh.first]+height >= D){
			printf("YES\n");
			return;
		}
		
		for(i = 0; i < n; i++){
			if(abs(d[i] - d[vrh.first]) <= height){
				q.push(par(i, vrh.first));
			}
		}
	}
	
	printf( "NO\n" );
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		printf( "Case #%d: ", i );
		solve();
	}
	return 0;
}