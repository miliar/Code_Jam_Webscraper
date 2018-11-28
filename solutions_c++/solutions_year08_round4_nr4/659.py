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
const int maxn=1010;
char buf[maxn],temp[maxn],a[maxn];
int k,t;
int main(){
	freopen("input4.txt","r",stdin);
	freopen("output4.txt","w",stdout);
	scanf("%d",&t);
	for(int cas=1;t--;cas++){
		scanf("%d",&k);
		scanf("%s",buf);
		int n=strlen(buf);
		For(i,0,k) a[i]=i;
		int ret=n+2;
		do{
			for(int j=0;j<n;j+=k){
				For(i,0,k)
					temp[j+i]=buf[j+a[i]];			
			}
			
			int cur=1;
			For(i,1,n)
				cur+=(temp[i]!=temp[i-1]);
			//cout << temp << ' ' << cur << endl;
			ret=min(ret,cur);
		} while (next_permutation(a,a+k));
		printf("Case #%d: %d\n",cas,ret);
	}
	return 0;
}