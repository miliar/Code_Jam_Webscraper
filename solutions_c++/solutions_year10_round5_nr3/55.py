#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
using namespace std;
typedef pair<int,int> pi;
int main() {
    int tests;
    scanf("%d", &tests);
    for(int z=1; z<=tests; z++) {
	int ile;
	scanf("%d", &ile);
	priority_queue<pi> Q;
	map<int,int> M;
	while(ile--) {
	    pi tmp;
	    scanf("%d %d", &tmp.SE, &tmp.FI);
	    Q.push(tmp);
	    M[tmp.SE] = tmp.FI;
	}
	int wynik = 0;
	while(!Q.empty()) {
	    pi tmp = Q.top();
	    Q.pop();
	    if(M[tmp.SE] != tmp.FI)
		continue;
	    int x = M[tmp.SE];
	    wynik += x/2;
	    M[tmp.SE] = x&1;
	    
	    int val = M[tmp.SE-1];
	    val += x/2;
	    M[tmp.SE-1] = val;
	    if(val > 1)
		Q.push(MP(val, tmp.SE-1));
	    
	    val = M[tmp.SE+1];
	    val += x/2;
	    M[tmp.SE+1] = val;
	    if(val > 1)
		Q.push(MP(val, tmp.SE+1));
	}
	printf("Case #%d: %d\n", z,  wynik);
    }
    return 0;
}