#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <sstream>
using namespace std;

typedef long long ll;


int N, M;
int U[10], V[10];

vector<vector<int> > poly;

void update(int a, int b){
	vector<vector<int> > res;
	for(int i = 0; i < poly.size(); i++){
		vector<int>  g = poly[i];
		bool ok[2]={0,0};
		for(int j = 0; j < g.size(); j++){
			if(g[j]== a)ok[0] = true;
			if(g[j]== b)ok[1] = true;
		}

		if( !(ok[0] && ok[1]) ){
			res.push_back(g);
			continue;
		}

		for(int j = 0; j < g.size(); j++){
			if(g[j] == a){
				vector<int> son;
				for(int k = j; g[(k) % g.size() ] != b; k++){
					son.push_back( g[(k) % g.size() ] );
				}
				son.push_back( b );
				if( son.size() > 2)res.push_back( son );
			}

			if(g[j] == b){
				vector<int> son;
				for(int k = j; g[(k) % g.size() ] != a; k++){
					son.push_back( g[(k) % g.size() ] );
				}
				son.push_back( a );
				if( son.size() > 2)res.push_back( son );
			}
		}
	}

	poly = res;
}

int best, color;
int method[10], bestM[10];

void dfs(int dep){
	if(dep == N){
		int chk = -1;
		for(int i = 0; i < poly.size(); i++){
			bool visit[10];
			memset(visit, 0, sizeof(visit));
			for(int j = 0; j < poly[i].size(); j++){
				visit[ method[ poly[i][j]-1 ] ] = true;
			}
			int cnt = 0;
			for(int j = 0; j < 10; j++)if(visit[j])cnt++;
			if(chk != -1 && chk != cnt)return;
			chk = cnt;
		}
		
		if(chk > best){
			best = chk;
			for(int i = 0; i < 10; i++)
				bestM[i] = method[i];
		}

		return ;
	}


	for(int i = 0; i < color; i++){
		
		int pre = method[dep];
		method[dep] = i;
		
		dfs(dep + 1 );
		
		method[dep] = pre;
	}
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("ans.txt","w",stdout);
	
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		scanf("%d %d",&N, &M);
		for(int i = 0; i < M; i++)scanf("%d",&U[i] );
		for(int i = 0; i < M; i++)scanf("%d",&V[i] );
		
		poly.clear(); vector<int> tem;
		for(int i = 1; i <= N; i++)tem.push_back( i );
		poly.push_back(tem);
		
		for(int i = 0; i < M; i++){
			update(U[i], V[i]);
		}
		
		printf("Case #%d: ",cas);

		if(poly.size() == 1){
			printf("%d\n", N);	
			for(int i = 1; i <= N; i++){
				printf("%d",i);
				if(i == N )printf("\n"); else printf(" ");
			}
			continue;
		}
		
		color = 100;
		for(int i = 0; i < poly.size(); i++)color = min(color, (int)poly[i].size() );
		
		best = -1;
		dfs(0);
		int visit[10];
		for(int i = 0; i < 10; i++)visit[i] = 0;
		for(int i = 0; i < 10; i++)visit[ bestM[i] ] = 1;
		
		int cnt = 1;
		for(int i = 0; i < 10; i++)if(visit[i])visit[i] = cnt++;
		
		printf("%d\n", best );	
		for(int i = 0; i < N; i++){
			printf("%d",visit[ bestM[i] ]);
			if(i+1 == N )printf("\n"); else printf(" ");
		}
	}
}