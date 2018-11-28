#include<cassert>
#include<algorithm>
#include<cstring>
#include<cctype>
#include<cmath>
#include<functional>
#include<cerrno>
#include<iomanip>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>
#include<list>
//#include<gmpxx.h>
using namespace std;
#define sz(x) ((int)(x.size()))
#define mp make_pair
#define pb push_back
#define fr(k,y,z) for(int k=(y);k<=(z);k++)
#define fo(k,z) for(int k = 0;k<(z);k++)
#define foa(k,x) fo(k,sz(x))
#define all(x) (x).begin(),(x).end()
#define iall(I,x) for(typeof((x).begin()) I = (x).begin(); I != (x).end();++I)
const char *IMP = "IMPOSSIBLE";
struct Bool{
	int M;
	bool V;
	vector<bool> g,c;
	vector<bool> leaf;
	vector<int> memo[2];
	int N;
	static const int INF = 10009;
	int dps(int node,bool want){
		if(node > N){
			assert(node-N-1 < sz(leaf));
			if(leaf[node-N-1] == want) return 0;
			return INF;
		}

		int &m = memo[want][node];
		if(m != -1) return m;

		int c1idx = 2 * (node+1)     - 1;
		int c2idx = 2 * (node+1) + 1 - 1;

		m = INF;
		if(g[node]){ //AND
			if(want){
				m = min(m, dps(c1idx,true) + dps(c2idx,true));
				if(c[node]){
					m = min(m, 1 + dps(c1idx,false) + dps(c2idx,true));
					m = min(m, 1 + dps(c1idx,true) + dps(c2idx,false));
					m = min(m, 1 + dps(c1idx,true) + dps(c2idx,true));
				}
			}else{
				m = min(m, dps(c1idx,false) + dps(c2idx,false));
				m = min(m, dps(c1idx,false) + dps(c2idx,true));
				m = min(m, dps(c1idx,true) + dps(c2idx,false));
				if(c[node]){
					m = min(m, 1 + dps(c1idx,false) + dps(c2idx,false));
				}
			}
		}else{ //OR
			if(want){
				m = min(m, dps(c1idx,true) + dps(c2idx,true));
				m = min(m, dps(c1idx,true) + dps(c2idx,false));
				m = min(m, dps(c1idx,false) + dps(c2idx,true));
				if(c[node]){
					m = min(m, 1 + dps(c1idx,true) + dps(c2idx,true));
				}
			}else{
				m = min(m, dps(c1idx,false) + dps(c2idx,false));
				if(c[node]){
					m = min(m, 1 + dps(c1idx,false) + dps(c2idx,false));
					m = min(m, 1 + dps(c1idx,true) + dps(c2idx,false));
					m = min(m, 1 + dps(c1idx,false) + dps(c2idx,true));
				}
			}
		}
//		cout << node << ' ' << want << " Return " << m << endl;
		return m;
	}

	void Go(){
//		foa(k,g) cout << g[k] << ' ' << c[k] << endl;
//		foa(k,leaf) cout << leaf[k] << endl;
		N = (M-1)/2 - 1;
		memo[0].assign(sz(g)+1,-1);
		memo[1].assign(sz(g)+1,-1);
//		cout << "We want " << V << endl;
		int m = dps(0,V);
		if(m >= INF) cout << IMP;
		else cout << m;
	}
};

int main()
{
	string line;
	getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		Bool b;
		{istringstream iss(line); iss >> b.M >> b.V;}
		fo(k,b.M){
			if(!getline(cin,line)) throw int();
			istringstream iss(line);
			if(k+1 <= (b.M-1)/2){
				bool a,d;
				iss >> a >> d;
				b.g.pb(a); b.c.pb(d);
			}else{
				bool a;
				iss >> a;
				b.leaf.pb(a);
			}
		}
		cout << "Case #" << ca << ": ";
		b.Go();
		cout << endl;
	}
}
