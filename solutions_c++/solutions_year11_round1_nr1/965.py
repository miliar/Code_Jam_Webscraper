#include <map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define xx first
#define yy second
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////

int main(){
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test = 1;test <= T;test++){
		int pd, pg;
		long long n;
		scanf("%I64d%d%d",&n,&pd,&pg);
		printf("Case #%d: ",test);
		if (pd == 0){
			if (pg == 100) printf("Broken\n");
			else printf("Possible\n");
			continue;
		}
		else if (pd == 100){
			if (pg == 0) printf("Broken\n");
			else printf("Possible\n");
			continue;
		}
		else if (pg == 0){
			if (pd > 0) { printf("Broken\n"); continue; }
		}
		else if (pg == 100){
			if (pd < 100) { printf("Broken\n"); continue; }
		}
		int d = 100 / __gcd(pd, 100);
		if (d > 0 && d <= n) printf("Possible\n");
		else printf("Broken\n");
	}
//	system("pause");
	return 0;
}
