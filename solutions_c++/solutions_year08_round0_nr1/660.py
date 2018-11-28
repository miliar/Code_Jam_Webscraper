#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define cs c_str()
#define pb push_back
#define sz size()
#define INF (int)1e9+1

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
//typedef long long LL;
typedef long double LD;

VS engines,queries;
VVI occur;
VI pos;

int main(){

	ifstream fin("input1.txt");
	ofstream fout("output1.txt");
	int n;
	fin>>n;
	FOR(i,1,n+1){
		int ans=0,s,q;
		engines.clear();
		queries.clear();
		pos.clear();
		REP(j,occur.sz)	occur[j].clear();
		occur.clear();
		fin>>s;fin.get();
		
		REP(j,s){
			string engine="";
			char en[105];
			fin.getline(en,105);
			
			for(int k=0;en[k];k++)	engine+=en[k];
			engines.pb(engine);
		}
		fin>>q;fin.get();
		REP(j,q){
			string query="";
			char en[105];
			fin.getline(en,105);
			for(int k=0;en[k];k++)	query+=en[k];
    		
			queries.pb(query);
		}
		
		occur.resize(s);
		pos.resize(s,0);
		REP(j,s){
			REP(k,q){
				if(queries[k]==engines[j])
					occur[j].pb(k);
			}
			occur[j].pb( 1000000);
		}
		int tobetaken=-1,engtaken=-1;
		while(1){
			REP(j,occur.sz){
				if(occur[j][ pos[j] ]>tobetaken && j!=engtaken){
					tobetaken= occur[j][ pos[j] ];
					engtaken=j;
				}
			}
		
			REP(j,occur.sz){
				int k;
				for(k=pos[j];k<occur[j].sz && occur[j][k]<tobetaken;k++);
				pos[j]=k;
			}
			if(tobetaken>=1000000)	break;
			ans++;
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;	   
	}
	return 0;
}

