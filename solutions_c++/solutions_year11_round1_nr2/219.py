#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
const int MAXN = 10000;
int N, M;
vector<string> dict;
string alp;
bool has[MAXN][30];
map<string, int> m;
bool rev[15];
int get(string s){
	vector<string> d;
	REP(i, SIZE(dict)) if(SIZE(dict[i]) == SIZE(s)) d.push_back(dict[i]);
	int ret = 0;
	for(int i = 0; i < SIZE(alp); i ++){
		//bool fin = true;
		//REP(j, SIZE(s))if(!rev[j]) fin = false;
		//if(fin) return ret;
		char c = alp[i];
		bool find = false;
		REP(j, SIZE(d)){
			if(has[m[d[j]]][c-'a']) find = true;
		}
		if(!find) continue;
		bool ok = false;
		for(int j = 0; j < SIZE(s); j ++){
			if(s[j] == c){
				rev[j] = true;
				ok = true;
				for(int k = 0; k < SIZE(d); k ++){
					if(d[k][j] != c){
						d.erase(d.begin() + k);
						k --;
					}
				}
			}
			else{
				for(int k = 0; k < SIZE(d); k ++){
					if(d[k][j] == c){
						d.erase(d.begin() + k);
						k --;
					}
				}
			}
		}
		
		if(!ok){
			ret ++;
		}
		if(SIZE(d) == 1) break;
		
	}
	return ret;
}
string solve(){
	int ret = -1;
	string str = "";
	for(int i = 0; i < N; i ++){
		memset(rev, false, sizeof rev);
		int r = get(dict[i]);
		if(ret == -1 || (r > ret)){
			ret = r;
			str = dict[i];
		}
	}
	return str;
}
int main() {
	//freopen("B-small-attempt0.in", "r", stdin); 
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt111.out", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	freopen("B-small-attempt3.in", "r", stdin); freopen("B-small-attempt3.out", "w", stdout);
	
	//freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	
	int nT;
	cin>>nT;
	for (int t=1; t<=nT; t++) {
		printf("Case #%d: ", t);
		cin>>N>>M;
		m.clear();
		dict.clear();
		REP(i, N){
			memset(has[i], false, sizeof has[i]);
			string tmp;
			cin>>tmp;
			m[tmp] = i;
			REP(j, SIZE(tmp)) has[i][tmp[j] - 'a'] = true;
			dict.push_back(tmp);
		}
		REP(i, M - 1){
			cin>>alp;
			cout<<solve()<<" ";
		}
		cin>>alp;
		cout<<solve()<<endl;
	}
	return 0;
}
