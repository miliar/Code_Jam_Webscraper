#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define FOR(i,a,b) for(__typeof(b) i=(a);i!=(b);i++)
#define REP(i,n) FOR(i,0,n)
#define EACH(i,a) FOR(i,a.begin(),a.end())
#define PB push_back
#define ALL(a) a.begin(),a.end()
#define iss istringstream
#define SZ(a) (int)a.size()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long

int T,N;
int mem[99][99];
int p[99],q[99];

inline int solve(int L) {
	if (L==1) {return 0;}
	int ind=0;
	while (ind<L && q[ind]!=L-1) {ind++;}
	int ret=0;
	for(int i=ind;i<L-1;i++) {
		swap(q[i],q[i+1]);
		ret++;
	}
	return ret+solve(L-1);
}

inline int calc() {
	memcpy(q,p,sizeof(p));
	return solve(N);
}

inline bool inRow(int memrow,int row) {
	for(int i=row+1;i<N;i++) {
		if (mem[memrow][i]!=0) {return false;}
	}
	return true;
}

inline int getChar() {
	char ret;
	scanf("%c",&ret);
	while (ret!='0' && ret!='1') {scanf("%c",&ret);}
	return ret-'0';
}

int main() {
	scanf("%d",&T);
	for(int h=1;h<=T;h++) {
		scanf("%d",&N);
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				mem[i][j]=getChar();
			}
			p[i]=i;
		}
		int ans=99999999;
		do {
			bool yes=true;
			for(int i=0;i<N;i++) {
				if (!inRow(i,p[i])) {yes=false;break;}
			}
			if (yes) {
				ans=min(ans,calc());
			}
		}	while(next_permutation(p,p+N));
		printf("Case #%d: %d\n",h,ans);				
	}
	return 0;
}








