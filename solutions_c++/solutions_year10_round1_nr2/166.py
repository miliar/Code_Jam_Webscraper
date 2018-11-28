#include <numeric>
#include <cstring>
#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <deque>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;
typedef pair<int, pair<int, int> > pii;
#define mp(a, b, c) make_pair(a, make_pair(b, c))
#define fst first
#define snd second
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
int D, I, M, N;
vector<int> a;
int dist[110][300];
int inf = 1 << 30;

int solve(){
	for(int i = 0; i < 110; i++) for(int j = 0; j < 300; j++) dist[i][j] = inf;
	//shift de 1
	dist[0][0] = 0;
	set<pii> cola;
	cola.insert(mp(0, 0, -1));
	
	while(!cola.empty()){
		int d = cola.begin()->first;
		int pos = cola.begin()->second.first;
		int anterior = cola.begin()->second.second;
		cola.erase(cola.begin());
		if(d > dist[pos][anterior + 1]) continue;
		if(pos == N) return d;
		
		int nd;
		//elimina
		nd = d + D;
		if(dist[pos + 1][anterior + 1] > nd){
			dist[pos + 1][anterior + 1] = nd;
			cola.insert(mp(nd, pos + 1, anterior));
		}	
		//continue;
		
		//salta 
		if(anterior != -1 && abs(a[pos] - anterior) <= M){ // puede
			nd = d;
			if(dist[pos + 1][a[pos] + 1] > nd){
				dist[pos + 1][a[pos] + 1] = nd;
				cola.insert(mp(nd, pos + 1, a[pos]));
			}
		}
		//modifica
		for(int val = 0; val <= 255; val++){
			if(anterior != -1 && abs(val - anterior) > M)
					continue;
			nd = d + abs(a[pos] - val);
			
			if(dist[pos + 1][val + 1] > nd){
				dist[pos + 1][val + 1] = nd;
				cola.insert(mp(nd, pos + 1, val));
			}	
		}	
		
		//inserta atras del actual
		for(int val = 0; val <= 255; val++) if(anterior != -1){
			if(abs(val - anterior) > M)
					continue;
			nd = d + I;
			
			if(dist[pos][val + 1] > nd){
				dist[pos][val + 1] = nd;
				cola.insert(mp(nd, pos, val));
			}	
		}	
				
	}	
	
	return -1;
}

int main(){
	int tt;
	cin >> tt;
	for(int casos = 1; casos <= tt; casos++){
		cin >> D >> I >> M >> N;
		a.resize(N);
		for(int i = 0; i < N; i++){
			cin >> a[i]; 
		}
		
		cout <<"Case #"<<casos<<": "<< solve() << endl;
	}
}
