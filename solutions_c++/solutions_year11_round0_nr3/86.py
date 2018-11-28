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
int a[1000];
int main(){
	freopen("c-large.in","r",stdin);
	freopen("c-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++){
		int n,ret=0,allxor=0;
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%d",&a[i]),allxor^=a[i];
		printf("Case #%d: ",test);
		if (allxor) { printf("NO\n",test); continue; }
		sort(a,a+n);
		//////////////
		for (int i=1;i<n;i++)
			ret+=a[i];
		printf("%d\n",ret);
	}
//	system("pause");
	return 0;
}
