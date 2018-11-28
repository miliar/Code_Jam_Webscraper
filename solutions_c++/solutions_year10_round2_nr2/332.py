#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cassert>
#include <utility>
#include <sstream>
#include <cstring>
using namespace std;

#define FALL(ii,vv) for (int (ii)=0; (ii)<(vv).size();(ii)++)
#define REP(i,b) for(int (i)=(0);(i)<(b);(i)++)
#define FUP(i,a,b) for(int (i)=(a); (i)<=(b); (i)++)
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef vector<int> vi;
typedef long long ll;

int N,K,B,T;
int x[55],v[55];

int main(){
	int test;
	scanf("%d",&test);
	FUP(ii,1,test){
		scanf("%d %d %d %d",&N,&K,&B,&T);
		REP(i,N) scanf("%d",&x[i]);
		REP(i,N) scanf("%d",&v[i]);
		
		int res = 0, niedoszlo = 0;
		
		for(int i=N-1; i>=0; i--){
			if (K==0) break;
			if (B-x[i] <= T * v[i]){
				res+=niedoszlo;
				K--;
			}
			else niedoszlo++;
		}
		
		printf("Case #%d: ",ii);
		if (K!=0) puts("IMPOSSIBLE");
		else printf("%d\n",res);
	}
	return 0;
}
