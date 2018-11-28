//      hello world


//DS includes
#include<bitset>
#include<complex>
#include<deque>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

//Other Includes
#include<algorithm>
#include<cassert>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iostream>
#include<sstream>

#define oo 			0xBADC0DE
#define s(n)			scanf("%d",&n)
#define sl(n) 			scanf("%lld",&n)
#define sf(n) 			scanf("%lf",&n)
#define fill(a,v) 		memset(a, v, sizeof a)
#define ull 			unsigned long long
#define ll 				long long
#define bitcount 		__builtin_popcount
#define all(x) 			x.begin(), x.end()
#define pb( z ) 		push_back( z )
#define gcd				__gcd

#define FOR(i,n) for (int i=0; i < (n); i++)

using namespace std;


char to[256][256];
bool opp[256][256];

int main(int argc, char** argv) {
	//freopen("ip.txt", "r", stdin); 
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	//freopen("B-small-attempt3.in", "r", stdin); freopen("B-small-attempt3.out", "w", stdout);
	
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	
	int runs;
	cin>>runs;
	for (int X=1; X <= runs; X++) {
		printf("Case #%d: ", X);
		int C; cin>>C;
		fill(to, 0); fill(opp, 0);
		while (C-- > 0) {
			string change;
			cin>>change;
			to[ change[0] ][ change[1] ] = change[2];
			to[ change[1] ][ change[0] ] = change[2];
		}
		int D; cin>>D;
		while (D-- > 0) {
			string op;
			cin>>op;
			opp[ op[0] ][ op[1] ] = 1;
			opp[ op[1] ][ op[0] ] = 1;
		}
		int N; cin>>N;
		string a;
		cin>>a;
		char prevChar = 0;
		string list = "";
		for (int i=0; i < a.size(); i++) {
			if (to[prevChar][a[i]]) {
				list.erase( --list.end() );
				list += prevChar = to[prevChar][a[i]];
				
			} else {
				bool flushed = 0;
				for (int j=0; j < list.size(); j++)
				if (opp[ list[j] ][ a[i] ]) {
					list.clear();
					flushed = 1;
					prevChar = 0;
					break;
				}
				if (!flushed) {
					list += a[i];
					prevChar = a[i];
					
				}
			}
			
		}
		cout <<"[";
		for (int i=0; i < list.size(); i++) {
			cout << list[i];
			if (i+1 != list.size()) {
				cout <<", ";
			}
		}
		cout <<"]"<<endl;
	}
	
	return 0;
}
