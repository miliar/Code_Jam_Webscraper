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
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(cs,1,test){
		int n,l,h,arr[200];
		int ans=-1;bool b[200]={};
		int num1=0;
		scanf("%d %d %d",&n,&l,&h);
		
		REP(i,n)
			scanf("%d",arr+i);
		
					
		FOR(i,l,h){
			int num2=0;
			REP(j,n)
				if(arr[j] % i == 0 || i % arr[j] == 0)
					num2++;
			if(num2==n){
				ans = i;
				break;	
			}
		}
		
		printf("Case #%d: ",cs);
		if(ans == -1)puts("NO");
		else printf("%d\n",ans);
	}
	
    return 0;
}
