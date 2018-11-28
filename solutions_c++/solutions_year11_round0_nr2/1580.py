// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define SIZE(X) int(X.size())

bool Oposed[256][256];
char Transform[256][256];

int main() {
	int T, C, D, N;
	char a, b, c, buffer[128];
	scanf("%d", &T);
    FORTO(t,1,T) {
		vector<char> Stack;
		FORTO(i,'A','Z') FORTO(j,'A','Z') {
			Oposed[i][j] = Transform[i][j] = 0;
		}
    	scanf("%d", &C);
    	FOR(i,C) {
    		scanf(" %c%c%c", &a, &b, &c);
    		Transform[a][b] = Transform[b][a] = c;
    	}
    	scanf("%d", &D);
    	FOR(i,D) {
    		scanf(" %c%c", &a, &b);
    		Oposed[a][b] = Oposed[b][a] = true;
    	}
    	scanf("%d %s", &N, &buffer);
    	FOR(i,N) {
    		if (!Stack.empty()) {
    			char tr = Transform[Stack.back()][buffer[i]];
    			if (tr) {
    				Stack.pop_back();
    				Stack.push_back(tr);
    			} else {
    				bool del = false;
    				FOR(j,SIZE(Stack)) {
    					if (Oposed[Stack[j]][buffer[i]]) {
    						del = true;
    					}
    				}
    				if (del) {
    					Stack.clear();
    				} else {
    					Stack.push_back(buffer[i]);
    				}
    			}
    		} else {
    			Stack.push_back(buffer[i]);
    		}
    	}
    	printf("Case #%d: [", t);
    	FOR(i,SIZE(Stack)) {
    		if (i) printf(", ");
    		printf("%c", Stack[i]);
    	}
    	printf("]\n");
	}
	return 0;
}

