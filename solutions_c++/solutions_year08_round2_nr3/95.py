
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
#define For(i,a,b) for(i64 i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/
int ret[10000],t;
void gen(int n){
	int cpos=0;
	CLR(ret,-1);
	For(i,0,n){
	
		int req=i;
		while (req){
			while (ret[cpos]!=-1) cpos=(cpos+1)%n;
			cpos=(cpos+1)%n;
			req--;
		}
		while (ret[cpos]!=-1) cpos=(cpos+1)%n;
		ret[cpos]=i+1; 
		cpos=(cpos+1)%n;		

	
	}
	

}
int n,k,x;
int main(){
	freopen("input3.txt","r",stdin);
	scanf("%d",&t);
	for(int cas=1;t--;cas++){
		scanf("%d",&n);
		gen(n);
		scanf("%d",&k);
		printf("Case #%d:",cas);
		while (k--){
			scanf("%d",&x);
			printf(" %d",ret[x-1]);
		}
		putchar(10);
	
	}
	return 0;
}
