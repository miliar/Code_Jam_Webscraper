#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>
#define PB push_back
#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
#define INF 1000000000

using namespace std;

int body(int t) {
	int n,a,b,m;
	vector<int> v;
	scanf("%d%d%d",&n,&a,&b);
	REP(i,n) {
		scanf("%d",&m);
		v.PB(m);
	}
	for (int i=a; i<=b; i++) {
		bool ba=1, bb=1;
		REP(j,n) {
			if (v[j]%i>0&&i%v[j]>0) ba=0;
			if (!ba) break;
		}
		if (ba) {
			printf("Case #%d: %d\n",t,i);
			return 0;
		}
	}
	printf("Case #%d: NO\n",t);
}

int main()	{
/*
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
*/


	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);


/*
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
*/

	int k;
	scanf("%d",&k);
	for (int t=1; t<=k; t++) {
		body(t);
	}
    return 0;
}
