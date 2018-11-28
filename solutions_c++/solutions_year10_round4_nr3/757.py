
#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

int main(){
	
	set<long long> s[2];
	int T, R, x1, x2, y1, y2;

	scanf("%d", &T);
	set<long long>::iterator ite;

	for(int testcase=1; testcase<=T; ++testcase){
		scanf("%d", &R);
		s[0].clear();
		s[1].clear();
		for(int r=0; r<R; ++r){
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int i=x1; i<=x2; ++i){
				for(int j=y1; j<=y2; ++j){
					s[0].insert((((long long)i)<<32)+j);
				}
			}
		}
		if(s[0].size() == 0){
			printf("Case #%d: 0\n", testcase);
			continue;
		}
		for(int t=1; ;++t){
			int u = (t+1)%2;
			int v = t%2;
			for(ite=s[u].begin(); ite != s[u].end(); ++ite){
				if(s[u].find((*ite)-1) == s[u].end()
				&& s[u].find((*ite)-(1ULL<<32)) == s[u].end()){
				}else{
					s[v].insert(*ite);
				}
				if(s[u].find((*ite)+1-(1ULL<<32)) != s[u].end()
				&& s[u].find((*ite)+1) == s[u].end()){
					s[v].insert((*ite)+1);
				}
				if(s[u].find((*ite)+(1ULL<<32)-1) != s[u].end()
				&& s[u].find((*ite)+(1ULL<<32)) == s[u].end()){
					s[v].insert((*ite)+(1ULL<<32));
				}
			}
			s[u].clear();
			if(s[v].size() == 0){
				printf("Case #%d: %d\n", testcase, t);
				break;
			}
		}
	}
	return 0;
}
