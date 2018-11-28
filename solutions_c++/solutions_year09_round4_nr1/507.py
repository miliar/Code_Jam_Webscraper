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
int t;
int main(){
	scanf("%d",&t);
	pair<int,int>  a[55];
	int n;
	char buf[100];
	for(int cas=1;cas<=t;cas++){
		scanf("%d",&n);
		For(i,0,n){
			scanf("%s",buf);
			a[i].first=0;
			For(j,0,n) if (buf[j]=='1') a[i].first>?=j;
			a[i].second=i;	
		}
		int ret=0;
		For(i,0,n){
			if (a[i].first>i){
				For(j,i+1,n){
					if (a[j].first<=i){
						int k=j;
						while (k>i){
							swap(a[k],a[k-1]);
							k--;
							ret++;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",cas,ret);
	}
	return 0;
}
