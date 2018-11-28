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
const int maxn=250;
const int inf=9999999;
struct node{
	int tim,tr;
};
bool operator<(const node &a,const node &b){
	return a.tim < b.tim;	
}
char buf[maxn];
node A[maxn],D[maxn];
int t,na,nb,N,T;
int main(){
	freopen("b1.in","r",stdin);
	scanf("%d",&t);
	for(int cas=1;t--;cas++){
		int x,y;
		scanf("%d",&T);
		scanf("%d%d",&na,&nb);
		N=0;
		For(i,0,na){
			scanf("%s",buf);
			sscanf(buf,"%d:%d",&x,&y);
			D[i].tim=x*60+y;
			D[i].tr=0;

			scanf("%s",buf);
			sscanf(buf,"%d:%d",&x,&y);
			A[i].tim=x*60+y+T;
			A[i].tr=1;
		}
		For(i,na,na+nb){
			scanf("%s",buf);
			sscanf(buf,"%d:%d",&x,&y);
			D[i].tim=x*60+y;
			D[i].tr=1;
			scanf("%s",buf);
			sscanf(buf,"%d:%d",&x,&y);
			A[i].tim=x*60+y+T;
			A[i].tr=0;		
		}
		N=na+nb;
		sort(A,A+N); A[N].tim=inf; 
		sort(D,D+N); D[N].tim=inf;
		int an=0,dn=0;
		int ret[2]; ret[0]=ret[1]=0;
		int cur[2]; cur[0]=cur[1]=0;
		while (dn < N){
			int ctim=min(A[an].tim,D[dn].tim);
			//cout << ctim << ' ' << cur[0] << ' '<< cur[1] << ' ' << ret[0] << ' ' << ret[1] << endl;
			while (A[an].tim==ctim) cur[A[an++].tr]++ ;
			while (D[dn].tim==ctim){
				if (cur[D[dn].tr]==0) ret[D[dn].tr]++; else cur[D[dn].tr]--;
				dn++;
			}
		}
		printf("Case #%d: %d %d\n",cas,ret[0],ret[1]);
		
	
	}
	return 0;
}
