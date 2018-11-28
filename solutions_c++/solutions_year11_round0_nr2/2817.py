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
#define pb(x) push_back(x)
using namespace std;
//using namespace __gnu_cxx;

int A[30][30];
int B[30];
int M[30];

vector <int> R;

int main()
{
	int T;
	scanf("%d",&T);
	string str;
	int sz;
	int ind;
	int i;
	int a , b ;
	int prev;
	int test = 1;
	while(T--) {
		scanf("%d",&a);
		memset(A,0,sizeof(A));
		memset(B,0,sizeof(B));
		memset(M,0,sizeof(M));
		R.clear();
		FOR(i,1,a) {
			str.clear();
			cin >> str;
			//cout << str[0] - 'A' +1 << " " << str[1] - 'A' +1 << endl;
			A[str[0]-'A'+1][str[1]-'A'+1] = str[2] - 'A' + 1;
			A[str[1]-'A'+1][str[0]-'A'+1] = str[2] - 'A' + 1;
		}

		scanf("%d",&b);
		
		FOR(i,1,b) {
			str.clear();
			cin >> str;
			B[str[0]-'A'+1] = str[1]-'A'+1;
			B[str[1]-'A'+1] = str[0]-'A'+1;
		}
		scanf("%d",&sz);
		str.clear();
		cin >> str;
		
		
		//	cout << B[str[0]-'A'+1] << endl;
		M[str[0]-'A'+1]++;
		prev = str[0] -'A'+1;
		R.pb(str[0]-'A'+1);
		ind = 1;
		//sz = str.size();
		int val;
		
		for(i = 1; i < sz;) {
			val = str[i] - 'A' +1;
		//	cout <<"P" <<  prev  << " " << val << endl;
			
			if(A[prev][val]) {
		//		cout << "Y ";
				M[prev]--;
				R[ind-1] = A[prev][val];
				prev = R[ind-1];
				i++;
				continue;
			}
			else if(M[B[val]]) {
				memset(M,0,sizeof(M));
				R.clear();
		//		cout << "R ";
				ind = 0;
				i = i+1;
				if(i < sz) {
					prev = str[i] - 'A' + 1;
					M[prev]++;
					R.pb(prev);
					ind = 1;
					i++;
				}
				continue;
				
			}
			else {
		//		cout <<"Nothing\n";	
				M[val]++;
				R.pb(val);
				prev = R[ind];
				ind++;
			}
			i++;
			//cout << R.size() << endl;
		//	for(int j = 0; j < R.size(); j++) {
		//		cout << R[j] << " ";
		//	}
		//	cout << endl;

		}
		sz = R.size();
		//cout << sz << endl;
		printf("Case #%d: [",test);
		FOR(i,0,sz-2) {
			printf("%c, ",(char)(R[i]+'A'-1));
		}
		if(sz-1 >= 0)
		printf("%c",(char)(R[sz-1]+'A'-1));

		printf("]\n");
		test++;
	}

		
	return 0;
}
