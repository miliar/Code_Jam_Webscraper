#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <map>
#include <limits.h>
#include <signal.h>

#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ROF(i, a, b) for ( i = a; i >= b; i-- )
#define ALL(v) (v).begin(), (v).end()
#define MAX(a, b) ((a) >= (b) ? (a) : (b))
#define MIN(a, b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SWAP(a, b) typeof(a) T; T=a; a=b; b=T;
#define mx 55
using namespace std;
//using namespace __gnu_cxx;

int main()
{
	int test , Test;

	scanf("%d",&test);
	int n , m , i , j;
	Test = 0;
	while(test--) {
		char A[mx][mx];
		Test++;
		scanf("%d%d",&n,&m);

		FOR(i,1,n) {
			FOR(j,1,m) {
				cin >> A[i][j];
			}
		}
		bool f = 0;
		for(i = 1; i <= n; i++) {
			for(j = 1; j <= m;j++) {
				if(A[i][j] == '#') {
					if(A[i][j+1] == '#' && A[i+1][j] == '#' && A[i+1][j+1] == '#') {
						A[i][j+1] = '\\';
						A[i][j] = '/';
						A[i+1][j] = '\\';
						A[i+1][j+1] = '/';
					}
					else {
						f = 1;
						break;
					}
				}
			}
		}
		if(f) {	
			printf("Case #%d:\n",Test);
			cout << "Impossible\n";
		}
		else {
			printf("Case #%d:\n",Test);
			FOR(i,1,n) {
				FOR(j,1,m) {
					cout << A[i][j];
				}
				cout << endl;
			}
		}
	}
		
	return 0;
}
