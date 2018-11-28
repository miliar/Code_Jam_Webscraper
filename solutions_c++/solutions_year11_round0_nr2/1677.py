#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int N = 1000010;
int n;
map<pair<char,char>, char> com;
set<char> oppo[256]; // z kim sa opposed
map<char,int> zb; // teraz w liscie co jest, (znak, ileRazyWystepuje)

main(){
	int t;
	cin >> t;
	FOR(q,1,t){
		string pom;
		int comb,opposite;
		cin >> comb;
		while(comb--){
			cin >> pom;
			com[make_pair(pom[0],pom[1])] = pom[2];
			com[make_pair(pom[1],pom[0])] = pom[2];
		}
		cin >> opposite;
		while(opposite--){
			cin >> pom;
			oppo[pom[0]].insert(pom[1]);
			oppo[pom[1]].insert(pom[0]);
		}
		int N;
		cin >> N;
		string invoke;
		list<char> result;
		cin >> invoke;
		REP(i,N){
			if(result.empty()){
				result.PB(invoke[i]);
				zb[invoke[i]]++;
			}
			else{
				if(com.find(make_pair(result.back(),invoke[i])) != com.end()){
					zb[result.back()]--;
					result.back() = com[make_pair(result.back(),invoke[i])];
					zb[result.back()]++;
				}
				else{
					bool toClear = false;
					for(set<char>::iterator p = oppo[invoke[i]].begin();p!=oppo[invoke[i]].end();p++){
						if(zb[*p] > 0){
							toClear = true;
						}
					}
					if(toClear){
						result.clear();
						zb.clear();
					}
					else{
						zb[invoke[i]]++;
						result.PB(invoke[i]);
					}
				}
			}
		}
		cout << "Case #"<<q << ": ";
		if(result.empty())
			cout << "[]\n";
		else{
			list<char>::iterator p = result.begin();
			cout << "["<<*p;
			p++;
			for(;p != result.end();p++){
				cout << ", " << *p;
			}
			cout << "]\n";
		}
		REP(i,256)
			oppo[i].clear();
		com.clear();
		zb.clear();
		result.clear();
	}
	return 0;
}
