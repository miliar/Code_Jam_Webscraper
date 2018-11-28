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
	int A, B, T, res, k;
	char s1[10], s2[10];
	scanf("%d\n", &T);
	REP(i, T) {
		scanf("%d%d", &A, &B);
		res = 0;
		FOR(j, A, B) {
			sprintf(s1, "%d", j);
			sprintf(s2, "%d", j);
			int l = strlen(s2);
			rotate(s2,s2 + 1, s2 + l);
			while(strcmp(s1, s2)) {
				sscanf(s2, "%d", &k);
				if(s2[0] != '0' && k <= B && k > j) res++;
				rotate(s2,s2 + 1, s2 + l);
			}
		} 
		printf("Case #%d: %d\n", i + 1, res);
	}
}