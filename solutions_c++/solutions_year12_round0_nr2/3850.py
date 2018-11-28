#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cassert>
#include <climits>
#include <functional>
#include <bitset>

#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define rep(i,n) for(int i=0;i<n;i++)
#define print(x) cout<<#x<<" is "<<x<<endl;
#define inf 2000000000
#define eps 1e-8
#define fill(x,y) memset(x,y,sizeof(x))

using namespace std;

int a[200], ms[31][2];

int main() {
    int Nt;
    ms[1][0] = 1;
    ms[2][0] = 1, ms[2][1] = 2;
    int b[3];
    for(int i=3; i<=30; i++) {
	int v = i;
	b[0] = v/3;
	v -= b[0];
	b[1] = v/2;
	v -= b[1];
	b[2] = v;
	sort(b, b+3);
	if(i%3 == 1) {
	    ms[i][0] = ms[i][1] = b[2];
	}
	else {
	    ms[i][0] = b[2];
	    ms[i][1] = b[2]+1;
	}
    }
    scanf("%d",&Nt);
    for(int ttt=1; ttt <= Nt; ttt++) {
	printf("Case #%d: ",ttt);
	int sur, N, p;
	scanf("%d%d%d",&N,&sur,&p);
	rep(i,N)
	    scanf("%d",&a[i]);
	int ans = 0;
	sort(a,a+N, greater<int>());
	rep(i,N) {
	    if(a[i]==0 || a[i]==1) {
		if(a[i] >= p)
		    ans++;
		continue;
	    }
	    if(ms[a[i]][0] >= p)
		ans++;
	    else if(ms[a[i]][1] >= p && sur > 0) {
		sur--;
		ans++;
	    }
	}
	printf("%d\n",ans);
    }
    return 0;
}
