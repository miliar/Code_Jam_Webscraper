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
	void out() const {cout << x << ' ' << y <<' ';}
};
inline bool operator<(const point &a, const point &b){
	return a.x<b.x || (a.x==b.x && a.y<b.y);
}
inline point operator+(const point &a, const point &b){
	point ret;
	ret.x=a.x+b.x; ret.y=a.y+b.y;
	return ret;
}
inline bool operator==(const point &a, const point &b){
	return (a.x%3==b.x%3) && (a.y%3==b.y%3);
}
point a[101000];
int t,n,A,B,C,D,M;
int main(){
	point Z; Z.x=Z.y=0;
	freopen("input1.txt","r",stdin);
	scanf("%d",&t);
	for(int cas=1;t--;cas++){
		scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&a[0].x,&a[0].y,&M);
		For(i,1,n){
			a[i].x=((i64)A*a[i-1].x +B)%M;
			a[i].y=((i64)C*a[i-1].y +D)%M;
		}
		map<point,int> M;
		For(i,0,n){
			//a[i].out(); cout << endl;
			a[i].x%=3;a[i].y%=3;
			M[a[i]]++;
		}
		i64 ret=0;
	//	cout << "DONE \n";
		FOREACH(M,it)
			FOREACH(M,jt)
				FOREACH(M,kt){
					if (it->first < jt->first) continue;
					if (jt->first < kt->first) continue;
					if (!(it->first + jt->first  +kt->first ==Z)) continue;
				//	it->first.out(); jt->first.out(); kt->first.out(); cout << ret <<  endl;
					if (it==jt && it==kt){
						i64 temp=it->second;
						ret+= (temp)*(temp-1)*(temp-2)/6;
						continue;
					}
					if (it==jt || it==kt || kt==jt ){
						i64 temp=it->second; it->second--;
						temp*= jt->second; jt->second--;
						temp*=kt->second; kt->second--;
						ret+=temp/2;
						kt->second++;
						jt->second++;
						it->second++;	
						continue;					
					}
					ret+= (it->second)*(jt->second)*(kt->second);
				}
		printf("Case #%d: %lld\n",cas,ret);
			
	}
	return 0;
}

