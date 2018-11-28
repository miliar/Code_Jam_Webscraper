#include <iostream>
#include <algorithm>
#include <vector>
#define pb push_back

using namespace std;

const int MaxN= 10;
int n, m, w, num;
int v[MaxN], u[MaxN], c[MaxN];
bool mark[MaxN];
vector<int> col;
vector<int> g[MaxN];

inline void setC(int now){
	memset(c, 0, sizeof c);
	int i= 0;
	while(now>0){
		c[i++]= now%w;
		now/= w;
	}
}
/*******************************/
inline int numCol(){
	int tmp[MaxN];
	for (int i=0 ; i<n ; i++)
		tmp[i]= c[i];
	sort(tmp, tmp+n);
	int res= unique(tmp, tmp+n) - tmp;
	return res;
}
/*******************************/
inline int pwr(int a, int b){
	int res= 1;
	while(b--)
		res*= a;
	return res;
}
/******************************/
inline bool dfs(int v, int par= -1){
//	cout << v+1 << endl;
	bool insert= true;
	for (unsigned int i=0 ; i<col.size() ; i++)
		if (col[i]==c[v]){
			insert= false;
			break;
		}
	if (insert)
		col.pb( c[v] );
	mark[v]= true;
	for (int i=0 ; i<g[v].size() ; i++){
		int u= g[v][i];
		if (u!=par && mark[u] && col.size()!=num){
			mark[v]= false;
			return false;
		}
		if (!mark[u] && !dfs(u, v)){
			mark[v]= false;
			return false;
		}
	}
	if (insert)
		col.pop_back();
	mark[v]= false;
	return true;
}
/******************************/
inline bool satisfy(){
	for (int i=0 ; i<n ; i++){
		memset(mark, 0, sizeof mark);
		col.clear();
		if (!dfs(i))
			return false;
	}
	return true;
}
/*******************************/
inline bool good(){
	int tmp[MaxN];
	for (int i=0 ; i<n ; i++)
		tmp[i]= c[i];
	sort(tmp, tmp+n);
	int k= unique(tmp, tmp+n) - tmp;
	for (int i=0 ; i<k ; i++)
		if (tmp[i]!=i)
			return false;
	return true;
}
/******************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		memset(mark, 0, sizeof mark);
		for (int i=0 ; i<MaxN ; i++)
			g[i].clear();
		cout << "Case #" << t << ": ";
		cin >> n >> m;
		for (int i=0 ; i<m ; i++){
			cin >> v[i];
			v[i]--;
		}
		for (int i=0 ; i<m ; i++){
			cin >> u[i];
			u[i]--;
		}
		for (int i=0 ; i<n ; i++){
			g[i].pb( (i+1)%n );
			g[ (i+1)%n ].pb(i);
		}
		for (int i=0 ; i<m ; i++){
			g[ v[i] ].pb( u[i] );
			g[ u[i] ].pb( v[i] );
		}
		if (m==0){
			cout << n << endl;
			for (int i=0 ; i<n ; i++)
				cout << i+1 << ' ';
			cout << endl;
			continue;
		}
		
		w= (n+1)/2 +1;
		int stat= pwr(w, n);
		int maxi= 0;
		int resStat= 0;
		for (int i=0 ; i<stat ; i++){
			setC(i);
			if (!good())
				continue;
			num= numCol();
			if (num>maxi && satisfy()){
				maxi= num;
				resStat= i;
			}
		}
		cout << maxi << endl;
		setC(resStat);
		for (int i=0 ; i<n ; i++)
			cout << c[i]+1 << ' ';
		cout << endl;
	}
	return 0;
}