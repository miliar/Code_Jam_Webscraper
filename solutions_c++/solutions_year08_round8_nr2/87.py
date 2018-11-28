#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
#define MP make_pair
#define FS first
#define SD second

vector< pair<int,int> > farby[500];
map<string,int> M;
vector< pair<int,int> > L;

int count(){
	sort(L.begin(),L.end());
	
	int ret = 0;
	int ost = 1;
	int naj = -1;
	FOR(i,0,SZ(L)){
		if(L[i].FS>ost){
			if(naj==-1) return 1000000;
			ret++;
			ost = naj;
			if(ost==10001) return ret;
			i--;
			naj = -1;
			continue;
		}

		if(L[i].SD+1>naj && L[i].SD+1>ost) naj=L[i].SD+1;
	}

	if(naj==10001) return ret+1;
	else return 1000000;
}

int main(){
	int T;
	cin>>T;
	FORE(tt,1,T){
		FOR(i,0,500) farby[i].clear();
		M.clear();
		int N,ind =0;
		cin>>N;
	
		FOR(i,0,N){
			string s;
			cin>>s;
			if(M.find(s)==M.end()) M[s]=ind++;
			int a,b;
			cin>>a;
			cin>>b;
			
			farby[M[s]].push_back(MP(a,b));
		}
		int best = 1000000;
		if(ind<3) ind = 3;
		for(int i=0;i<ind;i++) for(int j=i+1;j<ind;j++) for(int z=j+1;z<ind;z++){
			L.clear();
			FOR(it,0,SZ(farby[i])) L.push_back(farby[i][it]);
		   FOR(it,0,SZ(farby[j])) L.push_back(farby[j][it]);
			FOR(it,0,SZ(farby[z])) L.push_back(farby[z][it]);
			int a = count();
			if(a<best) best = a;
		}
		if(best==1000000) printf("Case #%d: IMPOSSIBLE\n",tt);
		else printf("Case #%d: %d\n",tt,best);
	}
}
