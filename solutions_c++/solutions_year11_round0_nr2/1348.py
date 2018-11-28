#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

int main(){
	//freopen("a.in", "r", stdin);
	//freopen("B-small-attempt0.in","r",stdin); freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);
	int t, C, D, N;
	string s;
	scanf("%d", &t);
	for(int cas=1; cas<=t ;cas++){
		scanf("%d", &C);
		map<pair<char,char>, char> mc;
		F(i, C){
			cin>>s;
			mc[MP(s[0], s[1])] = s[2];
			mc[MP(s[1], s[0])] = s[2];
		}
		scanf("%d", &D);
		vector<string> cd(D);
		F(i, D) cin>>cd[i];
		scanf("%d", &N);
		cin>>s;
		vector<char> sol;
		F(i, N){
			if(sol.S) if(mc.find(MP(sol[ sol.S-1 ], s[i])) != mc.end()){
				sol[ sol.S-1 ] = mc[ MP(sol[ sol.S-1 ], s[i]) ];
				continue;
			}
			F(j, D){
				if(cd[j][0] == s[i]){
					if(count(ALL(sol), cd[j][1])){
						sol.clear();
						goto salto;
					}
				}
				else if(cd[j][1] == s[i]){
					if(count(ALL(sol), cd[j][0])){
						sol.clear();
						goto salto;
					}
				}
			}
			sol.PB(s[i]);
			salto:;
		}
		printf("Case #%d: [", cas);
		F(i, sol.S){
			if(i) printf(", ");
			cout<<sol[i];
		}
		printf("]\n");
	}
}

