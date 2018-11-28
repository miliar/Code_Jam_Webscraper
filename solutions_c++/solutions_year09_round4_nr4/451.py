#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/

struct point{
	int x,y;
};
double dist(const point &a, const point &b){
	return sqrt((double)(a.x-b.x)*(a.x-b.x) + (double)(a.y-b.y)*(a.y-b.y));
}
int t,n;
point a[5];
int r[5];
int main(){
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		scanf("%d",&n);
		For(i,0,n){
			scanf("%d%d",&a[i].x,&a[i].y);
			scanf("%d",&r[i]);
		}
		if (n==1){
			printf("Case #%d: %d\n",cas,r[0]);
		}
		if (n==2){
			printf("Case #%d: %d\n",cas,max(r[0],r[1]));

		}
		if (n==3){
			double ret=0,ans=1e100;
			ret=max(0.5*(dist(a[0],a[1])+r[1]+r[0]),(double)r[2]);
			ans<?=ret;
			ret=max(0.5*(dist(a[0],a[2])+r[2]+r[0]),(double)r[1]);
			ans<?=ret;
			ret=max(0.5*(dist(a[2],a[1])+r[1]+r[2]),(double)r[0]);
			ans<?=ret;
			printf("Case #%d: %.5lf\n",cas,ans);
		}

	}
	return 0;
}
