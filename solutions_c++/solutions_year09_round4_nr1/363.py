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

int n , v[50];

void solve() {
	int i, res = 0 , j;
	string s;
	cin >> n;
	for ( i = 0 ; i < n ; i++)
	{
		cin >> s;
		for (j = n-1 ; j > 0 ; j--)
			if (s[j] == '1')
				break;
		v[i] = j;
	}
	for (i = 0 ; i < n ; i++)
	{
		for (j = i ; j < n ; j++)
			if ( v[j] <= i )
				break;
		while ( j > i ) {
			res++;
			swap(v[j],v[j-1]);
			j--;
		}
	}

	cout << res << endl;
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
