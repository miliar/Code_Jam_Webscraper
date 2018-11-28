#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <climits>
#define REP(i,n) for(int (i)=0, _n=(n); (i) < (_n); i++)
#define REPD(i,n) for(int (i)=(n-1); i >= 0; i--)
#define FOR(i,a,n) for(int (i)=(a),_n=(n); (i) <= (_n); (i)++)
#define FORD(i,a,n) for(int (i)=(a),_n=(n); (i) >= (_n); (i)--)
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(cs,1,test){
		int n;int small = 1000000000;
		int t,bit=0;
		int ans=0;
		scanf("%d",&n);
		REP(i,n){
			scanf("%d",&t);
			bit^=t;
			small = min(small,t);
			ans+=t;
		}	
		
		printf("Case #%d: ",cs);
		if(bit)puts("NO");
		else printf("%d\n",ans-small);
	}
    return 0;
}
