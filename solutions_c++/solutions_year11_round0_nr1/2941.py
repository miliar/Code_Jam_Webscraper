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
#define pii pair<char,int>
#define pb(x) push_back(x)

using namespace std;
//using namespace __gnu_cxx;

vector <pii> C;
vector <int> A;
vector <int> B;

int main()
{
	int n;
	int i;
	int T;
	char a;
	int b;
	scanf("%d",&T);
		
	int rob1 , rob2 , ind1 , ind2 , t , time;
	int test = 1;
	while(T--) {
		
		scanf("%d",&n);
		time = 0;
		C.clear();
		A.clear();
		B.clear();
		FOR(i,1,n) {
			//scanf("%c%d",&a,&b);
			cin >> a >> b;
			C.pb(pii(a,b));
//			cout << C[i-1].first << endl;
			if(a == 'O') {
				A.pb(b);
			}
			else {
				B.pb(b);
			}
		}

		rob1 = 1;
		rob2 = 1;
		ind1 = 0;
		ind2 = 0;

		FOR(i,0,n-1) {
			//cout << rob1 << " " << rob2 << endl;
			if(C[i].first == 'O') {
				t = ABS(C[i].second-rob1)+1;
				rob1 = C[i].second;
				ind1++;
				
				if(B[ind2] < rob2) {
					rob2 = rob2 - (t);
					if(rob2 < B[ind2]) {
						rob2 = B[ind2];
					}
				}
				else {
					rob2 = rob2 + (t);
					if(rob2 > B[ind2]) {
						rob2 = B[ind2];
					}
				}
				time += t;
			}
			else {
				t = ABS(C[i].second-rob2)+1;
				rob2 = C[i].second;
				ind2++;

				if(A[ind1] < rob1) {
					rob1 = rob1 - (t);
					if(rob1 < A[ind1]) {
						rob1 = A[ind1];
					}
				}
				else {
					rob1 = rob1 + (t);
					if(rob1 > A[ind1]) {
						rob1 = A[ind1];
					}
				}
				time+=t;
			}
		}
		printf("Case #%d: %d\n",test,time);
		test++;
	}	
	return 0;
}
