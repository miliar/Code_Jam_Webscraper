/*
ID: harrymw1
LANG: C++
TASK: 
*/
 
#include <iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include <cstdio>
#include<map>
#include<stack>
#include<set>
#include<queue>
#include<cctype>
#include<assert.h>
#include<numeric>
#include<ctime>
#include<iterator>
//#include<sstream>
using namespace std;

#define PI acos(-1.0)
#define fore(i,a) for(int i=0; i<(a); i++)
#define forv(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define all(x) x.begin(),x.end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
/*template<class T> string toString(T n){
	ostringstream ost;ost<<n;ost.flush();
	return ost.str();
}*/

//__builtin_popcount(int x);
typedef struct Seg{int l,r;}Seg;
int main()
{
	freopen("A.in.txt", "r", stdin);
	freopen("A.out.txt", "w", stdout);
	//clock_t start, finish;
   	//double duration;
   	//start = clock();
	int t,ca=1;cin>>t;
	while(t--){
		int n;scanf("%d",&n);
		Seg seg[1002];
		for(int i=0;i<n;i++)scanf("%d%d",&seg[i].l,&seg[i].r);
		int ret=0;
		for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
			if((seg[i].l-seg[j].l)*(seg[i].r-seg[j].r)<=0)++ret;
		}
		printf("Case #%d: %d\n",ca++,ret);
	}


	//finish = clock();
   	//duration = (double)(finish - start) / CLOCKS_PER_SEC;
	//printf( "%f seconds\n", duration );
	return 0;
}
