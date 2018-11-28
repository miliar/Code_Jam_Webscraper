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
#define MAX 1010
int v[MAX], N;

void solve() {
	int res = 0 , i , j = 0;
	cin >> N;
	for (i = 0 ; i < N ; i++) {
		cin >> v[i];
		j ^= v[i];
	}
	if (j != 0 ) {
		cout << "NO\n";
		return;
	}
	sort(v, v+N);
	for (i = 1 ; i < N ; i++)
		res += v[i];
	/*
	int mask = 0;
	for (i = 1  ; i+1 < two(N) ; i++) {
		p = k = 0;
		int soma = 0;
		for (j = 0 ; j < N ; j++) {
			if (contain(i,j)) {
				soma += v[j];
				k ^= v[j];	
			}	
			else
				p ^= v[j];
		}
		if ( p == k && soma > res) {
			res = soma;
			mask = i;
		}
	}
	*/
	cout << res << endl;
/*	for (j =  0 ; j < N ; j++)
		if (contain(mask,j))
			printf("%d ", v[j]);
	printf("\n");
	*/

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
