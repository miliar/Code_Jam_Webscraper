#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iterator> 
#include <algorithm> 
#include <utility> 

// container 
#include <vector> 
#include <string> 
#include <set> 
#include <map> 

// C-style 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 

using namespace std;

#define FOR(_I,_A,_B) for(int _I=(_A);(_I)<(_B);_I++)
#define FORE(_I,_A,_B) for(int _I=(_A);(_I)<=(_B);_I++) 
#define REP(_I,_B) for(int _I=(0);(_I)<(_B);_I++) 

typedef long long ll;
typedef long double ld;

set<string> s;
char line[1000];

int N, S, Q;

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d\n", &N);
	FORE(tc, 1, N) {
		s.clear();

		scanf("%d\n", &S);
		REP(i, S) gets(line);

		scanf("%d\n", &Q);
		int res=0;
		REP(i, Q) {
			gets(line);
			s.insert(line);
			if(s.size()==S) {
				s.clear();
				res++;
				s.insert(line);
			}	
		}

		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}
