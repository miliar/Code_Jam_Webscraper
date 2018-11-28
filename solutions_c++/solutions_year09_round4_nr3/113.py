#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

//BipartiteMatching
#define MAXV1 110
#define MAXV2 110

struct BipartiteMatching{
	int V1,V2;
	bool graph[MAXV1][MAXV2];
	int prev[MAXV2];
	bool used[MAXV1];
	
	BipartiteMatching(int v1, int v2){
		V1 = v1; V2 = v2;
		int i,j; REP(i,V1) REP(j,V2) graph[i][j] = false;
	}
	
	void add_edge(int x, int y){
		graph[x][y] = true;
	}

	bool dfs(int v){
		int i;
		used[v] = true;
		REP(i,V2) if(graph[v][i] && (prev[i] == -1 || (!used[prev[i]] && dfs(prev[i])))) {prev[i] = v; return true;}
		return false;
	}
	
	int matching(void){
		int i,j,ans=0;
		REP(i,V2) prev[i] = -1;
		REP(i,V1){
			REP(j,V1) used[j] = false;
			if(dfs(i)) ans++;
		}
		return ans;
	}
};

int N,K;
int price[110][30];
vector <pair <int, int> > p;

int func(void){
	int i,j,k;
	
	p.clear();
	REP(i,N){
		int sum = 0;
		REP(j,K) sum += price[i][j];
		p.push_back(make_pair(sum,i));
	}
	sort(p.begin(),p.end());
	
	BipartiteMatching bip(N,N);
	REP(i,N) REP(j,N){
		int v1=p[i].second,v2=p[j].second;
		REP(k,K) if(price[v1][k] >= price[v2][k]) break;
		if(k == K) bip.add_edge(i,j);
	}
	
	int ans = N - bip.matching();
	return ans;
}

int main(void){
	int test,T,i,j;
	
	cin >> T;
	REP(test,T){
		cin >> N >> K;
		REP(i,N) REP(j,K) scanf("%d",&price[i][j]);
		int ans = func();
		gcj_print(ans);
	}
	
	return 0;
}
