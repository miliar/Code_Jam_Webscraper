#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>

#define FOR(i, a, b) for(int i = int(a); i < int(b); i++)
#define INF 2000000000
#define EPS 1e-9
#define PB push_back
#define MP make_pair
#define F first
#define S second
using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

int main() {
//	freopen("magicka.in", "r", stdin);
//	freopen("magicka.out", "w", stdout);
	
	int T, tc = 0;
	scanf("%d", &T);
	
	while(T--) {
		int c;
		scanf("%d", &c);
		
		char combine[300][300] = {0};
		for(int i = 0; i < c; ++i) {
			char tmp[5];
			scanf("%s", &tmp);
			
			combine[tmp[0]][tmp[1]] = combine[tmp[1]][tmp[0]] = tmp[2];
		}					
		
		int d;
		scanf("%d", &d);
		
		bool opposed[300][300] = {0};
		for(int i = 0; i < d; ++i) {
			char tmp[5];
			scanf("%s", &tmp);
			
			opposed[tmp[0]][tmp[1]] = opposed[tmp[1]][tmp[0]] = 1;
		}
		
		int n;
		scanf("%d", &n);
		
		char s[105];
		scanf("%s", &s);
		
		vector <char> l;
		int len = strlen(s);
		
		int used[300] = {0};
		for(int i = 0; i < len; ++i) {
			used[s[i]]++;
			if(l.empty()) l.PB(s[i]);
			else if(combine[l.back()][s[i]] > 0) {
				char tmp = combine[l.back()][s[i]];
				
				used[l.back()]--;
				used[s[i]]--;
				used[combine[l.back()][s[i]]]++;
				l.pop_back(); l.PB(tmp);
			} 
			else {
				bool oppos = 0;
				for(int j = 0; j < 300; ++j) 
					if(opposed[s[i]][j] && used[j]) { oppos = 1; break; }
				
				if(oppos) {
					for(int j = 0; j <= i; ++j) used[s[j]] = 0;
				
					l.clear();
				} 
				else l.PB(s[i]);
			}
//			for(int j = 0; j < l.size(); ++j) printf("(%c)", l[j]); printf("\n");
//			for(int j = 'A'; j <= 'Z'; ++j) printf("%c=%d ", j, used[j]); printf("\n");
		}
		
		printf("Case #%d: [", ++tc);
		for(int i = 0; i < l.size(); ++i) {
			if(i) printf(", ");
			printf("%c", l[i]);
		}
		printf("]\n");
	}
	
	return 0;
}
