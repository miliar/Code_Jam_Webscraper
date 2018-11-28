#include <cstdio>
#include <cassert>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
using namespace std;

#define rep(i,a,b) for(int i=(a); i<(b); ++i)

int main() {
	int T;
	scanf("%d", &T);
	rep(t,0,T) {
		int C;
		scanf("%d", &C);
		map<pair<char,char>, char> combine;
		rep(c,0,C) {
			char s[10];
			scanf(" %s", s);
			combine[make_pair(s[0], s[1])] = s[2];
			combine[make_pair(s[1], s[0])] = s[2];
		}
		int D;
		scanf("%d", &D);
		map<char, set<char> > oppose;
		rep(d,0,D) {
			char s[10];
			scanf(" %s", s);
			oppose[s[0]].insert(s[1]);
			oppose[s[1]].insert(s[0]);
		}
		int N;
		scanf("%d", &N);
		char s[200];
		scanf(" %s", s);
		vector<char> elements;
		rep(n,0,N) {
			elements.push_back(s[n]);
			while(elements.size()>1) {
				char c1 = elements[elements.size()-2], c2 = elements[elements.size()-1];
				if(combine.count(make_pair(c1,c2))) {
					elements.pop_back();
					elements.pop_back();
					elements.push_back(combine[make_pair(c1,c2)]);
				}
				else break;
			}
			if(elements.size()>1)
				rep(i, 0, (int)elements.size()-1) {
					if(oppose[elements.back()].count(elements[i])) {
						elements.clear();
						break;
					}
				}
		}
		printf("Case #%d: [", t+1);
		if(!elements.empty()) printf("%c", elements[0]);
		rep(i,1,(int)elements.size()) printf(", %c", elements[i]);
		printf("]\n");
	}
	return 0;
}