#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <limits>

using namespace std;

typedef long long 		LL;
typedef vector<int> 	VI;
typedef pair<int, int> 	PII;

#define FOR(i,a,b) 		for(int i = (a); i < (b); ++i)
#define REP(i,N) 		for(int i = 0; i < (N); ++i)
#define FORD(i,a,b) 	for(int i = (a); i >= (b); --i)
#define FOREACH(i,c) 	for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

#define SIZE(x)			((int)(x.size()))
#define LENGTH(x) 		((int)(X.length()))
#define ALL(x) 			(x).begin(),(x).end()
#define SORT(x) 		sort(ALL(x))
#define REVERSE(x) 		reverse(ALL(x))
#define UNIQUE(x) 		a.resize(unique(ALL(x)) - x.begin())
#define REMOVE(a, b) 	a.resize(remove(ALL(a), b) - a.begin())
#define FIND(a, b) 		find(ALL(a), b)
#define FILL(a, b) 		memset(a, b, sizeof(a))
#define BS(a, b) 		binary_search(ALL(a), b)

#define PB 				push_back

int main() {
	char map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 
					'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 
					'j', 'p', 'f', 'm', 'a', 'q'};
	int T;
	char s[1000];
	scanf("%d\n", &T);
	REP(i, T) {
		gets(s);
		REP(j, strlen(s)) {
			if(isalpha(s[j])) s[j] = map[s[j] - 'a'];
		} 
		printf("Case #%d: %s\n", i + 1, s);
	}
}

