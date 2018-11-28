#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#include <iostream>
#include <sstream>
#include <map>
#include <algorithm>

#define zbwmqlw
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define pow(x) (1<<(x))
#define powLL(x) ((1LL)<<(LL)(x))
#define sqr(x) ((x)*(x))
#define abs(x) ((x)>0?(x):-(x))
#define lch(x) (((x)<<1)+1)
#define rch(x) (((x)<<1)+2)
#define PI 3.141592653589793238463
#define fill(x,y) memset((x),(y),sizeof(x))
#define rep(x,l,r) for ((x)=(l);(x)<=(r);++(x))
#define repd(x,r,l) for ((x)=(r);(x)>=(l);--(x))

//using namespace std;
using std::pair;
using std::make_pair;
using std::cin;
using std::cout;
using std::endl;
using std::stringstream;
using std::iostream;
using std::sort;
typedef long long LL;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-7;
template<class T> inline void checkmin(T &a,const T &b) {if (b<a) a=b;}
template<class T> inline void checkmax(T &a,const T &b) {if (b>a) a=b;}

int T,n,k;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
#endif
	int t;
	for (t=1,scanf("%d",&T);t<=T;++t) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",t);
		if ((k+1)&(pow(n)-1)) printf("OFF\n");else printf("ON\n");
	}
}