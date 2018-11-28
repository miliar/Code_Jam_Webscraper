#include <cstring>
#include <iostream>
#include <sstream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <set>
#include <list>
#include <map>
#include <iterator>
#include <cctype>
#include <stack>
#include <cassert>
#include <cmath>
using namespace std;

#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FALL(ii,vv) for (int (ii)=0; (ii)<(vv).size();(ii)++)
#define REP(ii,vv) for (int (ii)=0; (ii)<(vv); (ii)++)
#define ALL(a) a.begin(), a.end()
#define MP make_pair
#define PB push_back

typedef long long ll;
typedef pair<int,int> pii;

int n,k;

int main(){
	int tst;
	scanf("%d",&tst);
	FUP(testNo,1,tst){	
		scanf("%d %d",&n,&k);
		if (k%(1<<n)==(1<<n)-1) printf("Case #%d: ON\n",testNo);
		else printf("Case #%d: OFF\n",testNo);
	}
	return 0;
}
