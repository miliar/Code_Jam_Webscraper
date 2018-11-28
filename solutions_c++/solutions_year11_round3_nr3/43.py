#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(S,i)		( (S) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )

void solve() {
	int N , v[110], a,i,b;
	cin >> N >> a >> b;
	for (i = 0 ; i < N ; i++) {
		cin >> v[i];
	}
	while (a <= b) {
		bool ok = true;
		for (i = 0 ; ok && i < N ; i++) 
			ok = (a % v[i] == 0) || (v[i] % a == 0);
		if (ok) {
			printf("%d\n",a);
			return;
		}
		a++;
	}
	cout << "NO" << endl;
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ": ";
		solve();
	}	
	return 0;
}
