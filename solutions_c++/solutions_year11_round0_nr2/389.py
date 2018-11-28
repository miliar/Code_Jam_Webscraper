#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

map<pair<char,char>,char> c;
set<pair<char,char> > d;
char buf[200];

int main(){
	int T;
	scanf("%d",&T);
	FOR(tc,1,T+1){
		c.clear();
		d.clear();
		int C;
		scanf("%d",&C);
		FOR(i,0,C){
			scanf("%s",buf);
			c[make_pair(buf[0],buf[1])]=buf[2];
			c[make_pair(buf[1],buf[0])]=buf[2];
		}
		int D;
		scanf("%d",&D);
		FOR(i,0,D){
			scanf("%s",buf);
			d.insert(make_pair(buf[0],buf[1]));
			d.insert(make_pair(buf[1],buf[0]));
		}
		int N;
		scanf("%d%s",&N,buf);
		vector<char> st = vector<char>();
		FOR(i,0,N){
			char n = buf[i];
			while(!st.empty()){
				pair<char,char> pc = make_pair(n,st[sz(st)-1]);
				if(c.find(pc)==c.end())break;
				n = c[pc];
				st.pop_back();
			}
			st.push_back(n);
			FOR(i,0,sz(st))FOR(j,i+1,sz(st)){
				if(d.find(make_pair(st[i],st[j]))!=d.end()){
					st.clear();
				}
			}
		}
		printf("Case #%d: [",tc);
		FOR(i,0,sz(st)){
			if(i)printf(", ");
			printf("%c",st[i]);
		}
		printf("]\n");
	}
	return 0;
}
