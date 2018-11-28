
/*Paresh Verma*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <queue>		//max heap implementation
#include <limits.h>

#define pub push_back
#define pob pop_back
#define fi first
#define se second
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.end() ; it++ ) cout << *it << " "; cout << endl; }

using namespace std;

//class comparators for queue and others
class classcomp{
	public:
		bool operator() (const int& l, const int& r)const{
			return l<r;
		}
};
typedef pair<int, int> pii;
int d[10010], l[10010];
int n, dis;
map<pii,int> dd;

int rec(int in, double len){
	if(in>=n){
		return -1;
	}
	pii xx, yy;
	xx.fi=in; xx.se=len;
	if(dd[xx]!=0){
		return dd[xx];
	}
	int i,j,k;
	if(d[in]+len>=dis){
		return dd[xx]=1;
	}
	j=-1;
	for(i=in+1;i<n;i++){
		if(d[in]+len>=d[i] ){
			j = rec(i, min(d[i]-d[in], l[i]));
			if(j==1){
				return dd[xx]=1;
			}
		}
	}
	return dd[xx]=-1;
}


int main(){
	int T;
	int i,j,k,m;
	scanf("%d",&T);
	for(int p=1; p<=T; p++){
		dd.clear();
		printf("Case #%d: ",p);
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d",&d[i],&l[i]);
		}
		scanf("%d",&dis);
		if(l[0]<d[0]){
			printf("NO\n");
			continue;
		}
		rec(0,d[0]);
		pii xx;
		xx.fi=0; xx.se=d[0];
		if(dd[xx]==1){
			printf("YES\n");
		}
		else{
			printf("NO\n");
		}
	}
	return 0;
}
